# 获取男女比例等


from entities.models import Users
from entities.db_mysql import db


def r_renshu(users):
    """
    返回男的和女的总人数
    """
    nv = 0
    nan = 0
    for user in users:
        if user.gender == 1:
            nan += 1
        else:
            nv += 1
    return nan, nv


def get_ban_user_xb(cx):
    """
    获取班级男女比例
    :return:
    """
    users = db.session.query(Users).filter(Users.banji == cx).all()
    return r_renshu(users)

def get_zhuanye_user_xb(cx):
    """
    获取班级男女比例
    :return:
    """
    users = db.session.query(Users).filter(Users.zhuanye == cx).all()
    return r_renshu(users)

def get_yuan_user_xb(cx):
    """
    获取班级男女比例
    :return:
    """
    users = db.session.query(Users).filter(Users.xueyuan == cx).all()
    return r_renshu(users)

