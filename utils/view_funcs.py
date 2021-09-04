import sys
import requests
import re
sys.path.append("..")


from utils.core import MyRes

def xueqi_xuanze(res_obj: MyRes, xueqi:int):
    '''
    xueqi: int 你要选择的学期序号(从0开始) 这学期是0, 上学期是1, 上上是2
    '''
    # 获取学期
    xq = res_obj.get_res(
        '/jiaoshi/xslm/gongxuan/note', 
        r'align="?center"? ?>([\d]*-[\d]*-\d)</t.*?main.xueqi=(.*?)">选择</a>'
        ) 
    if not xq[-1]:
        return '失败', None
    xq = xq[-1]     # [('2021-2022-1', '学期号'), ('2020-2021-2', '学期号')]

    # 选择学期
    xq1 = xq[xueqi]   
    res_obj.xueqi = xq1[0]
    res_obj.get_res('/jiaoshi/xslm/gongxuan/main', params={'xueqi': xq1[1]})
