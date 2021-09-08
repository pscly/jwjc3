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
BANJI_MAX = 10  # 最多个班级
MAX_REN = 50    # 一个班级最大人数
PWD = '123456'
config = core.load_config_yaml(mode='WAI')

def get_user(start):
    '''
    202040030101    # 最后的01在这里进行拼接(也就是这个人在班级里的学号)
    start: 2020400301
    '''
    is_you = 0
    for i in range(1, MAX_REN+1):
        if i == 21 and is_you == 0:
            return 2    # 这个班级没人,后面就不用跑了
        try:
            x = logins.get_login_cookies(start*100+i, PWD, config)
            if not x[-1]:
                continue
            is_you = 1
            res = x[0]
            users.get_uesr_info(res)
            view_funcs.xueqi_xuanze(res, 0)
            kb.get_kebiao(res)
        except Exception as e:
            print(e)
            continue
    return 1

def get_zhuanye(xh:int):
    """
    给前面几位, 后面的自动补充
    202040030101
    xh: 20204003
    """
    x = 0
    for i in range(1, BANJI_MAX+1):
        if i > 5 and x2 == 2:
            return 2
        x2 = get_user(xh*100+i)
        if x2:
            x = x2

    return 1
            

def get_yuan1(xh:int):
    """
    给前面几位, 后面的自动补充
    202040030101
    xh: 202040
    """
    x = 0
    for i in range(1, BANJI_MAX+1):
        if i > 5 and x == 2:
            return 0
        x2 = get_zhuanye(xh*100+i)
        if x2:
            x = x2
        
    return 1


if __name__ == '__main__':
    # print(get_user(202040090101))
    print(get_user(2020402102))
    # print(get_yuan1(202040))
    # print(get_yuan1(202040030422))
    
