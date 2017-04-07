# -*- coding: utf-8 -*-

import threading
import requests
import json
import time

from enertalk_infos import info
from support import time_manager
from firebase import fcm_sender


class Observer(threading.Thread):
    def run(self):
        usages = {}
        sender = fcm_sender.FCMSender('AAAAI9HJHSc:APA91bEb1Y87VH-0RV5eNUDFu9faMikVY4NoUFVEVEAoZzdadtkWLs0dl1wt4BMCgEt3YRMGYgpeolYDPB0nvy9SJMWcARAsuEgMvTolxGAU7aQSAfOTjzQxUL4ndKl2zrzv_v5xbPQ4')
        for id in info.site_ids.keys():
            usages[id] = None

        while True:
            now = time_manager.get_cur_datetime()
            now_stamp = time_manager.datetime_to_timestamp(now)
            before_1minute_stamp = int(now_stamp) - 900000
            params = {'start': before_1minute_stamp, 'end': now_stamp}
            for id in info.site_ids.keys():
                response = requests.get(info.URL + 'sites/' + info.site_ids[id] + '/usages/periodic', headers=info.headers, params=params)
                json_obj = json.loads(response.text)
                if usages[id] is None:
                    usages[id] = json_obj['usage']
                else:
                    if usages[id] * 1.15 < json_obj['usage'] or usages[id] * 0.85 > json_obj['usage']:
                        sender.send(info.site_ids[id], id)
                        pass
                    else:
                        usages[id] = (int(usages[id]) + int(json_obj['usage'])) / 2

            time.sleep(900)
