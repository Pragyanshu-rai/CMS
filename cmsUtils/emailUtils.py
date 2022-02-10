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
<!DOCTYPE html
    PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>

<head>
    <!-- If you delete this meta tag, the ground will open and swallow you. -->
    <meta name="viewport" content="width=device-width">
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>OTP REQUEST EMAIL</title>
    <style>
        .btn-primary:hover {
            background-color: dodgerblue;
            color: white
        }
    </style>
    <style type="text/css">
        /* -------------------------------------
      		GLOBAL
      ------------------------------------- */
        /* -------------------------------------
      		ELEMENTS
      ------------------------------------- */
        /* -------------------------------------
      		HEADER
      ------------------------------------- */
        /* -------------------------------------
      		BODY
      ------------------------------------- */
        /* -------------------------------------
      		FOOTER
      ------------------------------------- */
        /* -------------------------------------
      		TYPOGRAPHY
      ------------------------------------- */
        /* -------------------------------------
      		SIDEBAR
      ------------------------------------- */
        /* ---------------------------------------------------
      		RESPONSIVENESS
      		Nuke it from orbit. It's the only way to be sure.
      ------------------------------------------------------ */
        /* Let's make sure tables in the content area are 100% wide */
        /* -------------------------------------------
      		PHONE
      		For clients that support media queries.
      		Nothing fancy.
      -------------------------------------------- */
        @media only screen and (max-width: 600px) {
            a[class="btn"] {
                display: block !important;
                margin-bottom: 10px !important;
                background-image: none !important;
                margin-right: 0 !important;
            }

            div[class="column"] {
                width: auto !important;
                float: none !important;
            }

            table.social div[class="column"] {
                width: auto !important;
            }
        }

        /*
              Animations
              simple animations to make the email feel more alive
               */
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

<body bgcolor="#FFFFFF" topmargin="0" leftmargin="0" marginheight="0" marginwidth="0"
    style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;-webkit-font-smoothing:antialiased;-webkit-text-size-adjust:none;height:100%;width:100% !important;'>
    <!-- HEADER -->
    <table class="head-wrap" bgcolor="dodgerblue"
        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;width:100%;'>
        <tr style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
            <td style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
            </td>
            <td class="header container" align=""
                style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;display:block !important;max-width:600px !important;margin:0 auto !important;clear:both !important;'>
                <!-- /content -->
                <div class="content"
                    style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;padding:15px;max-width:600px;margin:0 auto;display:block;'>
                    <table bgcolor="dodgerblue"
                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;width:100%;'>
                        <tr
                            style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                            <td
                                style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                                <h1
                                    style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;font-family:"HelveticaNeue-Light", "Helvetica Neue Light", "Helvetica Neue", Helvetica, Arial, "Lucida Grande", sans-serif;line-height:1.1;margin-bottom:15px;color:#000;font-weight:200;font-size:44px;'>
                                    <big
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;font-size:150%;color:#ffffff;line-height:1.2;text-transform:none;'>
                                        <strong
                                            style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>CMS</strong>
                                    </big>
                                </h1>
                            </td>
                        </tr>
                    </table>
                </div>
                <!-- /content -->
            </td>
            <td style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
            </td>
        </tr>
    </table>
    <!-- /HEADER -->
    <!-- BODY -->
    <table class="body-wrap"
        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;width:100%;'>
        <tr style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
            <td style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
            </td>
            <td class="container" align="" bgcolor="#FFFFFF"
                style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;display:block !important;max-width:600px !important;margin:0 auto !important;clear:both !important;'>
                <!-- content -->
                <div class="content"
                    style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;padding:15px;max-width:600px;margin:0 auto;display:block;'>
                    <table
                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;width:100%;'>
                        <tr
                            style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                            <td
                                style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                                <h1
                                    style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;font-family:"HelveticaNeue-Light", "Helvetica Neue Light", "Helvetica Neue", Helvetica, Arial, "Lucida Grande", sans-serif;line-height:1.1;margin-bottom:15px;color:#000;font-weight:200;font-size:44px;text-align: center;'>
                                    <strong
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                                        OTP REQUEST!
                                    </strong>
                                </h1>
                                <p class="lead"
                                    style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;margin-bottom:10px;font-weight:normal;font-size:14px;line-height:1.6;font-size:17px;'>
                                </p>
                                <h3
                                    style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;font-family:"HelveticaNeue-Light", "Helvetica Neue Light", "Helvetica Neue", Helvetica, Arial, "Lucida Grande", sans-serif;line-height:1.1;margin-bottom:15px;color:#000;font-weight:500;font-size:27px;'>
                                    Dear {},
                                    <br
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                                    <br
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                                    Thank you for being associated with <br
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                                    <span class="bold"
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;font-weight:bold;'>Clinic
                                        Management System
                                        (CMS).</span>
                                    <br
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                                    <br
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                                    The request for password change originated from IP address <mark class="bold"
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;font-weight:bold;'>{}</mark>
                                    for which the One Time Password (OTP) has been generated at <span class="bold"
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;font-weight:bold;'>{}</span>.
                                    <br
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                                </h3>
                                <br
                                    style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                                <!-- A Real Hero (and a real human being) -->
                                <p
                                    style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;margin-bottom:10px;font-weight:normal;font-size:14px;line-height:1.6;'>
                                    <img src="https://raw.githubusercontent.com/Pragyanshu-rai/CMS/d8bc6f4004c2f027b124bf07c36bf0e7bc4e16d2/static/cms/img/otp_alert.svg"
                                        alt="OTP Alert Image" class="pulsate"
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;max-width:100%;animation:pulse 2s ease-in-out infinite;'>
                                </p>
                                <h2 class="bold"
                                    style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;font-family:"HelveticaNeue-Light", "Helvetica Neue Light", "Helvetica Neue", Helvetica, Arial, "Lucida Grande", sans-serif;line-height:1.1;margin-bottom:15px;color:#000;font-weight:200;font-size:37px;font-weight:bold;'>
                                    OTP -
                                    <span class="code bold"
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;font-weight:bold;color:dodgerblue;'>
                                        {}
                                    </span>
                                </h2>
                                <!-- /hero -->
                                <p
                                    style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;margin-bottom:10px;font-weight:normal;font-size:14px;line-height:1.6;'>
                                </p>
                                <h3
                                    style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;font-family:"HelveticaNeue-Light", "Helvetica Neue Light", "Helvetica Neue", Helvetica, Arial, "Lucida Grande", sans-serif;line-height:1.1;margin-bottom:15px;color:#000;font-weight:500;font-size:27px;'>
                                    Not you? then notify us at
                                    <a href="mailto:noreply.services.2001@gmail.com" class="btn btn-primary"
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;color:#2BA6CB;text-decoration:none;color:#FFF;background-color:#666;padding:10px 16px;font-weight:bold;margin-right:10px;text-align:center;cursor:pointer;display:inline-block;background-color:dodgerblue;border-radius:4%;'>CMS
                                        Support</a>,
                                    <span class="text-muted"
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                                        so we can make sure no one else is trying to access your account.
                                    </span>
                                    <br
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                                    <br
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                                    
                                    Sincerely,
                                    <br
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                                    Team <span class="bold"
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;font-weight:bold;'>Clinic
                                        Management System (CMS)</span>
                                </h3>
                            </td>
                        </tr>
                    </table>
                </div>
                <!-- /content -->
            </td>
            <td style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
            </td>
        </tr>
    </table>
    <!-- /BODY -->
    <!-- FOOTER -->
    <table class="footer-wrap dark"
        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;background-color:#dad7d7;width:100%;clear:both !important;'>
        <tr style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
            <td style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
            </td>
            <td class="container"
                style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;display:block !important;max-width:600px !important;margin:0 auto !important;clear:both !important;'>
                <!-- content -->
                <div class="content"
                    style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;padding:15px;max-width:600px;margin:0 auto;display:block;'>
                    <table
                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;width:100%;'>
                        <tr
                            style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                            <td align="center"
                                style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                                <p
                                    style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;margin-bottom:10px;font-weight:normal;font-size:14px;line-height:1.6;'>
                                </p>
                                <div class="code bold"
                                    style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;font-weight:bold;color:dodgerblue;'>
                                    &copy; 2021 Clinic Management Service, Ltd.
                                    <br
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                                    <br
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                                    &commat;Pragyanshu Rai
                                </div>
                            </td>
                        </tr>
                    </table>
                </div>
                <!-- /content -->
            </td>
            <td style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
            </td>
        </tr>
    </table>
    <!-- /FOOTER -->
</body>

</html>
"""

email_body_invalid_login_html: str = """\
<!DOCTYPE html
    PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>

<head>
    <!-- If you delete this meta tag, the ground will open and swallow you. -->
    <meta name="viewport" content="width=device-width">
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>INVALID LOGIN EMAIL</title>
    <style>
        .btn-primary:hover {
            background-color: dodgerblue;
            color: white
        }
    </style>
    <style type="text/css">
        /* -------------------------------------
      		GLOBAL
      ------------------------------------- */
        /* -------------------------------------
      		ELEMENTS
      ------------------------------------- */
        /* -------------------------------------
      		HEADER
      ------------------------------------- */
        /* -------------------------------------
      		BODY
      ------------------------------------- */
        /* -------------------------------------
      		FOOTER
      ------------------------------------- */
        /* -------------------------------------
      		TYPOGRAPHY
      ------------------------------------- */
        /* -------------------------------------
      		SIDEBAR
      ------------------------------------- */
        /* ---------------------------------------------------
      		RESPONSIVENESS
      		Nuke it from orbit. It's the only way to be sure.
      ------------------------------------------------------ */
        /* Let's make sure tables in the content area are 100% wide */
        /* -------------------------------------------
      		PHONE
      		For clients that support media queries.
      		Nothing fancy.
      -------------------------------------------- */
        @media only screen and (max-width: 600px) {
            a[class="btn"] {
                display: block !important;
                margin-bottom: 10px !important;
                background-image: none !important;
                margin-right: 0 !important;
            }

            div[class="column"] {
                width: auto !important;
                float: none !important;
            }

            table.social div[class="column"] {
                width: auto !important;
            }
        }

        /*
              Animations
              simple animations to make the email feel more alive
               */
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

<body bgcolor="#FFFFFF" topmargin="0" leftmargin="0" marginheight="0" marginwidth="0"
    style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;-webkit-font-smoothing:antialiased;-webkit-text-size-adjust:none;height:100%;width:100% !important;'>
    <!-- HEADER -->
    <table class="head-wrap" bgcolor="dodgerblue"
        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;width:100%;'>
        <tr style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
            <td style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
            </td>
            <td class="header container" align=""
                style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;display:block !important;max-width:600px !important;margin:0 auto !important;clear:both !important;'>
                <!-- /content -->
                <div class="content"
                    style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;padding:15px;max-width:600px;margin:0 auto;display:block;'>
                    <table bgcolor="dodgerblue"
                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;width:100%;'>
                        <tr
                            style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                            <td
                                style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                                <h1
                                    style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;font-family:"HelveticaNeue-Light", "Helvetica Neue Light", "Helvetica Neue", Helvetica, Arial, "Lucida Grande", sans-serif;line-height:1.1;margin-bottom:15px;color:#000;font-weight:200;font-size:44px;'>
                                    <big
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;font-size:150%;color:#ffffff;line-height:1.2;text-transform:none;'>
                                        <strong
                                            style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>CMS</strong>
                                    </big>
                                </h1>
                            </td>
                        </tr>
                    </table>
                </div>
                <!-- /content -->
            </td>
            <td style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
            </td>
        </tr>
    </table>
    <!-- /HEADER -->
    <!-- BODY -->
    <table class="body-wrap"
        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;width:100%;'>
        <tr style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
            <td style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
            </td>
            <td class="container" align="" bgcolor="#FFFFFF"
                style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;display:block !important;max-width:600px !important;margin:0 auto !important;clear:both !important;'>
                <!-- content -->
                <div class="content"
                    style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;padding:15px;max-width:600px;margin:0 auto;display:block;'>
                    <table
                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;width:100%;'>
                        <tr
                            style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                            <td
                                style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                                <h1
                                    style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;font-family:"HelveticaNeue-Light", "Helvetica Neue Light", "Helvetica Neue", Helvetica, Arial, "Lucida Grande", sans-serif;line-height:1.1;margin-bottom:15px;color:#000;font-weight:200;font-size:44px;text-align: center;'>
                                    <strong
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                                        Suspicious Login Activity!
                                    </strong>
                                </h1>
                                <p class="lead"
                                    style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;margin-bottom:10px;font-weight:normal;font-size:14px;line-height:1.6;font-size:17px;'>
                                </p>
                                <h3
                                    style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;font-family:"HelveticaNeue-Light", "Helvetica Neue Light", "Helvetica Neue", Helvetica, Arial, "Lucida Grande", sans-serif;line-height:1.1;margin-bottom:15px;color:#000;font-weight:500;font-size:27px;'>
                                    Dear {},
                                    <br
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                                    <br
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                                    We detected suspicious password recovery activity from the IP <mark class="bold"
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;font-weight:bold;'>{}</mark>
                                    at <span class="bold"
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;font-weight:bold;'>{}</span>.
                                    <br
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                                </h3>
                                <br
                                    style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                                <!-- A Real Hero (and a real human being) -->
                                <p
                                    style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;margin-bottom:10px;font-weight:normal;font-size:14px;line-height:1.6;'>
                                    <img src="https://raw.githubusercontent.com/Pragyanshu-rai/CMS/d8bc6f4004c2f027b124bf07c36bf0e7bc4e16d2/static/cms/img/password_reset_warning.svg"
                                        alt="OTP Alert Image" class="pulsate"
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;max-width:100%;animation:pulse 2s ease-in-out infinite;'>
                                </p>
                                <!-- /hero -->
                                <p
                                    style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;margin-bottom:10px;font-weight:normal;font-size:14px;line-height:1.6;'>
                                </p>
                                <br>
                                <h3
                                    style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;font-family:"HelveticaNeue-Light", "Helvetica Neue Light", "Helvetica Neue", Helvetica, Arial, "Lucida Grande", sans-serif;line-height:1.1;margin-bottom:15px;color:#000;font-weight:500;font-size:27px;'>
                                    If this was you, then you can safely ignore this email and head to
                                    <a href="mailto:noreply.services.2001@gmail.com" class="btn btn-primary"
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;color:#2BA6CB;text-decoration:none;color:#FFF;background-color:#666;padding:10px 16px;font-weight:bold;margin-right:10px;text-align:center;cursor:pointer;display:inline-block;background-color:dodgerblue;border-radius:4%;'>CMS
                                        Website</a>.
                                    <br>
                                    <br>
                                    Not you? then notify us at
                                    <a href="mailto:noreply.services.2001@gmail.com" class="btn btn-primary"
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;color:#2BA6CB;text-decoration:none;color:#FFF;background-color:#666;padding:10px 16px;font-weight:bold;margin-right:10px;text-align:center;cursor:pointer;display:inline-block;background-color:dodgerblue;border-radius:4%;'>CMS
                                        Support</a>,
                                    <span class="text-muted"
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                                        so we can make sure no one else is trying to access your account.
                                    </span>
                                    <br>
                                    <br>
                                    We recommend that you update your password to a strong password here
                                    <a href="https://cms-wa.herokuapp.com/login/" class="btn btn-danger"
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;color:#2BA6CB;text-decoration:none;color:#FFF;background-color:#666;padding:10px 16px;font-weight:bold;margin-right:10px;text-align:center;cursor:pointer;display:inline-block;background-color:red;border-radius:4%;'>Update Password</a>.
                                    <br>
                                    <br>
                                    Thank you for being associated with <br
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                                    <span class="bold"
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;font-weight:bold;'>Clinic
                                        Management System
                                        (CMS).</span>
                                    <br
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                                    <br
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                                    Sincerely,
                                    <br
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                                    Team <span class="bold"
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;font-weight:bold;'>Clinic
                                        Management System (CMS)</span>
                                </h3>
                            </td>
                        </tr>
                    </table>
                </div>
                <!-- /content -->
            </td>
            <td style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
            </td>
        </tr>
    </table>
    <!-- /BODY -->
    <!-- FOOTER -->
    <table class="footer-wrap dark"
        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;background-color:#dad7d7;width:100%;clear:both !important;'>
        <tr style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
            <td style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
            </td>
            <td class="container"
                style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;display:block !important;max-width:600px !important;margin:0 auto !important;clear:both !important;'>
                <!-- content -->
                <div class="content"
                    style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;padding:15px;max-width:600px;margin:0 auto;display:block;'>
                    <table
                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;width:100%;'>
                        <tr
                            style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                            <td align="center"
                                style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                                <p
                                    style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;margin-bottom:10px;font-weight:normal;font-size:14px;line-height:1.6;'>
                                </p>
                                <div class="code bold"
                                    style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;font-weight:bold;color:dodgerblue;'>
                                    &copy; 2021 Clinic Management Service, Ltd.
                                    <br
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                                    <br
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                                    &commat;Pragyanshu Rai
                                </div>
                            </td>
                        </tr>
                    </table>
                </div>
                <!-- /content -->
            </td>
            <td style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
            </td>
        </tr>
    </table>
    <!-- /FOOTER -->
</body>

</html>
"""

email_body_password_changed_html: str = """\
<!DOCTYPE html
    PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>

<head>
    <!-- If you delete this meta tag, the ground will open and swallow you. -->
    <meta name="viewport" content="width=device-width">
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>PASSWORD CHANGE EMAIL</title>
    <style>
        .btn-primary:hover {
            background-color: dodgerblue;
            color: white
        }
    </style>
    <style type="text/css">
        /* -------------------------------------
      		GLOBAL
      ------------------------------------- */
        /* -------------------------------------
      		ELEMENTS
      ------------------------------------- */
        /* -------------------------------------
      		HEADER
      ------------------------------------- */
        /* -------------------------------------
      		BODY
      ------------------------------------- */
        /* -------------------------------------
      		FOOTER
      ------------------------------------- */
        /* -------------------------------------
      		TYPOGRAPHY
      ------------------------------------- */
        /* -------------------------------------
      		SIDEBAR
      ------------------------------------- */
        /* ---------------------------------------------------
      		RESPONSIVENESS
      		Nuke it from orbit. It's the only way to be sure.
      ------------------------------------------------------ */
        /* Let's make sure tables in the content area are 100% wide */
        /* -------------------------------------------
      		PHONE
      		For clients that support media queries.
      		Nothing fancy.
      -------------------------------------------- */
        @media only screen and (max-width: 600px) {
            a[class="btn"] {
                display: block !important;
                margin-bottom: 10px !important;
                background-image: none !important;
                margin-right: 0 !important;
            }

            div[class="column"] {
                width: auto !important;
                float: none !important;
            }

            table.social div[class="column"] {
                width: auto !important;
            }
        }

        /*
              Animations
              simple animations to make the email feel more alive
               */
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

<body bgcolor="#FFFFFF" topmargin="0" leftmargin="0" marginheight="0" marginwidth="0"
    style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;-webkit-font-smoothing:antialiased;-webkit-text-size-adjust:none;height:100%;width:100% !important;'>
    <!-- HEADER -->
    <table class="head-wrap" bgcolor="dodgerblue"
        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;width:100%;'>
        <tr style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
            <td style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
            </td>
            <td class="header container" align=""
                style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;display:block !important;max-width:600px !important;margin:0 auto !important;clear:both !important;'>
                <!-- /content -->
                <div class="content"
                    style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;padding:15px;max-width:600px;margin:0 auto;display:block;'>
                    <table bgcolor="dodgerblue"
                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;width:100%;'>
                        <tr
                            style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                            <td
                                style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                                <h1
                                    style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;font-family:"HelveticaNeue-Light", "Helvetica Neue Light", "Helvetica Neue", Helvetica, Arial, "Lucida Grande", sans-serif;line-height:1.1;margin-bottom:15px;color:#000;font-weight:200;font-size:44px;'>
                                    <big
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;font-size:150%;color:#ffffff;line-height:1.2;text-transform:none;'>
                                        <strong
                                            style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>CMS</strong>
                                    </big>
                                </h1>
                            </td>
                        </tr>
                    </table>
                </div>
                <!-- /content -->
            </td>
            <td style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
            </td>
        </tr>
    </table>
    <!-- /HEADER -->
    <!-- BODY -->
    <table class="body-wrap"
        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;width:100%;'>
        <tr style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
            <td style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
            </td>
            <td class="container" align="" bgcolor="#FFFFFF"
                style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;display:block !important;max-width:600px !important;margin:0 auto !important;clear:both !important;'>
                <!-- content -->
                <div class="content"
                    style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;padding:15px;max-width:600px;margin:0 auto;display:block;'>
                    <table
                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;width:100%;'>
                        <tr
                            style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                            <td
                                style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                                <h1
                                    style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;font-family:"HelveticaNeue-Light", "Helvetica Neue Light", "Helvetica Neue", Helvetica, Arial, "Lucida Grande", sans-serif;line-height:1.1;margin-bottom:15px;color:#000;font-weight:200;font-size:44px;text-align: center;'>
                                    <strong
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                                        PASSWORD CHANGED!
                                    </strong>
                                </h1>
                                <p class="lead"
                                    style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;margin-bottom:10px;font-weight:normal;font-size:14px;line-height:1.6;font-size:17px;'>
                                </p>
                                <h3
                                    style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;font-family:"HelveticaNeue-Light", "Helvetica Neue Light", "Helvetica Neue", Helvetica, Arial, "Lucida Grande", sans-serif;line-height:1.1;margin-bottom:15px;color:#000;font-weight:500;font-size:27px;'>
                                    Dear {},
                                    <br
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                                    <br
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                                    Thank you for being associated with <br
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                                    <span class="bold"
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;font-weight:bold;'>Clinic
                                        Management System
                                        (CMS).</span>
                                    <br
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                                    <br
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                                    Your request for password reset originating from IP address <mark class="bold"
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;font-weight:bold;'>{}</mark>
                                    at <span class="bold"
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;font-weight:bold;'>{}</span>
                                    has been successful.
                                    <br
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                                </h3>
                                <br
                                    style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                                <!-- A Real Hero (and a real human being) -->
                                <p
                                    style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;margin-bottom:10px;font-weight:normal;font-size:14px;line-height:1.6;'>
                                    <img src="https://raw.githubusercontent.com/Pragyanshu-rai/CMS/d8bc6f4004c2f027b124bf07c36bf0e7bc4e16d2/static/cms/img/password_reset_alert.svg"
                                        alt="OTP Alert Image" class="pulsate"
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;max-width:100%;animation:pulse 2s ease-in-out infinite;'>
                                </p>
                                <!-- /hero -->
                                <p
                                    style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;margin-bottom:10px;font-weight:normal;font-size:14px;line-height:1.6;'>
                                </p>
                                <br>
                                <h3
                                    style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;font-family:"HelveticaNeue-Light", "Helvetica Neue Light", "Helvetica Neue", Helvetica, Arial, "Lucida Grande", sans-serif;line-height:1.1;margin-bottom:15px;color:#000;font-weight:500;font-size:27px;'>
                                    If this was you, then you can safely ignore this email and head to
                                    <a href="mailto:noreply.services.2001@gmail.com" class="btn btn-primary"
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;color:#2BA6CB;text-decoration:none;color:#FFF;background-color:#666;padding:10px 16px;font-weight:bold;margin-right:10px;text-align:center;cursor:pointer;display:inline-block;background-color:dodgerblue;border-radius:4%;'>CMS
                                        Website</a>.
                                    <br>
                                    <br>
                                    Not you? then notify us at
                                    <a href="mailto:noreply.services.2001@gmail.com" class="btn btn-primary"
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;color:#2BA6CB;text-decoration:none;color:#FFF;background-color:#666;padding:10px 16px;font-weight:bold;margin-right:10px;text-align:center;cursor:pointer;display:inline-block;background-color:dodgerblue;border-radius:4%;'>CMS
                                        Support</a>,
                                    <span class="text-muted"
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                                        so we can make sure no one else is trying to access your account.
                                    </span>
                                    <br>
                                    <br>
                                    Sincerely,
                                    <br
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                                    Team <span class="bold"
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;font-weight:bold;'>Clinic
                                        Management System (CMS)</span>
                                </h3>
                            </td>
                        </tr>
                    </table>
                </div>
                <!-- /content -->
            </td>
            <td style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
            </td>
        </tr>
    </table>
    <!-- /BODY -->
    <!-- FOOTER -->
    <table class="footer-wrap dark"
        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;background-color:#dad7d7;width:100%;clear:both !important;'>
        <tr style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
            <td style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
            </td>
            <td class="container"
                style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;display:block !important;max-width:600px !important;margin:0 auto !important;clear:both !important;'>
                <!-- content -->
                <div class="content"
                    style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;padding:15px;max-width:600px;margin:0 auto;display:block;'>
                    <table
                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;width:100%;'>
                        <tr
                            style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                            <td align="center"
                                style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                                <p
                                    style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;margin-bottom:10px;font-weight:normal;font-size:14px;line-height:1.6;'>
                                </p>
                                <div class="code bold"
                                    style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;font-weight:bold;color:dodgerblue;'>
                                    &copy; 2021 Clinic Management Service, Ltd.
                                    <br
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                                    <br
                                        style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
                                    &commat;Pragyanshu Rai
                                </div>
                            </td>
                        </tr>
                    </table>
                </div>
                <!-- /content -->
            </td>
            <td style='margin:0;padding:0;font-family:"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'>
            </td>
        </tr>
    </table>
    <!-- /FOOTER -->
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
