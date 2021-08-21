import os
import requests
from utils.logins import get_login_cookies
from utils.core import MyRes

def update_pwd(old_pwd, new_pwd, config, xh="", cookies={}):
    """
    修改密码
    """

    # 如果没有cookies，则登录一下，获取cookies
    if not cookies:
        if not xh:
            return "没学号,也不传cookies，我怎么进?", 0 
        dl = get_login_cookies(xh, old_pwd, config)
        if not dl[1]:
            return "旧密码错误，请重新登录", 0
        cookies = dl[0][0]
        
    if not cookies:
        return "登录失败", 0


    url = 'jiaoshi/bangong/mima/changepwd1'
    res1 = MyRes(config, config['HEADERS'], cookies)
    res1.get_res('jiaoshi/bangong/mima/changepwd')
    data = {
        'password0': old_pwd,
        'password1': new_pwd,
        'password2': new_pwd,
        'submit1': '%C8%B7%C8%CF'   # 确认的url编码(gb2312)
    }
    print(data)
    re1 = r'<form ?name="?msn"? ?action="?javascript:window.history.go\(-1\)"? method="?post"?>(.*?)<'
    x = res1.post_res(url, data, re1)
    return x
