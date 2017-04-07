import datetime, time


def datetime_to_timestamp(datetime_str):
    date_datetime = datetime.datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
    stamp = str(time.mktime(date_datetime.timetuple())).replace('.', '')
    stamp += '0' * (13 - len(stamp))
    return stamp


def timestamp_to_datetime(timestamp_str):
    datetime_str = datetime.datetime.fromtimestamp(float(timestamp_str)/1000)
    return datetime_str
