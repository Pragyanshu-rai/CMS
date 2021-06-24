from os import environ
from twilio.rest import Client

# sendSMS takes two str type objects body and to, if to is not provided then the sms will be sent to the default number
def sendSMS(body, to=environ["MY_PHONE_NUMBER"]):

    client = Client(environ["MY_ACC_SID"], environ["MY_AUTH_TOKEN"])

    client.messages.create(
        to=to,
        from_="+18505839086",
        body=body
    )

    print("SMS SENT!")