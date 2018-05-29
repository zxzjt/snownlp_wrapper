#!/usr/bin/env python
# coding=utf8

"""
用于计算评论的情感极性，即好评与差评
rpc调用，server
"""
import logging,sys
from xmlrpc.server import SimpleXMLRPCServer
from socketserver import ThreadingMixIn

from snownlp import SnowNLP

class ZiyuLogging(object):
    """日志记录
    记录调试和校验日志
    """
    @staticmethod
    def config(logger, path):
        """日志配置
        :param logger:创建Logging对象
        :return:None
        """
        # 指定logger输出格式
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(filename)s:%(lineno)s - %(message)s')
        # 文件日志
        file_handler = logging.FileHandler(path, encoding='utf8')
        file_handler.setFormatter(formatter)  # 可以通过setFormatter指定输出格式
        # 控制台日志
        # console_handler = logging.StreamHandler(sys.stdout)
        # console_handler.formatter = formatter  # 也可以直接给formatter赋值
        # 为logger添加的日志处理器
        logger.addHandler(file_handler)
        # logger.addHandler(console_handler)
        # 指定日志的最低输出级别，默认为WARN级别
        logger.setLevel(logging.INFO)

class ThreadXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
    """
    多线程rpc
    """
    pass

def sentiment(sent):
    """
    第三方调用来判断好评与差评
    :param sent:待判断的句子（str类型）
    :return:返回好评或差评，和对应得分，两者下划线连接（str类型）
    """
    logger = logging.getLogger(log_unit)
    try:
        # 计算句子得分
        prob = round(SnowNLP(sent).sentiments,2)
    except:
        logger.info(sent + ':' + 'Exception')
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
        res = pos_neg+'_'+str(prob)
        logger.info(sent+':'+res)
        return res

if __name__=="__main__":
    home_path = './'
    log_unit = 'sentiment'
    # 日志开启
    ZiyuLogging.config(logger=logging.getLogger(log_unit), path=home_path + log_unit+'.log')
    server = ThreadXMLRPCServer(('47.52.1.34', 8000),allow_none=True)
    server.register_function(sentiment, "sentiment")
    server.serve_forever()

