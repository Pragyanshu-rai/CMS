from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from random import choices
from string import ascii_letters, digits
import datetime
from cms.viewsUtil import modifySession
from cms.models import *
from cms.forms import updateContact
from cmsUtils.mail import format_email_body, sendEmail
from cmsUtils.emailUtils import email_body_html, email_body_text, email_subjects
from cmsUtils.viewUtils import get_user_ip, validate_email_and_get_user


user_session: dict = dict()
OTP: dict = dict()
otp_request: str = "otpRequest"
password_change: str = "passwordChange"
invalid_login: str = "invalidLogin"

user_session['change'] = False

user_session['slots'] = [
    '09:00 AM',
    '09:30 AM',
    '10:00 AM',
    '10:30 AM',
    '11:00 AM',
    '11:30 AM',
    '12:00 PM',
    '01:00 PM',
    '01:30 PM',
    '02:00 PM',
    '02:30 PM',
    '03:00 PM',
    '03:30 PM',
    '04:00 PM',
    '04:30 PM',
    '05:00 PM',
    '05:30 PM',
    '06:00 PM',
]


def error(request, path):
    return render(request, 'cms/forbid.html')


def home(request):

    global user_session

    print("home")

    if request.user.is_authenticated == True:

        print(request.user)

        modifySession(request)

        user_session['fresh-login'] = True

        # return render(request, 'cms/profile.html', user_session)
        return redirect('profile')

    return render(request, 'cms/index.html', user_session)


def aboutMe(request):

    global user_session

    return render(request, 'cms/about.html', user_session)


def profile(request):

    global user_session

    modifySession(request)

    if request.user.is_authenticated == True:

        user_session['contact'] = Contact.objects.get(user=request.user)
        user_session['age'] = age(to_date(str(user_session['contact'].dob)))

        if request.method == "POST":

            check = updateContact(
                request.POST, request.FILES, instance=user_session['contact'])
            if check.is_valid():

                check.save()
                user_session['warning'] = False
                messages.info(request, "  User Profile Updated Successfully")

            else:

                user_session['warning'] = True
                messages.info(request, "  User Profile Update Failed")

        else:

            fresh = user_session.get("fresh-login", False)

            if fresh:

                messages.info(request, "  logged in")
                user_session['warning'] = False
                user_session['fresh-login'] = False

            else:
                user_session['show'] = False

        form = updateContact(instance=user_session['contact'])
        user_session['form'] = form

        return render(request, 'cms/profile.html', user_session)

    return redirect('login')


def pastconsult(request):

    global user_session

    modifySession(request)

    if request.user.is_authenticated == True:

        contact = Contact.objects.get(user=request.user)

        user_session['records'] = Details.objects.filter(contact=contact)

        return render(request, 'cms/pastconsult.html', user_session)

    return render(request, 'cms/forbid.html', user_session)


def dashboard(request):

    global user_session

    modifySession(request)

    if request.user.is_authenticated == True:

        contact = Contact.objects.get(user=request.user)

        return render(request, 'cms/dashboard.html', user_session)

    return render(request, 'cms/forbid.html', user_session)


def pastbooking(request):

    global user_session

    modifySession(request)

    if request.user.is_authenticated == True:

        check_bookings(datetime.date.today())

        user_session['bookings'] = History.objects.filter(
            patient_id=request.user.id)

        user_session['page'] = "Past Appointments"

        user_session['line'] = "All your past appointments"

        return render(request, 'cms/active_or_pastbooking.html', user_session)

    return render(request, 'cms/forbid.html', user_session)


def activebooking(request):

    global user_session

    modifySession(request)

    if request.user.is_authenticated == True:

        check_bookings(datetime.date.today())

        contact = Contact.objects.get(user_id=request.user.id)

        user_session['bookings'] = Booking.objects.filter(contact=contact)
        print(user_session)

        user_session['page'] = "Active Appointments"

        user_session['line'] = "All your pending or active appointments"

        if request.method == "POST":

            checks = request.POST.getlist('book_no')

            if len(checks) > 0:
                for check in checks:
                    res = cancel_booking(check)
                if res != "oops":
                    user_session['warning'] = False
                    if len(checks) == 1:
                        messages.info(request, " Appointment Canceled")
                    else:
                        messages.info(request, " Appointments Canceled")

            return redirect('dashboard')

        return render(request, 'cms/active_or_pastbooking.html', user_session)

    return render(request, 'cms/forbid.html', user_session)


def report(request):

    global user_session

    modifySession(request)

    if request.user.is_authenticated == True:

        contact = Contact.objects.get(user=request.user)

        user_session['reports'] = Reports.objects.filter(contact=contact)

        return render(request, 'cms/reports.html', user_session)

    return render(request, 'cms/forbid.html', user_session)


def doctors(request):

    global user_session

    modifySession(request)

    if request.user.is_authenticated == True:

        check_bookings(datetime.date.today())

        doctor = Doctor.objects.all()

        user_session['doctors'] = doctor

        if request.method == 'POST':

            doctor = request.POST['booking']

            user_session['doctor'] = Doctor.objects.get(id=doctor)

            return redirect('booking')

        return render(request, 'cms/doctors.html', user_session)

    return render(request, 'cms/forbid.html', user_session)


def booking(request):

    modifySession(request)

    if request.user.is_authenticated == True:

        doc = user_session.get('doctor', None)

        if doc == None:

            return redirect('doctors')

        if request.method == 'POST':

            date = request.POST['date']
            slot = request.POST['slot']
            print("date", date, ", Slot-", slot)

            result = has_duplicate(
                date, slot, user_session['doctor'].id, request.user.id)

            if result != None:

                if result == "Doc":
                    messages.info(request, "  This Slot Is Not Available!")
                else:
                    messages.info(
                        request, "  You Already Have An Appointment In This Slot And Date!")

                user_session['warning'] = True

                return render(request, 'cms/booking.html', user_session)

            user_session['warning'] = False

            messages.info(request, "  Slot Booked")

            booking = Booking()

            contact = Contact.objects.get(user_id=request.user.id)

            doctor = Doctor.objects.get(id=user_session['doctor'].id)

            booking.make_booking(contact, doctor, to_date(date), slot)

            booking.save()

            print(booking)

            print(user_session)

            # render(request, 'booking.html', user_session)
            return redirect('doctors')

        return render(request, 'cms/booking.html', user_session)

    return render(request, 'cms/forbid.html', user_session)


def login(request):

    global user_session

    if request.method == 'POST':

        name = request.POST['name']

        email = request.POST['email']

        password = request.POST['password']

        print(email, password)

        user = auth.authenticate(username=name+"_"+email, password=password)
        user = auth.authenticate(
            username=email, password=password) if user is None else user

        if user == None:

            messages.info(request, '  Invalid Login Details')

            user_session['warning'] = True

            return redirect('login')

        else:

            auth.login(request, user)

            request.session["user"] = user.id

            user_session["show"] = True

            user_session['warning'] = False

            print(user_session, messages.get_messages(request=request))

            return redirect('home')

    else:

        return render(request, 'cms/login.html', user_session)


def register(request):

    global user_session

    if request.method == 'POST':

        name = request.POST['name']

        email = request.POST['email']

        gender = request.POST['gender']

        dob = request.POST['dob']

        phone = request.POST['contact']

        address = request.POST['address']

        password = request.POST['password']

        confirm = request.POST['confirm']

        print(dob, gender)

        dob = to_date(dob)

        print(age(dob), gender)

        if password != confirm:

            messages.info(request, '  Password does not match')

            user_session['warning'] = True

            return redirect('register')

        if User.objects.filter(email=email).exists():

            messages.info(request, '  User Exists')

            user_session['warning'] = True

            return redirect('register')

        user = User.objects.create_user(
            username=name+"_"+email, password=password, email=email, first_name=name)
        # user.save()
        contact = Contact()
        contact.make_contact(user, gender, dob, address, phone)
        contact.save()
        messages.info(request, '  User Registered')

        user_session['warning'] = False

        return redirect("login")

    else:
        return render(request, 'cms/register.html', user_session)


def otp(request, uid=-1):

    global user_session, OTP

    print("uid =", uid)

    if request.method == 'POST':

        modifySession(request)

        print(OTP)

        if OTP[uid] == request.POST['otp']:

            messages.info(request, '  Correct OTP')

            user_session['warning'] = False

            user_session['change'] = True

            return redirect('change', uid=uid)
        else:

            messages.info(request, '  Invalid - OTP')

            user_session['warning'] = True

            return render(request, 'cms/otp.html', user_session)

    return render(request, 'cms/otp.html', user_session)


def forgot(request):

    global user_session, OTP, email_body_text, email_body_html, email_subjects
    current_date_time: str = str(
        datetime.datetime.now()).split(".")[0]

    if request.method == "POST":

        email = request.POST['email']
        print("in forgot")

        try:
            otp_otp = "".join(choices(digits + ascii_letters + digits, k=6))
            print(request.user, otp_otp)
            request.user = validate_email_and_get_user(request, email)
            user_name = request.user.first_name
            user_ip = get_user_ip(request)
            print(user_name, user_ip)
            text_body = format_email_body(
                email_body_text[otp_request], user_name, user_ip, current_date_time, otp_otp)
            html_body = format_email_body(
                email_body_html[otp_request], user_name, user_ip, current_date_time, otp_otp)
            sendEmail(subject=email_subjects[otp_request],
                      body=text_body, to=email, alternative=html_body)
            print("Email sent - ", request.user.email)
            messages.info(
                request, '  An OTP is sent to your registered email id. ')
            uid = request.user.id
            OTP[uid] = otp_otp

        except Exception as error:
            print("[SERVER ERROR] OTP ERROR - ", error)
            messages.info(request, '  User not found!')
            user_session['warning'] = True
            return render(request, 'cms/forgot.html', user_session)

        print(otp_otp)

        user_session['warning'] = False

        return redirect('otp', uid=uid)

    return render(request, 'cms/forgot.html', user_session)


def change(request, uid=-1):

    global user_session, email_subjects, email_body_html, email_body_text
    current_date_time: str = str(
        datetime.datetime.now()).split(".")[0]

    if user_session['change'] == True:

        user_session['change'] = False
        user = User.objects.get(id=uid)
        user_session['name'] = user.first_name
        return render(request, 'cms/change.html', user_session)

    if request.method == "POST":

        passw = request.POST['password']
        confirm = request.POST['confirm']

        if passw != confirm:

            messages.info(request, '  Password does not match')
            user_session['warning'] = True
            return render(request, 'cms/change.html', user_session)

        user = User.objects.get(pk=uid)
        user_email = user.email
        user_name = user.first_name
        user_ip = get_user_ip(request)
        user.set_password(passw)
        user.save()
        messages.info(request, '  Password is changed')
        user_session['warning'] = False
        text_body = format_email_body(
            email_body_text[password_change], user_name, user_ip, current_date_time)
        html_body = format_email_body(
            email_body_html[password_change], user_name, user_ip, current_date_time)
        sendEmail(subject=email_subjects[password_change],
                  body=text_body, to=user_email, alternative=html_body)
        return redirect('login')

    return render(request, 'cms/forbid.html', user_session)


def logout(request):

    global user_session
    auth.logout(request)
    messages.info(request, '  User Logged Out ')
    user_session['warning'] = False
    return redirect('home')
