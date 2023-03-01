import os
import time

from utils.twilio.make_call import MakeCall
from utils.twilio.twilio_make_call import CTI


def test_make_out_bound_call(twilio_make_call: CTI) -> None:
    twiml = "https://handler.twilio.com/twiml/EHc80d560fe35c83e0ac79286d3052c7af"
    to_phone_number = os.environ.get('TO_PHONE_NUMBER')

    # Make CTI call using twilio
    call_sid = twilio_make_call.make_the_call(to_phone_number, twiml)
    print("call_sid print", call_sid)
    time.sleep(120)
    # END CTI twilio call
    twilio_make_call.end_the_call(call_sid, twiml)
