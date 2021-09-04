import os
import requests
import re
import yaml, json
from utils import logins, core, users, kb
from pa_app.view_user.update_pwd import update_pwd
from pa_app.view_funcs import login_view
from utils import view_funcs


config = core.load_config_yaml(mode='WAI')  # WAI 是外网访问，NEI 是内网访问， 默认外网(参考配置文件)


if __name__ == '__main__':
    # login_view(config)


    x = logins.get_login_cookies('202040030804','xxx',config)
    print(x)
    if x[-1]:
        print('登录成功')
        res, user_info = users.get_uesr_info(x[0][0])
        print(user_info)

        view_funcs.xueqi_xuanze(res, 1)
        kb1 = kb.get_kebiao(res)
        print(kb1)
        # 保存网页
        with open(res.xueqi+x[0][1]['name']+'.html', 'w') as f:
            f.write(kb1[-1])
        

    else:
        print('登录失败')
    # x = update_pwd('yyqq12', 'yyqq12', config, cookies=x[0][0])    # 其实可以吧x封装成类，然后在里面判断
    # x = update_pwd('yyqq12', 'yyqq12', config, xh='202040030804')    # 其实可以吧x封装成类，然后在里面判断


