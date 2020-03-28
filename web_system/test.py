import os
import yaml
import settings

# conf file path
CONF_PATH = os.path.join(settings.BASE_DIR, "conf", "init.yaml")
with open(CONF_PATH, 'r', encoding='utf-8') as conffile:
    INFO = yaml.load(conffile, Loader=yaml.FullLoader)


debug = INFO['debug']
print(debug)