import os
import requests
import re
import yaml, json
import datetime, time
from utils import logins, core, users, kb
from pa_app.view_user.update_pwd import update_pwd
from pa_app.view_funcs import login_view
# from utils import view_funcs
from pa_app.view_class_card import crad
from pa_app.view_class_card import xuanke
from pa_app.bangxuan import get_user_by_gender
from pa_app.view_user import get_user_code

config = core.load_config_yaml(mode='WAI')  # WAI 是外网访问，NEI 是内网访问， 默认外网(参考配置文件)


if __name__ == '__main__':
    # x = logins.get_login_cookies('202040030713','123456',config)
    # print(x)
    # if x[-1]:
    #     print('登录成功')
    #     # res, user_info = users.get_uesr_info(x[0])
    #     # print('>>>',user_info,'<<<')

    #     xuanke.xuanke(x[0], '孙子兵法中的思维智慧')

    #     # view_funcs.xueqi_xuanze(res, 0)
    #     # kb1 = kb.get_kebiao(res)
    #     # print(kb1)

    # else:
    #     print('登录失败')

    # x = get_user_by_gender(2)
    # print(x)
    # print(len(x))
    # for i in x:
    #     logins.get_login_cookies(i,'123456',config)
    #     xuanke.xuanke(x[0], '孙子兵法中的思维智慧')
    
    # x = get_user_xb.get_yuan_user_xb('蓝盾网络空间安全学院')
    # x = get_user_code.get_yuan_user_xb('幼儿师范学院', 2)
    # for i in x:
    #     print(i)
    #     x = logins.get_login_cookies(i.code,'123456',config)
    #     xuanke.xuanke(x[0], '孙子兵法中的思维智慧')
    ...
    

