import os

from twilio.rest import Client


class CTI:

    def __init__(self, account_sid: str, auth_token: str, from_number: str) -> None:
        self.client = Client(account_sid, auth_token)
        self.from_number = from_number

    def make_the_call(self, to_number: str, twiml: str) -> str:
        call = self.client.calls.create(
            url=twiml,
            to=to_number,
            from_=self.from_number,
        )
        return call.sid

    def end_the_call(self, call_sid: str, twiml: str) -> None:
        # self.client.calls(call_sid).update(url=twiml, method="POST")
        self.client.calls(call_sid).update(status='completed')
