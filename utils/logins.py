import os, requests, re
from time import strftime
from utils.core import MyRes

# 登录加密算法
def login_str(s1:str) -> str:
    s1 = str(s1)
    s2 = ''  # 返回的字符串
    for i in s1:
        s2 += str(100000+ord(i))
    return s2


def get_login_cookies(xh:str, pwd:str, config:dict):
    """

    判断是否登录成功:
    x = get_login_cookies(...)
    if x[-1]:
        登录成功
    else:
        登录失败
        
    args:
        xh: 学号
        pwd: 密码
        config: 配置文件

    return: [res_obj, {'user':'xx','date':'当前时间'}], 1
    return: [], 0
    """
    headers = config['HEADERS']
    re_shouye_name = '>(.*?),欢迎您!<'

    res1 = MyRes(config, headers=headers)
    res1.get_res("web/web/web/index?pmkd=1920&pmgd=441")
    x = res1.post_res("jiaoshi/bangong/main/check", data={
        'user': xh,
        'pwd': '',
        'user1': login_str(xh),
        'pwd1': login_str(pwd),
    },re_text=re_shouye_name)

    if not (x1 := re.findall(re_shouye_name, x[0].text)):
        print(xh, '登录失败')
        return res1, 0
    print(xh, '登录成功')
    res1.xh = xh
    res1.pwd = pwd
    res1.name = x1[0]
    return res1, 1


if __name__ == '__main__':
    print(login_str('abc'))
    get_login_cookies('202040030804', 'yyyccc12', {'JWJC_URL': 'http://jwjc.scstc.cn', 'HEADERS': {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}})
