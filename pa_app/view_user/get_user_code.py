
# 获取男女比例等


from sqlalchemy.sql.functions import user
from entities.models import Users
from entities.db_mysql import db




def get_ban_user_xb(cx, xb=0):
    """
    获取班级男女比例
    :return:
    """

    if xb:
        users = db.session.query(Users).filter(
            Users.banji == cx,
            Users.gender == xb).all()
    else:
        users = db.session.query(Users).filter(Users.banji == cx).all()
    return users

def get_zhuanye_user_xb(cx,xb=''):
    """
    获取班级男女比例
    :return:
    """

    if xb:
        users = db.session.query(Users).filter(
            Users.zhuanye == cx,
            Users.gender == xb).all()
    else:
        users = db.session.query(Users).filter(Users.zhuanye == cx).all()
    return users

def get_yuan_user_xb(cx, xb=0):
    """
    获取班级男女比例
    :return:
    """
    if xb:
        users = db.session.query(Users).filter(
            Users.xueyuan == cx,
            Users.gender == xb).all()
    else:
        users = db.session.query(Users).filter(Users.xueyuan == cx).all()
    return users

