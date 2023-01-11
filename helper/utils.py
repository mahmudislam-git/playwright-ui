from datetime import datetime
from pytz import timezone


def get_current_date_time(self) -> str:
    tz = timezone('EST')
    now = datetime.now(tz)
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S %p")
    return dt_string
