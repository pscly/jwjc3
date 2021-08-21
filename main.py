import os
import requests
import re
import yaml
from utils import logins, core
from pa_app.view_user.update_pwd import update_pwd

config = core.load_config_yaml(mode='WAI')  # WAI 是外网访问，NEI 是内网访问， 默认外网(参考配置文件)

# x = logins.get_login_cookies('202040030804','yyqq12',config)
# print(x)
# x = update_pwd('yyqq12', 'yyqq12', config, cookies=x[0][0])    # 其实可以吧x封装成类，然后在里面判断
x = update_pwd('yyqq12', 'yyqq12', config, xh='202040030804')    # 其实可以吧x封装成类，然后在里面判断

print(x)

