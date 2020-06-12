"""
@author Jacob Xie
@time 6/5/2020
"""

from typing import List
import pandas as pd

__default_date_formatter = "%Y%m%d"


def str_to_timestamp(d: str) -> pd.Timestamp:
    return pd.Timestamp(d)


def timestamp_to_str(d: pd.Timestamp, formatter: str = __default_date_formatter) -> str:
    return d.strftime(formatter)


def day_before(d: str, offset: int = 1, formatter: str = __default_date_formatter) -> str:
    return timestamp_to_str(str_to_timestamp(d) - pd.Timedelta(days=offset), formatter)


def day_after(d: str, offset: int = 1, formatter: str = __default_date_formatter) -> str:
    return timestamp_to_str(str_to_timestamp(d) + pd.Timedelta(days=offset), formatter)


def today(formatter: str = __default_date_formatter) -> str:
    return timestamp_to_str(pd.Timestamp.today(), formatter)


def yesterday(formatter: str = __default_date_formatter) -> str:
    return day_before(today(), formatter=formatter)


def tomorrow(formatter: str = __default_date_formatter) -> str:
    return day_after(today(), formatter=formatter)


def __gen_dates(start_date: str, end_date: str) -> pd.Series:
    return pd.date_range(start_date, end_date, freq='D').to_series().dt.dayofweek


def generate_dates(start_date: str, end_date: str, formatter: str = __default_date_formatter) -> List[str]:
    return list(map(lambda x: timestamp_to_str(x, formatter), __gen_dates(start_date, end_date).index))


def generate_workdays(start_date: str, end_date: str, formatter: str = __default_date_formatter) -> List[str]:
    date_series = __gen_dates(start_date, end_date)
    days = list(date_series[date_series.map(lambda x: False if x in [5, 6] else True)].index)
    return [timestamp_to_str(i, formatter) for i in days]


def generate_weekends(start_date: str, end_date: str, formatter: str = __default_date_formatter) -> List[str]:
    date_series = __gen_dates(start_date, end_date)
    days = list(date_series[date_series.map(lambda x: True if x in [5, 6] else False)].index)
    return [timestamp_to_str(i, formatter) for i in days]
