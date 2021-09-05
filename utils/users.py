import os
from entities.models import Users
from entities.db_mysql import db
from utils import core

def get_uesr_info(res1, to_db=1):
# def get_uesr_info(res1, db_session=None):
    """
    获取用户详细信息, 并且保存到数据库
    res1: Core里面的对象
    to_db: 是否保存到数据库, 1是保存，0不保存

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
    if to_db:
        # 将用户信息保存到数据库
        if not (user_obj := db.session.query(Users).filter(Users.code == user_info_dic['学号']).first()):
            user_obj = Users()

        user_obj.code = user_info_dic['学号'],
        user_obj.name = user_info_dic['姓名'],
        user_obj.pwd = res1.pwd,
        user_obj.gender = 2 if user_info_dic['性别'] == '男' else 1,
        user_obj.zhuanye = user_info_dic['专业'],
        user_obj.xueyuan = user_info_dic['系部'],
        user_obj.lianji = user_info_dic['年级'],
        user_obj.sfz = user_info_dic['身份证']

        db.session.add(user_obj)
        db.session.commit()

    return res1, user_info_dic
