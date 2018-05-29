#!/usr/bin/env python
# coding=utf8

"""
用于计算评论的情感极性，即好评与差评
rpc调用，client
"""
from xmlrpc.client import ServerProxy

if __name__=="__main__":
    sent = "不错的鞋子"
    with ServerProxy("http://47.52.1.34:8000/") as proxy:
        print("\"%s\"为\"%s\"" % (sent,proxy.sentiment(sent)))

