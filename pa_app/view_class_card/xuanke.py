
import os, requests, re
from time import strftime
from utils import view_funcs
from utils.core import MyRes
from addict import Dict
from pa_app.view_class_card import xuankejiexi



def xuanke(res:MyRes, xk):
    '''
    选课

    res: MyRes 对象
    xk: 你要选择的课程名称
    '''
    r_data = Dict()
    url1 = '/jiaoshi/xslm/gongxuan/kai'
    re1 = r'<a ?class="?one"? ?href=.(.*?). ?title="?请点击进入"?><span class="?fcolor?">公共选修课</span>'

    _, url2 = res.get_res(url1, re1)
    if not url2:
        print('选课失败')
        return
    url2 = res.get_res('jiaoshi/xslm/gongxuan/' + url2[0])

    kc_dic: Dict = xuankejiexi.xuanke_jx(res.text)
    
    if xk not in kc_dic.keys():
        print('没有这门课程')
        return
    res.get_res('jiaoshi/xslm/gongxuan/' + kc_dic[xk]['选课'])
