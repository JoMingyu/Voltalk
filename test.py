# -*- coding: utf-8 -*-

import fbchat

username = 'dmdkzm3@naver.com'
password = 'uursty67a9e9e4'
target_uid = '126982884508007'
client = fbchat.Client(username, password)
# friends = client.getUsers('김성훈')
# friend = friends[0]
# print(friend.uid)
sent = client.send(target_uid, '서울대 3동 전기사용량 알려줘')
