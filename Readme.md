module = ['python-crontab', 'logzero', 'pyyaml', 'pymysql', 'psutil']

# 项目初始化配置信息    --- conf/init.yaml

# 项目启动
python3 start.py

# 添加任务计划,项目根目录下执行 --暂时不可用
python3 web_system/cron.py


# 检查脚本（巡检）  --- web_system/check_site.py
# 钉钉机器人通知    --- web_system/message.py
# 基础环境检查      --- web_system/check_option.py
# 健康检查          --- web_system/check_healthy.py