import os
import requests
import re
import yaml
from utils import logins, core

config = core.load_config_yaml(mode='WAI')  # WAI 是外网访问，NEI 是内网访问， 默认外网(参考配置文件)

os.environ['JWJC_URL'] = config['JWJC_URL']

x = logins.get_login_cookies('202040030804','cly12345',config)


print(x)

