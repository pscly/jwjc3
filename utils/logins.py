import os, requests, re
from time import strftime

# 登录加密算法
def login_str(s1:str) -> str:
    if not isinstance(s1, str):
        raise TypeError('s1 不是字符串')
    s2 = ''  # 返回的字符串
    for i in s1:
        s2 += str(100000+ord(i))
    return s2


def get_login_cookies(xh:str, pwd:str, config:dict):
    """

    args:
        xh: 学号
        pwd: 密码
        config: 配置文件

    return: [{'cookies':'xx'}, {'user':'xx','date':'当前时间'}], 1
    return: [], 0
    """
    # config = os.environ['CONFIG']
    dl_url = config['JWJC_URL'] + "/web/web/web/index?pmkd=1920&pmgd=441"
    dl_post_url = config['JWJC_URL'] + "/jiaoshi/bangong/main/check"
    headers = config['HEADERS']
    re_shouye_name = '>(.*?),欢迎您!<'

    zb1 = requests.get(dl_url, headers=headers)
    zb2 = requests.post(dl_post_url, data={
        'user': xh,
        'pwd': '',
        'user1': login_str(xh),
        'pwd1': login_str(pwd),
    }, headers=headers, cookies=zb1.cookies.get_dict())

    zb2.encoding = 'gbk'
    if not (x1 := re.findall(re_shouye_name, zb2.text)):
        return {}, 0
    return [zb2.cookies.get_dict(), {'name': x1[0], 'date':strftime("%Y-%m-%d")}], 1



if __name__ == '__main__':
    print(login_str('abc'))
    get_login_cookies('202040030804', 'cly12345', {'JWJC_URL': 'http://jwjc.scstc.cn', 'HEADERS': {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}})
