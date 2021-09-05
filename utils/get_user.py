# 获取一个区间内的学号,然后信息, 然后入库
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import core
import datetime, time
from utils import logins, core, users, kb
from pa_app.view_user.update_pwd import update_pwd
from pa_app.view_funcs import login_view
from utils import view_funcs
from pa_app.view_class_card import crad

# xh = 202040030101

YEAR = 2021
XUE_2 = 4
MAX_REN = 50    # 最大人数
PWD = '123456'
config = core.load_config_yaml(mode='WAI')

def get_user(start):
    for i in range(start, start+MAX_REN):
        try:
            x = logins.get_login_cookies(i, PWD, config)
            if not x[-1]:
                continue
            res = x[0]
            users.get_uesr_info(res)
            view_funcs.xueqi_xuanze(res, 1)
            kb.get_kebiao(res)
        except Exception as e:
            print(e)
            continue


if __name__ == '__main__':
    print(get_user(202040030101))
