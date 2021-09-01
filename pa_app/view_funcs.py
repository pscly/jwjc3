import os
from utils import logins
from pa_app.view_user import update_pwd


def login_view(xh, pwd, config):
    """
    登录
    """
    u1 = logins.get_login_cookies(xh, pwd, config)
    if u1[1]:
        return u1

def up_pwd(old_pwd, new_pwd, config):
    """
    修改密码
    """
    pass
