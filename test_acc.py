#!/usr/bin/env python
# coding=utf8

import time

from call_sample import sentiment
#from sklearn import metrics

if __name__=="__main__":
    # 统计正样本召回率
    pos_recall_count = 0
    pos_count = 0
    with open('./snownlp/sentiment/pos.txt', 'r', encoding='utf8') as f:
        start_time = time.time()
        line = f.readline()
        while line:
            res = sentiment(line)
            if res != '1':
                if res.split('_')[0] == '好评':
                    pos_recall_count = pos_recall_count + 1
            else:
                print("SnowNLP(sent).sentiments Error!")
            pos_count = pos_count + 1
            if pos_count%100 ==0:
                print("finish %s." % pos_count)
            line = f.readline()
        end_time = time.time()
        print("pos recall is %s" % (pos_recall_count/pos_count))
        print("pos predition takes %s s, count %s, " % (str(end_time - start_time), pos_count))

    # 统计负样本召回率
    neg_recall_count = 0
    neg_count = 0
    with open('./snownlp/sentiment/neg.txt', 'r', encoding='utf8') as f:
        start_time = time.time()
        line = f.readline()
        while line:
            res = sentiment(line)
            if res != '1':
                if res.split('_')[0] == '差评':
                    neg_recall_count = neg_recall_count + 1
            else:
                print("SnowNLP(sent).sentiments Error!")
            neg_count = neg_count + 1
            if neg_count % 100 == 0:
                print("finish %s." % neg_count)
            line = f.readline()
        end_time = time.time()
        print("neg recall is %s" % (neg_recall_count/neg_count))
        print("neg predition takes %s s, count %s, " % (str(end_time-start_time),neg_count))

    # 计算准确率
    pos_acc = pos_recall_count/(pos_recall_count+neg_count-neg_recall_count)
    neg_acc = neg_recall_count/(neg_recall_count+pos_count-pos_recall_count)
    acc = (neg_recall_count+pos_recall_count)/(neg_count+pos_count)
    print("pos_acc %s, neg_acc %s, acc %s" % (pos_acc,neg_acc,acc))


