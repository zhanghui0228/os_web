'''
    定义钉钉机器人进行消息发送
'''

import os
import json
import yaml
import requests
from logzero import logfile, logger, logging
# from . import settings


# PORT_PATH = os.path.join(settings.BASE_DIR, "conf", "init.yaml")
PORT_PATH = "conf/init.yaml"
with open(PORT_PATH, 'r', encoding='utf-8') as port:
    init_info = yaml.load(port, Loader=yaml.FullLoader)

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(name)s - %(moduls)s-%(processName)s-%(message)s')
logfile("log/message.log", maxBytes=3000000, backupCount=2, encoding="utf-8")

# 消息通知
def message_notice(info):
    webhook = init_info['webhook']
    keywords = init_info['keywords']
    headers = {'Content-Type': 'application/json;charset=utf-8', 'Connection': 'close',}
    pagrem = {
        "msgtype": "text", 
        "text": {
            "content": "{0},\n{1}".format(info, keywords)
        }, 
        "at": {
            "atMobiles": [
                "156xxxx8827", 
            ], 
            "isAtAll": False
        }
    }
    try:
        requests.post(webhook, json.dumps(pagrem),headers=headers).content
        logger.debug("{} 消息发送成功".format(info))
    except Exception as err:
        logger.error("消息发送失败：{}".format(err))
