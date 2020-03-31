# 添加计划任务
import os
from logzero import logfile, logger, logging
from crontab import CronTab
from web_system import settings


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(name)s - %(moduls)s-%(processName)s-%(message)s')
logfile("log/cron.log", maxBytes=3000000, backupCount=2, encoding="utf-8")

# 获取python安装路径
install_path = dict(os.environ).get('_')
# 任务中脚本执行路径
run_path = os.path.join(settings.BASE_DIR, 'bin/check.py')
# 创建当前用户的计划任务
my_user_cron = CronTab(user=True)
# 创建任务
job_1 = my_user_cron.new(command='{0} {1}'.format(install_path, run_path))
# 设置任务执行周期，每天18执行一次
job_1.setall('* 18 * * *')
# 启动任务
job_1.enable()
# 写入配置文件
try:
    my_user_cron.write()
    logger.info("任务创建成功！")
except Exception as err:
    logger.error("任务创建失败！")