module = ['python-crontab', 'logzero', 'pyyaml']

# 添加任务计划,项目根目录下执行
python3 web_system/cron.py


# 执行检查脚本（巡检），项目根目录下执行
python3 web_system/check.py