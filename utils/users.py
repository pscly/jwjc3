import os

from utils import core

def get_uesr_info(res1):
    """
    获取用户详细信息
    return res1, {}
    return res1, False
    """
    info_url = '/jiaoshi/xslm/info/bjiben'
    re_text = '<td *class=g_body *align=center *>(.*?)</td>'

    # res1 = core.MyRes(config, config.get('HEADERS'), cookies)
    user_info = res1.get_res(info_url, re_text)[-1]
    if not user_info:
        print('获取用户信息失败')
        return False
    user_info_dic = {
        '年级': user_info[0],
        '班级': user_info[1],
        '学号': user_info[2],
        '姓名': user_info[3],
        '性别': user_info[4],
        '身份证': user_info[5],
        '专业': user_info[7],
        '系部': user_info[9],
    }
    return res1, user_info_dic
