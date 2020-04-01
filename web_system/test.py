import os
import yaml
import settings
from logzero import logfile, logger, logging

# conf file path
CONF_PATH = os.path.join(settings.BASE_DIR, "conf", "init.yaml")
with open(CONF_PATH, 'r', encoding='utf-8') as conffile:
    INFO = yaml.load(conffile, Loader=yaml.FullLoader)

# 获取url信息
URL_PATH = os.path.join(settings.BASE_DIR, "conf", "url.yaml")
# 获取项目端口信息
PORT_PATH = os.path.join(settings.BASE_DIR, "conf", "init.yaml")
with open(URL_PATH, 'r', encoding='utf-8') as url:
    url_list = yaml.load(url, Loader=yaml.FullLoader)   # url_list['URL']
with open(PORT_PATH, 'r', encoding='utf-8') as port:
    init_info = yaml.load(port, Loader=yaml.FullLoader)


def local_healthy():
    local_url = []
    local_err_url = []
    for u in range(len(url_list['URL'])):
        # 定义url
        url = "http://127.0.0.1:{port}/{option}".format(port=init_info['server_port'], option=url_list['URL'][u])
        connect_status = requests.get("{}".format(url), timeout=3).status_code
        local_info = {url: connect_status}
        logger.info("[url:{0}; 状态:{1}]".format(url, connect_status))
        local_url.append(local_info)
        # except Exception as err:
        #     info = "{}健康检查失败".format(url)
        #     message_notice(info)
        #     local_err_url.append(info)
        #     logger.error("检查url失败：{}".format(err))
    return [local_url, local_err_url]
