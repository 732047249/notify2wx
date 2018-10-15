# -*- coding:utf-8 -*-
# @Author :songtao

import itchat
from itchat.content import *


def send_msg():
    itchat.auto_login(hotReload=True)

    # 发送给群
    room = itchat.search_chatrooms('主动基金开发python组')

    # 发送给朋友
    # friend = itchat.search_friends('chengshen')
    print(room)
    username = room[0]['UserName']
    itchat.send('hello. 我是机器人', toUserName=username)


# 接收信息
@itchat.msg_register([PICTURE, TEXT])
def simple_reply(msg):
    if msg['Type'] == TEXT:
        print(msg)
    else:
        pass


if __name__ == '__main__':
    send_msg()

    # itchat.auto_login(hotReload=True)
    # itchat.send('Hello filehelper', toUserName='filehelper')
    # itchat.run()