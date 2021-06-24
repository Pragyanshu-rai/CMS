import smtplib
import datetime
from email.message import EmailMessage  

# import random


def send_email(subject, otp, to):

    body = """
Dear Customer,

Thank you for being associated with Clinic Management System (CMS).

You have requested for password change for which One Time Password (OTP):- """+str(otp)+""" has been generated at """+str(datetime.datetime.now()).split(".")[0]+""".

In case you have not requested for password change you can write an email at "noreply.services.2001@gmail.com".

Disclaimer

We recommend you do not share this with anyone to prevent fraudulent transactions.

Sincerely,
Clinic Management System (CMS)
    """

    # create EmailMessage object
    message = EmailMessage()
    # set the body of mail
    message.set_content(body)
    message['subject'] = subject
    message['to'] = to
    
    sender = "noreply.services.2001@gmail.com"
    password = "cxzifunjhbptvsml"
    
    message['from'] = sender
    try :
        
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        # send mail
        server.send_message(message)

        server.quit()
    
    except:

        server.quit()


