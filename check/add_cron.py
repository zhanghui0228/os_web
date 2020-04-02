# 添加计划任务 
import os
from logzero import logfile, logger, logging
from crontab import CronTab

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(name)s - %(moduls)s-%(processName)s-%(message)s')
logfile("log/cron.log", maxBytes=3000000, backupCount=2, encoding="utf-8")

# 计划任务执行脚本所在路径
check_path = os.path.dirname(__file__)
# 命令执行路径
comm_path = os.getcwd()
# 执行脚本名称
run_file = 'url_healthy.py'
# 获取python安装路径
install_path = dict(os.environ).get('_')

# 计划任务命令
cmd = 'cd {0} && {1} {2}/{3}'.format(comm_path, install_path, check_path, run_file)


# 创建当前用户的计划任务
my_user_cron = CronTab(user=True)
# 创建任务
job_1 = my_user_cron.new(command='{}'.format(cmd))
# 设置任务执行周期，每天18执行一次
job_1.setall('* 18 * * *')
# 启动任务
job_1.enable()
# 写入配置文件
try:
    my_user_cron.write()
    logger.info("添加任务成功：[{}]".format(cmd))
except Exception as err:
    logger.error("添加任务失败：[{}]".format(cmd))