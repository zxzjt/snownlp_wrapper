模块说明
本模块用于判断句子的情感极性，即好评或差评
采用python3实现

性能
时间：平均49条/s（双核CPU 3.2G，Memory 8G）
准确率：pos_acc 0.85, neg_acc 0.83, acc 0.84（训练集）
召回率：pos_recall 0.80 neg_recall 0.88（训练集）

调用
1、终端运行
python run_terminal.py 衣服真好 好评

2、python第三方调用
函数sentiment(sent)
:param sent:待判断的句子（str类型）
:return:返回好评或差评，和对应得分，两者下划线连接（str类型），如"好评_0.67"
示例：
from call_sample import sentiment

# 输入评论
sent = "衣服真好 好评"
# 输出判断
res = sentiment(sent)
if res != '1':
    print(res) # "好评_0.67"
else:
    print("SnowNLP(sent).sentiments Error!")

3、xmlrpc远程调用
注册函数sentiment(sent)
示例：
# python
sent = "衣服真好 好评"
ServerProxy("http://47.52.1.34:8000/").sentiment(sent)
# java
String sent = "衣服真好 好评";
XmlRpcClient client = new XmlRpcClient();
client.execute("sentiment", sent); 

依赖：
python3


