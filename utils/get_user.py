# 获取一个区间内的学号,然后信息, 然后入库
from utils import core
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import logins, core

# xh = 202040030101

YEAR = 2021
XUE_2 = 4
MAX_REN = 50    # 最大人数
PWD = '123456'
config = core.load_config_yaml(mode='WAI')

def get_user(start):
    for i in range(start, start+MAX_REN):
        x = logins.get_login_cookies(start, PWD, config)
        if not x[-1]:
            continue
        
            


if __name__ == '__main__':
    print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
