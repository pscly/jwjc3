import os
import time
from utils import core
import re

def get_kebiao(res_obj:core.MyRes, save_html=True):
    """
    save_html: 是否保存课表html到本地
    """
    kburl = '/jiaoshi/xslm/gongxuan/kbbanji'
    res_obj.get_res(kburl, '.*')

    if save_html:
        if not os.path.isdir('kebiao'): # 保存路径
            os.mkdir('kebiao')
        # 保存课程表网页
        with open('kebiao/' + res_obj.xueqi + res_obj.name + time.strftime('%Y-%m-%d') +'.html', 'w') as f:
            f.write(res_obj.text)

    return res_obj, res_obj.text
