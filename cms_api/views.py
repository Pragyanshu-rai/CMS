from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from io import BytesIO
from .apiUtils import models_to_dict, get_contact_or_none, validate_signup
from cms.models import Contact, Details, Doctor, History, Booking, Reports
from cms.serializers import ContactSerializer, HistorySerializer, UserSerializer, DoctorSerializer
from cms.mail import send_email
from random import randint

# Create your views here.

instructions = "api-endpoint http://127.0.0.1:8000/cms-api-signup for user registeration (username, password, gender(m/f), roll, branch, section, year) "

api_list = [
    "http://127.0.0.1:8000/cms-api/patient/",
    "http://127.0.0.1:8000/cms-api/doctor/",
    "http://127.0.0.1:8000/cms-api/history/",
    "http://127.0.0.1:8000/cms-api/details/",
    "http://127.0.0.1:8000/cms-api/reports/",
    "http://127.0.0.1:8000/cms-api/booking/",
    "http://127.0.0.1:8000/cms-api/history/",
    "http://127.0.0.1:8000/cms-api/api-get-otp/",
    "http://127.0.0.1:8000/cms-api/help/",
]


def instruction(request):
    return JsonResponse({"MSG": instructions, "API-List": api_list}, safe=False)




@csrf_exempt
def request_otp(request):

    try:

        if len(request.body) > 0:

            email = JSONParser().parse(BytesIO(request.body)).pop("email")
            print(email)
            otp = str(randint(100000, 999999))
            send_email("OTP", otp, email)
            return JsonResponse({"MSG":"OTP Sent To The Registered Email", "OTP":otp}, safe=False)

        else:

            return JsonResponse({"ERR":"'email' is required but not provided!"}, safe=False)
    
    except Exception as error:

        print("[SERVER-ERROR]", error)
        return JsonResponse({"ERR":error}, safe=False)


@method_decorator(csrf_exempt, name="dispatch")
class patient_api(APIView):

    def get(self, request):

        try:
            # print(len(request.body))
            if len(request.body) > 0:

                python_data = JSONParser().parse(BytesIO(request.body))

                if "user_id" in python_data.keys():

                    try:
                        
                        ct = Contact.objects.get(user_id=python_data.pop("user_id"))
                        ser = ContactSerializer(ct)
                        return JsonResponse(ser.data, safe=False)
                    
                    except:
                        
                        return JsonResponse({"ERR": "Id Does Not Exist"}, safe=False)

                else:

                    ct = Contact.objects.all()
                    ser = ContactSerializer(ct, many=True)
                    return JsonResponse(ser.data, safe=False)

            else:

                return JsonResponse({"ERR":"Empty Json File, put these '{' '}' "}, safe=False)

        except Exception as error:

            print("Exception", error)
            return JsonResponse({"ERR": error}, safe=False)
    
    def post(self, request):

        try:

            if len(request.body) > 0:

                python_data = JSONParser().parse(BytesIO(request.body))
                print(python_data)
                valid = validate_signup(python_data)
                print(valid)
                
                if valid != None:
                    
                    return JsonResponse({"ERR":valid}, safe=False)
                
                print(python_data)
                ser = ContactSerializer(data=python_data)
                
                if ser.is_valid():
                    ser.save()
                    print("Data Saved")
                    return JsonResponse({"MSG":"DATA SAVED", "DATA":ser.data}, safe=False)
                
                return JsonResponse({"ERR":ser.errors}, safe=False)


            else:

                return JsonResponse({"ERR":"Empty Json File, put these '{' '}' "}, safe=False)

        except Exception as error:

            print("Exception", error)
            return JsonResponse({"ERR": error}, safe=False)


@method_decorator(csrf_exempt, name="dispatch")
class doctor_api(APIView):

    def get(self, request):

        try:

            if len(request.body) > 0:

                python_data = JSONParser().parse(BytesIO(request.body))

                if "doctor_id" in python_data.keys():

                    try:
                    
                        doc = Doctor.objects.get(id=python_data.pop("doctor_id"))
                        ser = DoctorSerializer(doc)
                        return JsonResponse(ser.data, safe=False)
                    
                    except:

                        return JsonResponse({"ERR":"ID Does Not Exist"}, safe=False)

                else:

                    doc = Doctor.objects.all()
                    ser = DoctorSerializer(doc, many=True)
                    return JsonResponse(ser.data, safe=False)

            else:

                return JsonResponse({"ERR":"Empty Json File, put these '{' '}' "}, safe=False)

        except Exception as error:

            print("Exception", error)
            return JsonResponse({"ERR": error}, safe=False)


@method_decorator(csrf_exempt, name="dispatch")
class history_api(APIView):

    def get(self, request):

        try:

            if len(request.body) > 0:

                python_data = JSONParser().parse(BytesIO(request.body))

                if "user_id" in python_data.keys():

                    try:
                    
                        his = History.objects.get(patient_id=python_data.pop("user_id"))
                        ser = HistorySerializer(his)
                        return JsonResponse(ser.data, safe=False)
                    
                    except Exception as error:
                        
                        print("[SERVER-ERROR]", error)
                        return JsonResponse({"ERR":"ID Does Not Exist"}, safe=False)

                else:

                    his = History.objects.all()
                    ser = HistorySerializer(his, many=True)
                    return JsonResponse(ser.data, safe=False)

            else:

                return JsonResponse({"ERR":"Empty Json File, put these '{' '}' "}, safe=False)

        except Exception as error:

            print("Exception", error)
            return JsonResponse({"ERR": error}, safe=False)


@method_decorator(csrf_exempt, name="dispatch")
class details_api(APIView):

    def get(self, request):

        try:

            python_data = JSONParser().parse(BytesIO(request.body))
            print("Data Recieved", python_data)

            if "user_id" in python_data.keys():

                contact = get_contact_or_none(Contact.objects, python_data.pop('user_id'))
                
                if contact == None:
                    
                    print("[SERVER-ERROR] Id Does not Exist")
                    return JsonResponse({"ERR":"ID Does Not Exist"}, safe=False)
                
                details = Details.objects.filter(contact_id=contact.id)
                data = models_to_dict(details)
                print("json-data:\n", data)
                return JsonResponse(data, safe=False)

            else:

                print("Error - user_id is required but not provided")
                return JsonResponse({"ERR": "user_id is required but not provided"}, safe=False)

        except Exception as error:

            print("Exception", error)
            return JsonResponse({"ERR": error}, safe=False)


@method_decorator(csrf_exempt, name="dispatch")
class reports_api(APIView):

    def get(self, request):

        try:

            python_data = JSONParser().parse(BytesIO(request.body))
            print("Data Recieved", python_data)

            if "user_id" in python_data.keys():

                contact = get_contact_or_none(Contact.objects, python_data.pop('user_id'))
                
                if contact == None:
                    
                    print("[SERVER-ERROR] Id Does not Exist")
                    return JsonResponse({"ERR":"ID Does Not Exist"}, safe=False)
                
                reports = Reports.objects.filter(contact_id=contact.id)
                data = models_to_dict(reports)
                print("json-data:\n", data)
                return JsonResponse(data, safe=False)

            else:

                print("Error - user_id is required but not provided")
                return JsonResponse({"ERR": "user_id is required but not provided"}, safe=False)

        except Exception as error:

            print("Exception", error)
            return JsonResponse({"ERR": error}, safe=False)


@method_decorator(csrf_exempt, name="dispatch")
class booking_api(APIView):

    def get(self, request):

        try:

            python_data = JSONParser().parse(BytesIO(request.body))
            print("Data Recieved", python_data)

            if "user_id" in python_data.keys():

                contact = get_contact_or_none(Contact.objects, python_data.pop('user_id'))
                
                if contact == None:
                    
                    print("[SERVER-ERROR] Id Does not Exist")
                    return JsonResponse({"ERR":"ID Does Not Exist"}, safe=False)
                
                bookings = Booking.objects.filter(contact_id=contact.id)
                data = models_to_dict(bookings)
                print("json-data:\n", data)
                return JsonResponse(data, safe=False)

            else:

                print("Error - user_id is required but not provided")
                return JsonResponse({"ERR": "user_id is required but not provided"}, safe=False)

        except Exception as error:

            print("Exception", error)
            return JsonResponse({"ERR": error}, safe=False)
