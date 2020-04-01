'''
    # 暂时废弃
    对系统的一个健康检查，用于每天固定巡检
        巡检项：
            系统基本信息
            url健康检查

        输出：
            引用机器人，发送到钉钉

'''
import os
import yaml
import json
import requests
from logzero import logfile, logger, logging
from . import settings
from . import message


log_path = os.path.join(settings.BASE_DIR, "log") 
# 获取url信息
URL_PATH = os.path.join(settings.BASE_DIR, "conf", "url.yaml")
# 获取项目端口信息
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



# 健康检查
# def local_healthy():
#     s = requests.session()
#     s.keep_alive = False
#     headers = {'Connection': 'close',}
#     local_url = []
#     local_err_url = []
#     for u in range(len(url_list['URL'])):
#         try:
#             # 定义url
#             url = "http://127.0.0.1:{port}/{option}".format(port=init_info['server_port'], option=url_list['URL'][u])
#             connect_status = requests.get("{}".format(url), headers=headers, timeout=3).status_code
#             local_info = {url: connect_status}
#             logger.info("[url:{0}; 状态:{1}]".format(url, connect_status))
#             local_url.append(local_info)
#         except Exception as err:
#             info = "{}健康检查失败".format(url)
#             message.message_notice(info)
#             local_err_url.append(info)
#             logger.error("检查url失败：{}".format(err))
#     return [local_url, local_err_url]
