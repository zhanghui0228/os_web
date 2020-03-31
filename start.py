import os
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

Pid = "ps -elf|grep 'manage.py'|grep -v grep|awk '{print $4}'"

# 安装模块依赖，初始化环境
module = "bash {}/init.sh".format(settings.BASE_DIR)
logger.debug(os.popen(module))

# 启动命令
start = "echo {0} >log/jenkins_work.log && nohup python3 {1}/manage.py runserver 0.0.0.0:9000 >>log/jenkins_work.log&".format(now_time, settings.BASE_DIR)
lines_pid = os.popen(Pid)

# kill process id
for i in lines_pid:
    i = i.strip('\n')
    logger.info(os.popen("kill -9 {}".format(i)))

# start project
local_info = os.popen(start)
logger.info(local_info)
