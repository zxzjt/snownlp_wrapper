#!/usr/bin/env python
# coding=utf8

"""
用于判断评论的情感极性，即好评与差评
终端运行：python run_terminal.py 衣服真好 好评
"""

import sys

from snownlp import SnowNLP

if __name__=="__main__":
    texts= sys.argv[1:]
    sent = ' '.join(texts)
    try:
        # 计算句子得分
        prob = round(SnowNLP(sent).sentiments,2)
    except:
        print("SnowNLP(sent).sentiments Error!")
    else:
        # 大于0.55为好评
        if prob > 0.55:
            pos_neg = "好评"
        elif prob < 0.45:
            pos_neg = "差评"
        else:
            pos_neg = "中性"
        print("\"%s\"为\"%s\", score为%s" % (sent,pos_neg,prob))
