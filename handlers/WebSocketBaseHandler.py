# -*- coding: utf-8 -*-
# @Author  :songtao

import json
import tornado.web

# from utils.session import Session
from tornado.websocket import WebSocketHandler

class WebSocketBaseHandler(WebSocketHandler):

    @property
    def db(self):
        return self.application.db

    def prepare(self):
        self.xsrf_token
        if self.request.headers.get("Content-Type", "").startswith("application/json"):
            self.json_args = json.loads(self.request.body.decode('utf-8'))
        else:
            self.json_args = None


class StaticFileHandler(tornado.web.StaticFileHandler):
    def __init__(self, *args, **kwargs):
        super(StaticFileHandler, self).__init__(*args, **kwargs)





