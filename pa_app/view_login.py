import os
from utils import logins


def login_view(xh, pwd, config):
    """
    登录
    """
    u1 = logins.get_login_cookies(xh, pwd, config)
    if u1[1]:
        return u1

