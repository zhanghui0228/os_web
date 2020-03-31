'''
    对系统的一个健康检查，用于每天固定巡检
        巡检项：
            系统基本信息
            url健康检查

        输出：
            引用机器人，发送到钉钉

'''
import os
import yaml
import time
import json
import requests
from logzero import logfile, logger, logging
from . import settings


log_path = os.path.join(settings.BASE_DIR, "log") 
URL_PATH = os.path.join(settings.BASE_DIR, "conf", "url.yaml")
PORT_PATH = os.path.join(settings.BASE_DIR, "conf", "init.yaml")
with open(URL_PATH, 'r', encoding='utf-8') as url:
    url_list = yaml.load(url, Loader=yaml.FullLoader)   # url_list['URL']
with open(PORT_PATH, 'r', encoding='utf-8') as port:
    init_info = yaml.load(port, Loader=yaml.FullLoader)

try:
    if os.path.exists(log_path) == False:
        os.mkdir(log_path)
except Exception as err:
    print("创建日志目录失败,错误原因：{}".format(err))

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(name)s - %(moduls)s-%(processName)s-%(message)s')
logfile("log/healthy.log", maxBytes=3000000, backupCount=2, encoding="utf-8")


# 消息通知
def message_notice(info):
    webhook = init_info['webhook']
    keywords = init_info['keywords']
    headers = {'Content-Type': 'application/json;charset=utf-8'}
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


# 健康检查
def local_healthy():
    local_url = []
    for u in range(len(url_list['URL'])):
        try:
            # 定义url
            url = "http://127.0.0.1:{port}/{option}".format(port=init_info['server_port'], option=url_list['URL'][u])
            connect_status = requests.get("{}".format(url), timeout=3).status_code
            local_info = {url: connect_status}
            logger.info("[url:{0}; 状态:{1}]".format(url, connect_status))
            local_url.append(local_info)
        except Exception as err:
            info = "{}健康检查失败".format(url)
            message_notice(info)
            logger.error("检查url失败：{}".format(err))
    return local_url




# # 定时检查url健康状态 
# def check_url():
#     while True:
#         local_healthy()
#         time.sleep(3000)