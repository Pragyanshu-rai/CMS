# email utility variables

email_subject_otp: str = "Changing your CMS password"
email_subject_invalid_login: str = "ACTION REQUIRED: Suspicious Activity"
email_subject_password_changed: str = "Password Updated"

email_body_otp: str = """
Dear {},

Thank you for being associated with Clinic Management System (CMS).

You have requested for password change originating from IP address {} for which the One Time Password (OTP) - "{}" has been generated at {}.

In case you have not requested for password reset you can notify us at - noreply.services.2001@gmail.com, so we can make
sure no one else is trying to access your account.

Disclaimer!

We recommend you do not share this OTP with anyone to prevent fraudulent transactions.

Sincerely,
Team Clinic Management System (CMS)
    """


email_body_invalid_login: str = """
Dear {},

Thank you for being associated with Clinic Management System (CMS).

Suspicious Login Activity!

We detected suspicious password recovery activity from the IP {} at {}.

If this was you, then you can safely ignore this email and head to https://cms-wa.herokuapp.com/.

If not you? then notify us at noreply.services.2001@gmail.com so we can make sure no one else is trying to 
access your account.

In case you have not requested for password change you can notify us at - noreply.services.2001@gmail.com.

We recommend that you update your password to a strong password here https://cms-wa.herokuapp.com/login/.

Sincerely,
Team Clinic Management System (CMS)
    """

email_body_password_changed: str = """
Dear {},

Thank you for being associated with Clinic Management System (CMS).

Your Password Has Been Changed.

Your request for password reset originating from IP address {} at {} has been successful.

In case you have not requested for password reset you can notify us at - noreply.services.2001@gmail.com, so we can make
sure no one else is trying to access your account.

Sincerely,
Team Clinic Management System (CMS)
    """

email_body_otp_html: str = """\
<!DOCTYPE html>
<html lang="en">
<!-- 
    This template belongs to Pragyanshu Rai.
-->

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OTP EMAIL TEMPLATE</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
        integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <style>
        /* Importing the ubuntu font */
        @import url('https://fonts.googleapis.com/css2?family=Ubuntu&display=swap');

        *:focus {
            outline: none;
        }

        a {
            text-decoration: none;
        }

        html {
            /*for smooth scrolling*/
            scroll-behavior: smooth;
        }

        body {
            background-color: lightblue;
            font-family: 'Ubuntu', sans-serif;
            font-weight: 570;
            font-size: larger;
        }

        .main-body {
            max-width: 60%;
            min-width: 60%;
            max-height: 90%;
            min-height: 90%;
            margin-left: 20%;
            margin-top: 5%;
            background-color: aliceblue;
        }

        footer {
            max-width: 60%;
            min-width: 60%;
            margin-left: 20%;
            max-height: 8vh;
            min-height: 8vh;
            font-weight: 400;
            font-size: large;
            text-align: center;
        }

        .important {
            font-size: large;
            font-weight: bold;
            color: dodgerblue;
        }

        .image {
            border: none;
            border-radius: 2%;
            max-height: 30vh;
        }

        .banner {
            margin-top: 1vh;
            max-height: 100%;
        }

        .banner_holder {
            text-align: center;
            background-color: dodgerblue;
            max-height: 30%;
        }

        .division {
            max-width: 100%;
            min-width: 100%;
            min-height: 0.5vh;
            max-height: 0.5vh;
            background-color: lightblue;
        }

        .message_holder {
            max-width: 90%;
            min-width: 90%;
            min-height: 70%;
            max-height: 70%;
            margin-left: 5%;
            margin-top: 3%;
            margin-bottom: 3%;
            /* background-color: aqua; */
        }

        .message {
            font-size: x-large;
            line-height: 3vh;
        }

        .bold {
            font-weight: bold;
        }

        .pulsate {
            animation: pulse 2s ease-in-out infinite;
        }

        @keyframes pulse {
            0% {
                transform: scale(0.97);
            }

            70% {
                transform: scale(1.0);
            }

            100% {
                transform: scale(0.97);
            }
        }
    </style>
</head>

<body class="container-fluid">
    <main class="row main-body">
        <div class="col-md-12 banner_holder">
            <img src="https://raw.githubusercontent.com/Pragyanshu-rai/CMS/dev/static/cms/img/CMS_dodgerblue.png" alt="CMS LOGO" class="banner">
        </div>
        <div class="col-md-12 division"></div>
        <div class="col-md-12 message_holder message">
            Dear {},
            <div class="p-3"></div>
            Thank you for being associated with <span class="bold">Clinic Management System (CMS)</span>.
            <div class="p-2"></div>
            The request for password change originated from IP address <mark class="bold">{}</mark> &nbsp;
            for which the One Time Password (OTP) has been generated at <span class="bold">{}</span>.
            <div class="p-4"></div>
            <div class="container-fluid">
                <div class="row">
                    <div class="col-md-12 important">
                        <img src="https://raw.githubusercontent.com/Pragyanshu-rai/CMS/d8bc6f4004c2f027b124bf07c36bf0e7bc4e16d2/static/cms/img/otp_alert.svg" alt="OTP Alert Image" class="image pulsate">
                        <span class="display-3 bold">
                            <span class="code">
                                {}
                            </span>
                        </span>
                    </div>
                </div>
            </div>
            <div class="p-4"></div>
            <div class="bold">
                Not you? then notify us at &nbsp;
                <a href="mailto:noreply.services.2001@gmail.com" class="btn btn-primary">CMS Support</a> &nbsp;
                <span class="text-muted">
                    so we can make sure no one else is trying to access your account.
                </span>
            </div>
            <div class="space-sm">
                <br>
            </div>
            Disclaimer!
            <br>
            We recommend you do not share this OTP with anyone to prevent fraudulent transactions.
            <div class="p-2"></div>
            Sincerely,
            <br>
            Team <span class="bold">Clinic Management System (CMS)</span>
        </div>
    </main>
    <div class="p-2"></div>
    <footer class="row">
        <div class="col-md-8"></div>
        <p class="col-md-4">
            &copy; 2021 Clinic Management Service, Ltd.
            <br>
            &commat;Pragyanshu Rai
        </p>
    </footer>
</body>

</html>
"""

email_body_invalid_login_html: str = """\
<!DOCTYPE html>
<html lang="en">
<!-- 
    This template belongs to Pragyanshu Rai.
-->

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>INVALID LOGIN EMAIL TEMPLATE</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
        integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <style>
        /* Importing the ubuntu font */
        @import url('https://fonts.googleapis.com/css2?family=Ubuntu&display=swap');

        *:focus {
            outline: none;
        }

        a {
            text-decoration: none;
        }

        html {
            /*for smooth scrolling*/
            scroll-behavior: smooth;
        }

        body {
            background-color: lightblue;
            font-family: 'Ubuntu', sans-serif;
            font-weight: 570;
            font-size: larger;
        }

        .main-body {
            max-width: 60%;
            min-width: 60%;
            max-height: 90%;
            min-height: 90%;
            margin-left: 20%;
            margin-top: 5%;
            background-color: aliceblue;
        }

        footer {
            max-width: 60%;
            min-width: 60%;
            margin-left: 20%;
            max-height: 8vh;
            min-height: 8vh;
            font-weight: 400;
            font-size: large;
            text-align: center;
        }

        .important {
            font-size: large;
            font-weight: bold;
            color: dodgerblue;
        }

        .image {
            border: none;
            border-radius: 2%;
            max-height: 30vh;
        }

        .banner {
            margin-top: 1vh;
            max-height: 100%;
        }

        .banner_holder {
            text-align: center;
            background-color: dodgerblue;
            max-height: 30%;
        }

        .division {
            max-width: 100%;
            min-width: 100%;
            min-height: 0.5vh;
            max-height: 0.5vh;
            background-color: lightblue;
        }

        .message_holder {
            max-width: 90%;
            min-width: 90%;
            min-height: 70%;
            max-height: 70%;
            margin-left: 5%;
            margin-top: 3%;
            margin-bottom: 3%;
        }

        .message {
            font-size: x-large;
            line-height: 3vh;
        }

        .bold {
            font-weight: bold;
        }

        .pulsate {
            animation: pulse 2s ease-in-out infinite;
        }

        @keyframes pulse {
            0% {
                transform: scale(0.97);
            }

            70% {
                transform: scale(1.0);
            }

            100% {
                transform: scale(0.97);
            }
        }
    </style>
</head>

<body class="container-fluid">
    <main class="row main-body">
        <div class="col-md-12 banner_holder">
            <img src="https://raw.githubusercontent.com/Pragyanshu-rai/CMS/dev/static/cms/img/CMS_dodgerblue.png" alt="CMS LOGO" class="banner">
        </div>
        <div class="col-md-12 division"></div>
        <div class="col-md-12 message_holder message">
            <div class="h1 bold text-center">
                Suspicious Login Activity!
            </div>
            <div class="p-2"></div>
            Dear {},
            <div class="p-3"></div>
            We detected suspicious password recovery activity from the IP <mark class="bold">{}</mark> at <span
                class="bold">{}</span>.
            <div class="p-4"></div>
            <div class="container-fluid">
                <div class="row">
                    <div class="col-md-6 important">
                        <img src="https://raw.githubusercontent.com/Pragyanshu-rai/CMS/d8bc6f4004c2f027b124bf07c36bf0e7bc4e16d2/static/cms/img/password_reset_warning.svg" alt="OTP Alert Image" class="image pulsate">
                    </div>
                    <div class="col-md-6 text-center">
                        <span class="h4 bold">
                            <span class="code">
                                If this was you, then you can safely ignore this email and head to
                                <a href="https://cms-wa.herokuapp.com/" class="btn btn-primary">CMS Website</a>.
                            </span>
                            <br>
                            <br>
                            <span class="code">
                                If not you? then notify us at &nbsp;
                                <a href="mailto:noreply.services.2001@gmail.com" class="btn btn-primary">CMS Support</a>
                                &nbsp;
                                <span class="text-muted">
                                    so we can make sure no one else is trying to access your account.
                                </span>
                            </span>
                            <br>
                            <br>
                            <span class="code">
                                We recommend that you update your password to a strong password here
                                <a href="https://cms-wa.herokuapp.com/login/" class="btn btn-danger">Update Password</a>
                                &nbsp;
                            </span>
                        </span>
                    </div>
                </div>
            </div>
            <div class="p-4"></div>
            Thank you for being associated with <span class="bold">Clinic Management System (CMS)</span>.
            <div class="p-2"></div>
            Sincerely,
            <br>
            Team <span class="bold">Clinic Management System (CMS)</span>
        </div>
    </main>
    <div class="p-2"></div>
    <footer class="row">
        <div class="col-md-8"></div>
        <p class="col-md-4">
            &copy; 2021 Clinic Management Service, Ltd.
            <br>
            &commat;Pragyanshu Rai
        </p>
    </footer>
</body>

</html>
"""

email_body_password_changed_html: str = """\
<!DOCTYPE html>
<html lang="en">
<!-- 
    This template belongs to Pragyanshu Rai.
-->

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CHANGED PASSWORD EMAIL TEMPLATE</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
        integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <style>
        /* Importing the ubuntu font */
        @import url('https://fonts.googleapis.com/css2?family=Ubuntu&display=swap');

        *:focus {
            outline: none;
        }

        a {
            text-decoration: none;
        }

        html {
            /*for smooth scrolling*/
            scroll-behavior: smooth;
        }

        body {
            background-color: lightblue;
            font-family: 'Ubuntu', sans-serif;
            font-weight: 570;
            font-size: larger;
        }

        .main-body {
            max-width: 60%;
            min-width: 60%;
            max-height: 90%;
            min-height: 90%;
            margin-left: 20%;
            margin-top: 5%;
            background-color: aliceblue;
        }

        footer {
            max-width: 60%;
            min-width: 60%;
            margin-left: 20%;
            max-height: 8vh;
            min-height: 8vh;
            font-weight: 400;
            font-size: large;
            text-align: center;
        }

        .important {
            font-size: large;
            font-weight: bold;
            color: dodgerblue;
        }

        .image {
            border: none;
            border-radius: 2%;
            max-height: 30vh;
        }

        .banner {
            margin-top: 1vh;
            max-height: 100%;
        }

        .banner_holder {
            text-align: center;
            background-color: dodgerblue;
            max-height: 30%;
        }

        .division {
            max-width: 100%;
            min-width: 100%;
            min-height: 0.5vh;
            max-height: 0.5vh;
            background-color: lightblue;
        }

        .message_holder {
            max-width: 90%;
            min-width: 90%;
            min-height: 70%;
            max-height: 70%;
            margin-left: 5%;
            margin-top: 3%;
            margin-bottom: 3%;
        }

        .message {
            font-size: x-large;
            line-height: 3vh;
        }

        .bold {
            font-weight: bold;
        }

        .pulsate {
            animation: pulse 2s ease-in-out infinite;
        }

        @keyframes pulse {
            0% {
                transform: scale(0.97);
            }

            70% {
                transform: scale(1.0);
            }

            100% {
                transform: scale(0.97);
            }
        }
    </style>
</head>

<body class="container-fluid">
    <main class="row main-body">
        <div class="col-md-12 banner_holder">
            <img src="https://raw.githubusercontent.com/Pragyanshu-rai/CMS/dev/static/cms/img/CMS_dodgerblue.png" alt="CMS LOGO" class="banner">
        </div>
        <div class="col-md-12 division"></div>
        <div class="col-md-12 message_holder message">
            <div class="h1 bold text-center">
                Your Password Has Been Changed!
            </div>
            <div class="p-2"></div>
            Dear {},
            <div class="p-3"></div>
            Your request for password reset originating from IP address <mark class="bold">{}</mark> at <span
                class="bold">{}</span> has been successful.
            <div class="p-4"></div>
            <div class="container-fluid">
                <div class="row">
                    <div class="col-md-6 important">
                        <img src="https://raw.githubusercontent.com/Pragyanshu-rai/CMS/d8bc6f4004c2f027b124bf07c36bf0e7bc4e16d2/static/cms/img/password_reset_alert.svg" alt="OTP Alert Image" class="image pulsate">
                    </div>
                    <div class="col-md-6 text-center">
                        <span class="h4 bold">
                            <br>
                            <span class="code">
                                If this was you, then you can safely ignore this email and head to
                                <a href="https://cms-wa.herokuapp.com/" class="btn btn-primary">CMS Website</a>.
                            </span>
                            <br>
                            <br>
                            <br>
                            <span class="code">
                                Not you? then notify us at &nbsp;
                                <a href="mailto:noreply.services.2001@gmail.com" class="btn btn-primary">CMS Support</a>
                                &nbsp;
                                <span class="text-muted">
                                    so we can make sure no one else is trying to access your account.
                                </span>
                            </span>
                        </span>
                    </div>
                </div>
            </div>
            <div class="p-4"></div>
            Thank you for being associated with <span class="bold">Clinic Management System (CMS)</span>.
            <div class="p-2"></div>
            Sincerely,
            <br>
            Team <span class="bold">Clinic Management System (CMS)</span>
        </div>
    </main>
    <div class="p-2"></div>
    <footer class="row">
        <div class="col-md-8"></div>
        <p class="col-md-4">
            &copy; 2021 Clinic Management Service, Ltd.
            <br>
            &commat;Pragyanshu Rai
        </p>
    </footer>
</body>

</html>
"""


email_subjects: dict = {
    "otpRequest": email_subject_otp,
    "passwordChange": email_subject_password_changed,
    "invalidLogin": email_subject_invalid_login
}

email_body_text: dict = {
    "otpRequest": email_body_otp,
    "passwordChange": email_body_password_changed,
    "invalidLogin": email_body_invalid_login
}

email_body_html: dict = {
    "otpRequest": email_body_otp_html,
    "passwordChange": email_body_password_changed_html,
    "invalidLogin": email_body_invalid_login_html
}
