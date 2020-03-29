import os
from web_system import settings


Pid = "ps -elf|grep 'manage.py'|grep -v grep|awk '{print $4}'"
# 启动命令
start = "nohup python3 {0}/manage.py runserver 0.0.0.0:9000 >>{1}/log/run.log &".format(settings.BASE_DIR, settings.BASE_DIR)
lines_pid = os.popen(Pid)

print (list(lines_pid))
# kill process id
for i in lines_pid:
    i = i.strip('\n')
    os.popen("kill -9 {}".format(i))

# start project
os.popen(start)