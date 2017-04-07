# -*- coding: utf-8 -*-

from support import time_manager

time_str = '2017-04-16 15:14:50'
ts = time_manager.datetime_to_timestamp(time_str)
print(time_manager.timestamp_to_datetime(ts))