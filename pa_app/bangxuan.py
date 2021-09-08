from entities.models import Users
from entities.db_mysql import db


def get_user_by_gender(gender:int):
    '''
    gender : 1 是男, 2 是女
    '''
    users = db.session.query(Users).filter(Users.gender == 2).all()
    return [i.code for i in users]
