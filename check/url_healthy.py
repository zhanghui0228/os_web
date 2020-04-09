'''
    检查url脚本
'''
import os
import yaml
import requests
from logzero import logfile, logger, logging
import message

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(name)s - %(moduls)s-%(processName)s-%(message)s')
logfile("log/url.log", maxBytes=3000000, backupCount=2, encoding="utf-8")


# 获取url信息
def pull_url():
    url_conf = "conf/url.yaml"
    with open(url_conf, 'r', encoding='utf-8') as info:
        url_list = yaml.load(info, Loader=yaml.FullLoader)
    return url_list['URL']


def pull_port():
    port_conf = "conf/init.yaml"
    with open(port_conf, 'r', encoding='utf-8') as info:
        port = yaml.load(info, Loader=yaml.FullLoader)
    return port['server_port']


# url健康检查
def healthy_url():
    local_info = []
    local_error = []
    url_list = pull_url()
    port = pull_port()
    for u in range(len(url_list)):
        url = "http://127.0.0.1:{0}/{1}".format(port, url_list[u])
        try:
            connect_status = requests.get(url, headers={'Connection': 'close'}, timeout=3).status_code
            url_info = {url: connect_status}
            local_info.append(url_info)
            logger.debug("检查信息：{}".format(url_info))
        except Exception as err:
            error_info = {"检查信息：{0}, 错误原因:{1}".format(url, err)}
            logger.error("{}".format(error_info))
            local_error.append(error_info)
    local_message = {
        "SUCESS": local_info,
        "FAILED": local_error
    }
    return local_message




# 调用钉钉机器人接口
def main(info):
    try:
        logger.info(info)
        message.message_notice(info)
    except Exception as err:
        logger.error("失败：{}".format(err))


if __name__ == '__main__':
    main(healthy_url())