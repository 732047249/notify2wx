# -*- coding:utf-8 -*-
# @Author :songtao

# import itchat
import requests

def test():
    url = 'http://127.0.0.1:8003/api/room'

    res = requests.post(url, {'msg':'测试， 忽略', 'username': '主动基金开发python组'})

    return res.text


if __name__ == '__main__':
    rep = test()
    print(rep)
