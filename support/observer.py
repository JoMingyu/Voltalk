# -*- coding: utf-8 -*-

import threading

from enertalk_infos import info
from support import time_manager

import requests
import json
import time


class Observer(threading.Thread):
    def run(self):
        usages = {}
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
                print(time.time(), id, json_obj['usage'])
                if usages[id] is None:
                    usages[id] = json_obj['usage']
                else:
                    if usages[id] * 1.3 < json_obj['usage'] or usages[id] * 0.7 > json_obj['usage']:
                        print(id, '이상하다')
                        pass
                    else:
                        usages[id] = (int(usages[id]) + int(json_obj['usage'])) / 2

            time.sleep(900)
