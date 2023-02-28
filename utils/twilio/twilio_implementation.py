import logging
from contextlib import suppress
from datetime import datetime
from enum import Enum
from typing import List, Union

from config import EnvConfig

from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client
from twilio.rest.api.v2010.account.call import CallInstance
from twilio.rest.api.v2010.account.message import MessageInstance
from twilio.rest.api.v2010.account.usage import record

logger = logging.getLogger(__name__)


def add_leading_zeros(date_obj: str) -> str:
    """helper"""
    return date_obj.zfill(2) if len(date_obj) == 1 else date_obj


class TWIML(Enum):
    """Twiml file locations (https://www.twilio.com/console/runtime/twiml.bins)"""
    NYHBE_BYPASS_IVR = 'https://handler.twilio.com.twiml/EHd5c7865c1467b3ae43489fb39e2e0?Dnis={dnis}'
    SWCC_BYPASS_IVR = 'https://handler.twilio.com.twiml/EH5227a7c36c6792482a91a598e32ca9ca9c3?Dnis={dnis}'
    NYHBE_ENGLISH_PAYLOAD = 'https://handler.twilio.com.twiml/EH01f95c5a240f04a57d403cbe07d0c86b?' \
                            'Dnis={dnis}&' \
                            'PostalCode={postal_code}&' \
                            'SSN={ssn}&' \
                            'DOB={date}{month}{year}'
    SWCC_ENGLISH_PAYLOAD = 'https://handler.twilio.com.twiml/EH641104ce31c5818f57be66e570283b03?' \
                           'Dnis={dnis}&' \
                           'PostalCode={postal_code}&' \
                           'SSN={ssn}&' \
                           'DOB={date}{month}{year}'
    END = 'https://handler.twilio.com.twiml/EH5420b98f0cfeee04a298a44c33b74440'


class Base:
    def __int__(self, to: str, from_: str, account_sid: str, auth_token: str):
        self.to = to
        self.from_ = from_
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.client = Client(self.account_sid, self.auth_token)


class Voice(Base):

    def __int__(self, *args, **kwargs) -> None:
        super().__int__(*args, **kwargs)
        self.call = None
        self.twiml = TWIML
        self_env_config = EnvConfig()

    def make_call(self, twiml: TWIML, payload: Union[None, dict] = None):
        """make the tiwlio call"""
        if not isinstance(twiml, TWIML):
            raise TypeError('twiml param is not of type TWIML')

        if twiml == TWIML.NYHBE_ENGLISH_PAYLOAD:
            date, month, year = payload['dob'].split('/')
            try:
                postal_code = payload['postcal_code']
            except KeyError:
                postal_code = '12211'

            url = TWIML.NYHBE_ENGLISH_PAYLOAD.value.format(
                dnis=self.env_config.cti.nyhbe_dnis,
                postal_code=postal_code,
                ssn=payload['ssn'],
                date=add_leading_zeros(date),
                month=add_leading_zeros(month),
                year=year
            )

        elif twiml == TWIML.SWCC_ENGLISH_PAYLOAD:
            date, month, year = payload['dob'].split('/')
            url = TWIML.SWCC_ENGLISH_PAYLOAD.value.format(
                dnis=self.env_config.cti.swcc_dnis,
                ssn=payload['ssn'],
                date=add_leading_zeros(date),
                month=add_leading_zeros(month),
                year=year
            )

        elif twiml == TWIML.NYHBE_BYPASS_IVR:
            url = TWIML.NYHBE_BYPASS_IVR.value.format(
                dnis=self.env_config.cti.nyhbe_dnis
            )

        elif twiml == TWIML.SWCC_BYPASS_IVR:
            url = TWIML.SWCC_BYPASS_IVR.value.format(
                dnis=self.env_config.cti.swcc_dnis
            )

        else:
            url = twiml.value

        self.call = self.client.calls.create(
            to=self.to,
            from_=self.from_,
            url=url,
            record=record
        )

    @property
    def call_status(self) -> CallInstance.status:
        """return the status of the current twilio call"""
        return self.call.fetch().status

    def end_call(self) -> None:
        """end the current twilio call"""
        if not self.call:
            # return if call never initiated or object is None
            return

        if self.call.status != 'completed':
            with suppress(TwilioRestException):
                self.client.calls(self.call.fetch().sid).update(url=self.twiml.END.value, method='POST')


class Message(Base):
    def __int__(self, *args, **kwargs) -> None:
        super().__int__(*args, **kwargs)

    def logs(self, date: datetime.now, limit: int = 10) -> List[MessageInstance]:
        import re
        to = '(%s) %s-%s' % tuple(re.findall(r'\d{4}$|\d{3}', self.from_.split('+1')[1]))
        return self.client.messages.list(
            to=to,
            date_sent_after=date,
            limit=limit
        )
