# -*- coding: utf-8 -*-

import datetime, time


def date_to_timestamp(datetime_str):
    date_datetime = datetime.datetime.strptime(datetime_str, '%Y-%m-%d')
    stamp = str(time.mktime(date_datetime.timetuple())).replace('.', '')
    stamp += '0' * (13 - len(stamp))
    return stamp


def datetime_to_timestamp(date_str):
    date = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    stamp = str(time.mktime(date.timetuple())).replace('.', '')
    stamp += '0' * (13 - len(stamp))
    return stamp


def timestamp_to_datetime(timestamp_str):
    datetime_str = datetime.datetime.fromtimestamp(float(timestamp_str)/1000)
    return datetime_str


def get_cur_datetime():
    cur_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return cur_datetime
