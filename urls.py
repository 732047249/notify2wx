# -*- coding: utf-8 -*-
# @Author  :songtao

import os

from config import *
from handlers import ItChat,WebHandler
from handlers.BaseHandler import StaticFileHandler

handlers=[
        (r"/api/room", ItChat.RoomHandler),
        (r"/ws/itchat", WebHandler.wsItchatHandler),
    ]
