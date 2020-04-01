'''
    检查脚本，供计划任务使用
'''
from logzero import logfile, logger, logging
from . import check_healthy
from . import check_option
from . import message


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(name)s - %(moduls)s-%(processName)s-%(message)s')
logfile("log/cron.log", maxBytes=3000000, backupCount=2, encoding="utf-8")

# url健康状态
url_healthy = check_healthy.local_healthy()
# 系统基础信息
basics_healthy = check_option.useagent()



def healthy():
    local_info = [basics_healthy, url_healthy]
    try:
        # 钉钉机器人通知
        message.message_notice(local_info)
        logger.debug("发送信息：{}".format(check_healthy))
    except Exception as err:
        logger.error("消息发送失败:{}".format(err))