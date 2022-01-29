

email_subject_otp: str = "Changing your CMS password"
email_subject_invalid_login: str = ""
email_subject_password_changed: str = ""

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

You have requested for password change originating from IP address {} for which the One Time Password (OTP) - "{}" has been generated at {}.

In case you have not requested for password change you can notify us at - noreply.services.2001@gmail.com.

Disclaimer!

We recommend you do not share this OTP with anyone to prevent fraudulent transactions.

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

"""

email_body_invalid_login_html: str = """\

"""

email_body_password_changed_html: str = """\

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
