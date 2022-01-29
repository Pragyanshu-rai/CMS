# from django.shortcuts import redirect
import datetime
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from io import BytesIO
from random import choices
from string import ascii_letters, digits

# importing stuff from cms module which is parallel to cms_api(this) module
from cms.models import *
# , UserSerializer
from cms.serializers import ContactSerializer, HistorySerializer, DoctorSerializer

# importing stuff from cmsUtils module which is parallel to cms_api(this) module
from cmsUtils.apiUtils import models_to_dict, get_contact_or_none, validate_signup
from cmsUtils.mail import sendEmail
from cmsUtils.emailUtils import email_subjects, email_body_text, email_body_html
from cmsUtils.viewUtils import get_user_ip, validate_email_and_get_user


# Create your views here.

instructions = "api-endpoint http://127.0.0.1:8000/cms-api/signup for user registeration (username, password, gender(m/f), dob, address, phone) and "

api_list = [
    "http://127.0.0.1:8000/cms-api/login",
    "http://127.0.0.1:8000/cms-api/patient/",
    "http://127.0.0.1:8000/cms-api/doctor/",
    "http://127.0.0.1:8000/cms-api/history/",
    "http://127.0.0.1:8000/cms-api/details/",
    "http://127.0.0.1:8000/cms-api/reports/",
    "http://127.0.0.1:8000/cms-api/booking/",
    "http://127.0.0.1:8000/cms-api/history/",
    "http://127.0.0.1:8000/cms-api/api-get-otp/",
    "http://127.0.0.1:8000/cms-api/reset-password/",
    "http://127.0.0.1:8000/cms-api/",
]


# stores the userid and otp as key and value pair
otp_book: dict = dict()
# store the userid of the user when otp request is raised
password_reset_request: list = list()


def getInstruction(request):

    try:
        return JsonResponse({"MSG": instructions, "API-List": api_list}, safe=False,)

    except Exception as error:
        print("[SERVER ERROR] get instructions - ", error)
        return JsonResponse({"ERR": "Error occurred while fetching the help instructions from the api"}, safe=False)


@csrf_exempt
def signup(request):

    try:

        if len(request.body) > 0:

            python_data = JSONParser().parse(BytesIO(request.body))
            print(python_data)
            valid = validate_signup(python_data)
            print(valid)

            if valid != None:

                return JsonResponse({"ERR": valid, "authStatus": False}, safe=False)

            print(python_data)
            ser = ContactSerializer(data=python_data)

            if ser.is_valid():
                ser.save()
                print("Data Saved")
                return JsonResponse({"MSG": "DATA SAVED", "DATA": ser.data, "authStatus": True}, safe=False)

            return JsonResponse({"ERR": ser.errors, "authStatus": False}, safe=False)

        else:

            return JsonResponse({"ERR": "Empty Json File, use these '{' '}' ", "authStatus": False}, safe=False)

    except Exception as error:
        print("Exception", error)
        return JsonResponse({"ERR": "Error occurred while registering the patient", "authStatus": False}, safe=False)


@method_decorator(csrf_exempt, name="dispatch")
class request_otp(APIView):

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def __init__(self, **kwargs: any) -> None:
        super().__init__(**kwargs)
        self.__otp_request: str = "otpRequest"

    def __generate_otp(self, request):

        global otp_book, email_body_text, email_body_html, email_subjects
        current_date_time: str = str(datetime.datetime.now()).split(".")[0]

        try:
            email = JSONParser().parse(BytesIO(request.body)).pop("email")
            # genrating a 6-digit random alphanumeric OTP for validation
            otp = "".join(choices(digits + ascii_letters + digits, k=6))
            print(request)
            request.user = validate_email_and_get_user(request, email)
            print(request)
            otp_book[request.user.id] = otp
            user_name = request.user.first_name
            user_ip = get_user_ip(request)
            print(user_name, user_ip)
            text_body = email_body_text[self.__otp_request].format(
                user_name, user_ip, otp, current_date_time)
            html_body = email_body_html[self.__otp_request].format(
                user_name, user_ip, otp, current_date_time)

            if email != "":
                sendEmail(subject=email_subjects[self.__otp_request],
                          body=text_body, to=email, alternative=html_body)
                user_token = str(Token.objects.get(user=request.user))
                print("user token generated")

            else:
                return JsonResponse({"ERR": "'email' is required but not provided!", "authStatus": False}, safe=False)

            return JsonResponse({"MSG": "OTP Sent To The Registered Email.", "authToken": user_token, "authStatus": True, "userId": request.user.id, "firstName": user_name}, safe=False)

        except Exception as error:
            print("[SERVER-ERROR]", error)
            return JsonResponse({"ERR": "Error occurred while generating OTP", "authStatus": False}, safe=False)

    def get(self, request):

        return self.__generate_otp(request)


@method_decorator(csrf_exempt, name="dispatch")
class reset_password(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def __init__(self, **kwargs: any) -> None:
        super().__init__(**kwargs)
        self.__password_change: str = "passwordChange"
        self.__invalid_login: str = "invalidLogin"

    def __validate(sef, request):

        global otp_book, password_reset_request, email_body_text, email_body_html, email_subjects

        try:
            otp = JSONParser().parse(BytesIO(request.body)).pop("otp")

            if otp != "":

                if otp_book.get(request.user.id, None) == otp:
                    # delete the otp once it is validated
                    del otp_book[otp]
                    print("OTP Validated")
                    password_reset_request.append(request.user.id)
                    print("Password Reset Request Raised!")

                else:
                    return JsonResponse({"ERR": "Invalid OTP!", "authStatus": False}, safe=False)

            else:
                return JsonResponse({"ERR": "'otp' is required but not provided!", "authStatus": False}, safe=False)

            return JsonResponse({"MSG": "OTP Sent To The Registered Email.", "OTP": otp, "authStatus": True}, safe=False)

        except Exception as error:
            print("[SERVER-ERROR]", error)
            return JsonResponse({"ERR": error, "authStatus": False}, safe=False)

    def __update_password(self, request):

        global password_reset_request, email_body_text, email_body_html, email_subjects
        current_date_time: str = str(datetime.datetime.now()).split(".")[0]

        try:
            new_password = JSONParser().parse(BytesIO(request.body)).pop("password")
            request.user = validate_email_and_get_user(request)
            user_id = request.user.id
            print(user_id)

            if new_password != "":

                if user_id in password_reset_request:
                    user = User.objects.get(pk=user_id)
                    user.set_password(new_password)
                    user.save()
                    print("password updated")
                    password_reset_request.remove(user_id)
                    print("Password Reset Request Completed!")

                else:
                    print("Invalid Login Attempt! logged at - ", current_date_time)
                    user_email = request.user.email
                    user_name = request.user.first_name
                    user_ip = get_user_ip(request)
                    text_body = email_body_text[self.__invalid_login].format(
                        user_name, user_ip, current_date_time)
                    html_body = email_body_html[self.__invalid_login].format(
                        user_name, user_ip, current_date_time)
                    sendEmail(subject=email_subjects[self.__invalid_login],
                            body=text_body, to=user_email, alternative=html_body)
                    return JsonResponse({"ERR": "Invalid Login Attempt has been logged!", "authStatus": False}, safe=False)

            else:
                return JsonResponse({"ERR": "'password' is required but not provided!", "authStatus": False}, safe=False)

            return JsonResponse({"MSG": "Password reset successful.", "authStatus": True}, safe=False)

        except Exception as error:
            print("[SERVER-ERROR]", error)
            return JsonResponse({"ERR": "Error occurred while updating the password", "authStatus": False}, safe=False)

    def post(self, request):
        return self.__validate(request)

    def put(self, request):
        return self.__update_password(request)

    def patch(self, request):
        return self.__update_password(request)


@method_decorator(csrf_exempt, name="dispatch")
class patient_api(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):

        try:
            # print(len(request.body))
            if len(request.body) > 0:
                try:

                    ct = Contact.objects.get(user_id=request.user.id)
                    data = ContactSerializer(ct).data.copy()
                    data["age"] = age(to_date(str(ct.dob)))
                    print(data)
                    return JsonResponse(data, safe=False)

                except:

                    return JsonResponse({"ERR": "Id Does Not Exist"}, safe=False)

            else:

                return JsonResponse({"ERR": "Empty Json File, put these '{' '}' "}, safe=False)

        except Exception as error:
            print("Exception", error)
            return JsonResponse({"ERR": "Error occurred while fetching the patient details"}, safe=False)


@method_decorator(csrf_exempt, name="dispatch")
class doctor_api(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):

        try:

            if len(request.body) > 0:

                check_bookings(datetime.date.today())
                python_data = JSONParser().parse(BytesIO(request.body))

                if "doctor_id" in python_data.keys():

                    try:

                        doc = Doctor.objects.get(
                            id=python_data.pop("doctor_id"))
                        ser = DoctorSerializer(doc)
                        return JsonResponse(ser.data, safe=False)

                    except:

                        return JsonResponse({"ERR": "ID Does Not Exist"}, safe=False)

                else:

                    doc = Doctor.objects.all()
                    ser = DoctorSerializer(doc, many=True)
                    return JsonResponse(ser.data, safe=False)

            else:

                return JsonResponse({"ERR": "Empty Json File, put these '{' '}' "}, safe=False)

        except Exception as error:
            print("Exception", error)
            return JsonResponse({"ERR": "Error occurred while fetching the doctor details"}, safe=False)


@method_decorator(csrf_exempt, name="dispatch")
class history_api(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):

        try:

            if len(request.body) > 0:

                try:

                    print("User", request.user.id)
                    his = History.objects.filter(patient_id=request.user.id)
                    ser = HistorySerializer(his, many=True)
                    return JsonResponse(ser.data, safe=False)

                except Exception as error:

                    print("[SERVER-ERROR]", error)
                    return JsonResponse({"ERR": "User Does Not Exist!"}, safe=False)

            else:

                return JsonResponse({"ERR": "Empty Json File, put these '{' '}' "}, safe=False)

        except Exception as error:
            print("Exception", error)
            return JsonResponse({"ERR": "Error occurred while fetching the patient's history"}, safe=False)


@method_decorator(csrf_exempt, name="dispatch")
class details_api(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):

        try:

            contact = get_contact_or_none(Contact.objects, request.user.id)

            if contact == None:
                print("[SERVER-ERROR] Id Does not Exist")
                return JsonResponse({"ERR": "ID Does Not Exist"}, safe=False)

            details = Details.objects.filter(contact_id=contact.id)
            data = models_to_dict(details)
            print("json-data:\n", data)
            return JsonResponse(data, safe=False)

        except Exception as error:
            print("Exception", error)
            return JsonResponse({"ERR": "Error occurred while fetching the details"}, safe=False)


@method_decorator(csrf_exempt, name="dispatch")
class reports_api(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):

        try:

            contact = get_contact_or_none(Contact.objects, request.user.id)

            if contact == None:
                msg = "Id Does not Exist"
                print("[SERVER-ERROR]", msg)
                return JsonResponse({"ERR": msg}, safe=False)

            reports = Reports.objects.filter(contact_id=contact.id)
            data = models_to_dict(reports, report=True)
            print("json-data:\n", data)
            return JsonResponse(data, safe=False)

        except Exception as error:
            print("Exception", error)
            return JsonResponse({"ERR": "Error occurred while fetching the patient reports"}, safe=False)


@method_decorator(csrf_exempt, name="dispatch")
class booking_api(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):

        try:

            contact = get_contact_or_none(Contact.objects, request.user.id)

            if contact == None:
                msg = "User Does Not Exist!"
                print("[SERVER-MSG]", msg)
                return JsonResponse({"ERR": msg}, safe=False)

            bookings = Booking.objects.filter(contact_id=contact.id)
            data = models_to_dict(bookings)
            print("json-data:\n", data)
            return JsonResponse(data, safe=False)

        except Exception as error:
            print("Exception", error)
            return JsonResponse({"ERR": "Error occurred while fetching the patient bookings"}, safe=False)

    def post(self, request):

        data = ""
        try:

            python_data = JSONParser().parse(BytesIO(request.body))
            print("Data Received", python_data)

            try:

                date = python_data.pop("date")
                slot = python_data.pop("slot")
                doc_id = python_data.pop("doc_id")

            except Exception as error:

                print("[SERVER-ERROR]", error)
                return JsonResponse({"ERR": " Either date or slot or doctor_id is not given!"}, safe=False)

            result = has_duplicate(date, slot, doc_id, request.user.id)
            print(request.user.id)
            if result != None:

                if result == "Doc":
                    msg = " This Slot Is Not Available!"
                else:
                    msg = " You Already Have An Appointment In This Slot And Date!"
            else:

                booking = Booking()
                booking.make_booking(Contact.objects.get(
                    user_id=request.user.id), Doctor.objects.get(id=doc_id), to_date(date), slot)
                booking.save()
                data = booking.get_dict()
                msg = " Slot Booked!"

            print("json-data:\n", msg)
            return JsonResponse({"MSG": msg, "data": data}, safe=False)

        except Exception as error:
            print("Exception", error)
            return JsonResponse({"ERR": "Error occurred while booking the slots"}, safe=False)

    def delete(self, request):

        try:

            python_data = JSONParser().parse(BytesIO(request.body))
            print("Data Received", python_data)

            if "booking-ids" in python_data.keys():

                res = ""
                for bookings in python_data["booking-ids"]:
                    res += cancel_booking(bookings)+" "

                if "oops" not in res:

                    if len(python_data["booking-ids"]) == 1:
                        msg = " Appointment Canceled"
                    else:
                        msg = " Appointments Canceled"

                else:
                    msg = "[SERVER-ERROR] booking id does not exist!"

                print("json-data:\n", msg)
                return JsonResponse({"MSG": msg}, safe=False)

            else:
                msg = "booking-ids are required but not provided"
                print("Error -", msg)
                return JsonResponse({"ERR": msg}, safe=False)

        except Exception as error:
            print("Exception", error)
            return JsonResponse({"ERR": "Error occurred while deleting the bookings"}, safe=False)
