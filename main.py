import os
import requests
import re
import yaml, json
import datetime, time
from utils import logins, core, users, kb
from pa_app.view_user.update_pwd import update_pwd
from pa_app.view_funcs import login_view
from utils import view_funcs
from pa_app.view_class_card import crad


config = core.load_config_yaml(mode='WAI')  # WAI 是外网访问，NEI 是内网访问， 默认外网(参考配置文件)


if __name__ == '__main__':
    x = logins.get_login_cookies('202040030713','123456',config)
    print(x)
    if x[-1]:
        print('登录成功')
        res, user_info = users.get_uesr_info(x[0])
        print('>>>',user_info,'<<<')

        view_funcs.xueqi_xuanze(res, 1)
        kb1 = kb.get_kebiao(res)
        print(kb1)

    else:
        print('登录失败')


