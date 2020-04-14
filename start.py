import os
import yaml
from datetime import datetime
from logzero import logfile, logger
from web_system import settings


log_path = os.path.join(settings.BASE_DIR, "log") 
run_log = os.path.join(log_path, "run.log")
# now time
now_time = datetime.now()
try:
    if os.path.exists(log_path) == False:
        os.mkdir(log_path)
except Exception as err:
    print("创建日志目录失败,错误原因：{}".format(err))

logfile(run_log, maxBytes=3000000, backupCount=2, encoding="utf-8")

# 获取启动端口
init_file = 'conf/init.yaml'
with open(init_file, 'r', encoding='utf-8') as file:
    info_list = yaml.load(file, Loader=yaml.FullLoader)

# start port
port = info_list['server_port']

Pid = "ps -elf|grep 'manage.py'|grep -v grep|grep {port}|awk '{{print $4}}'".format(port=port)

# 启动命令
start = "echo {0} >log/jenkins_work.log && nohup python3 {1}/manage.py runserver 0.0.0.0:{2} >>log/jenkins_work.log&".format(now_time, settings.BASE_DIR, port)
lines_pid = os.popen(Pid)

# kill process id
for i in lines_pid:
    i = i.strip('\n')
    logger.info(os.popen("kill -9 {}".format(i)))

# start project
local_info = os.popen(start)
logger.info(local_info)