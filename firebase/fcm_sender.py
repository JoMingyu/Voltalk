# -*- coding: utf-8 -*-

from pyfcm import FCMNotification


class FCMSender:
    def __init__(self, server_key):
        self.push_service = FCMNotification(api_key=server_key)

    def send(self, topic_id, topic_name):
        message_title = topic_name
        message_body = '새로운 메시지가 있습니다'
        result = self.push_service.notify_topic_subscribers(topic_name=topic_id,
                                                            message_title=message_title,
                                                            message_body=message_body)

        return result
