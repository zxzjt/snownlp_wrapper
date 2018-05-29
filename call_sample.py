#!/usr/bin/env python
# coding=utf8

"""
用于计算评论的情感极性，即好评与差评
第三方调用
"""

from snownlp import SnowNLP

def sentiment(sent):
    """
    第三方调用来判断好评与差评
    :param sent:待判断的句子（str类型）
    :return:返回好评或差评，和对应得分，两者下划线连接（str类型）
    """
    try:
        # 计算句子得分
        prob = round(SnowNLP(sent).sentiments,2)
    except:
        return '1'
    else:
        # 大于0.55为好评
        if prob >0.55:
            pos_neg = "好评"
        elif prob < 0.45:
            pos_neg = "差评"
        else:
            pos_neg = "中性"
        #print("\"%s\"为\"%s\", score为%s" % (sent,pos_neg,prob))
        return pos_neg+'_'+str(prob)

if __name__=="__main__":
    # 输入评论
    sent = "衣服真好 好评"
    # 输出判断
    res = sentiment(sent)
    if res != '1':
        print(res)
    else:
        print("SnowNLP(sent).sentiments Error!")
