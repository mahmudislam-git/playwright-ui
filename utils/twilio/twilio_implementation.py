# import logging
# from contextlib import suppress
# from datetime import datetime
# from enum import Enum
# from typing import List, Union
#
# from config import EnvConfig
#
# from twilio.rest import Client
#
#
# def add_leading_zeros(date_obj: str) -> str:
#     """helper"""
#     return date_obj.zfill(2) if len(date_obj) == 1 else date_obj
#
#
# class TWIML(Enum):
#     NYHA_BASE = ""
#
#
# class Base:
#     def __int__(self, to: str, from_: str, account_sid: str, auth_token: str):
#         self.to = to
#         self.from_ = from_
#         self.account_sid = account_sid
#         self.auth_token = auth_token
#         self.client = Client(self.account_sid, self.auth_token)
#
#
# class Voice(Base):
#
#     def __init__(self, *args, **kwargs) -> None:
#         super().__init__(*args, **kwargs)
#         self.call = None
#         self.twiml = TWIML
#         self.env_config = EnvConfig()
#
#     def make_call(self, twiml: TWIML, payload: Union[None, dict]):
#         """make the twilio call"""
#         if not isinstance(twiml, TWIML):
#             raise TypeError('twiml param is not type TWIML')
#
#         if twiml == TWIML.NYHBE_ENGLISH_PAYLOAD:
#             date, month, year = payload['dob'].split('/')
#             try:
#                 postal_code = payload['postal_code']
#             except KeyError:
#                 postal_code= '12211'
#
#             url = TWIML.NYHBE_ENGLISH_PAYLOAD.value.format(
#
#
#             )
#
#             elif twiml
#
