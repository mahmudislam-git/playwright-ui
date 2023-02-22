from utils.twilio.make_call import MakeCall


def test_make_out_bound_call(make_call: MakeCall) -> None:
    make_call.dial_out_bound_call()