# -*- coding:utf-8 -*-
# @Author :songtao

import itchat
import logging
import datetime

from utils.response_code import RET
from .BaseHandler import BaseHandler

class RoomHandler(BaseHandler):
    """
    kline 数据
    """
    def post(self, *args, **kwargs):
        msg = self.get_argument('msg', default=None)
        username = self.get_argument('username', default=None)
        print(msg)
        print(username)
        itchat.auto_login(hotReload=True)
        # rooms = itchat.get_chatrooms(update=True)
        room  = itchat.search_chatrooms(username)
        if not room:
            return self.write(dict(errcode=RET.PARAMERR, errmsg="群名不存在"))
        # friend = itchat.search_friends('chengshen')
        # print(friend)
        username = room[0]['UserName']
        ret = itchat.send(msg, toUserName=username)
        self.write(dict(code=RET.OK, errmsg="", data=ret))


