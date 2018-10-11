# -*- coding: utf-8 -*-
# @Author  :songtao

import os

from config import *
from handlers import ItChat
from handlers.BaseHandler import StaticFileHandler

handlers=[
        (r"/api/room", ItChat.RoomHandler),
    ]
