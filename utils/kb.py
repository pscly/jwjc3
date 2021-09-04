from utils import core
import re

def get_kebiao(res_obj:core.MyRes):
    """
    
    """
    kburl = '/jiaoshi/xslm/gongxuan/kbbanji'
    res_obj.get_res(kburl, '.*')
    return res_obj, res_obj.text
