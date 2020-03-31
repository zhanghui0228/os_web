import os
from web_system import settings


module = ['python-crontab', 'logzero', 'pyyaml']
bin_path = os.path.join(settings.BASE_DIR, 'bin')

for m in range(len(module)):
    os.popen("pip3 install {}".format(module[m]))

run_cron = "python3 {}/cron.py".format(bin_path)
os.popen(run_cron)