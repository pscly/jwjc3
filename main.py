import os
import requests
import re
import yaml, json
from utils import logins, core
from pa_app.view_user.update_pwd import update_pwd
from pa_app.view_funcs import login_view


config = core.load_config_yaml(mode='WAI')  # WAI 是外网访问，NEI 是内网访问， 默认外网(参考配置文件)


if __name__ == '__main__':
    # login_view(config)


    x = logins.get_login_cookies('202040030804','abcd123',config)
    print(x)
    if x[-1]:
        print('登录成功')
    else:
        print('登录失败')
    # x = update_pwd('yyqq12', 'yyqq12', config, cookies=x[0][0])    # 其实可以吧x封装成类，然后在里面判断
    # x = update_pwd('yyqq12', 'yyqq12', config, xh='202040030804')    # 其实可以吧x封装成类，然后在里面判断


