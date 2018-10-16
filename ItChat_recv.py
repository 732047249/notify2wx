# -*- coding:utf-8 -*-
# @Author :songtao

import itchat
import json
from itchat.content import *
from websocket import create_connection
from urllib import request

#调用websocket发送消息
def send_message(url, message):
    ws = create_connection(url)
    print("Sending message...")
    ws.send(message)
    print("Sent successful!")
    ws.close()

#接收信息
@itchat.msg_register([TEXT])
def simple_reply(msg):
    if  msg['FromUserName'] == '@f4fd04eecac8b98f279360c90c48f563':
        return
    url = 'ws://127.0.0.1:8006/ws/itchat'
    msg = json.dumps(msg)
    print(msg)
    send_message(url, msg)

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    if  msg['FromUserName'] == '@f4fd04eecac8b98f279360c90c48f563':
        return
    print('msg',msg)
    msg['Text'](msg['FileName'])
    message = '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])
    url = 'ws://127.0.0.1:8006/ws/itchat'
    send_message(url, message)
    return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])

if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    itchat.run()