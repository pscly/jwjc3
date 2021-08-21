import os

def get_uesr_info(cookie, config):
    """
    获取用户详细信息
    """
    info_url = f'{config.get("JWJC_URL")}/jiaoshi/xslm/info/bjiben'
    re_text = '<td *class=g_body *align=center *>(.*?)</td>'
    
