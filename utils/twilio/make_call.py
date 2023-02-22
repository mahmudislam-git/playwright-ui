import os

from twilio.rest import Client


class MakeCall:

    def __init__(self) -> None:
        self.account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
        self.auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

    def dial_out_bound_call(self) -> None:

        client = Client(self.account_sid, self.auth_token)

        call = client.calls.create(
            to=os.environ.get('TO_PHONE_NUMBER'),
            from_=os.environ.get('FROM_TWILIO_PHONE_NUMBER'),
            url="http://demo.twilio.com/docs/voice.xml"

    
        )

        print(call.sid)
