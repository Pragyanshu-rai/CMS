import smtplib
from email.message import EmailMessage
from os import environ


def sendEmail(subject, body, to, alternative=None):
    """
        Given the subject, body(plain text), recipient and an optional
        html email body this function will send an email to the recipient.
        NOTE: alternative html email body is optional.
    """

    # create EmailMessage object
    message = EmailMessage()
    # set the body of mail
    message.set_content(body)

    # add the alternative if provided
    if alternative is not None:
        message.add_alternative(alternative, subtype='html')

    # authentication
    sender = environ["SYSTEM_EMAIL"]
    password = environ["SYSTEM_EMAIL_PASSKEY"]

    message['subject'] = subject
    message['to'] = to
    message['from'] = sender

    try:

        server = smtplib.SMTP(
            environ["SYSTEM_EMAIL_HOST"], environ["SYSTEM_EMAIL_PORT"])
        server.starttls()
        server.login(sender, password)
        # send mail
        server.send_message(message)
        server.quit()

    except Exception as error:
        print("[SERVER ERROR] EMAIL ERROR - ", error)


def format_email_body(body: str, user_name: str, user_ip: str, current_date_time: str, otp:str = None) -> str:
    """
        Given the email body and the details to fill in this function will fill the data in the string. \n
        NOTE: Only otp is optional argument.
    """
    substitutes: list = [
        user_name,
        user_ip,
        current_date_time,
    ]

    if otp is not None:
        substitutes.append(otp)
    
    body = body.format(*substitutes)

    return body
