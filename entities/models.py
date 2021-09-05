import datetime
from sqlalchemy import create_engine    # 连接引擎
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index

Base = declarative_base()   # 创建表的models， django是models.Models
# Base = declarative_base()   # 创建表的models

class Users(Base):
    __tablename__ = 'users'  # 数据库表名称
    code = Column(String(255), primary_key=True)
    pwd = Column(String(32))
    name = Column(String(32))
    gender = Column(Integer)
    zhuanye = Column(String(32))
    xueyuan = Column(String(32))
    lianji = Column(Integer)
    sfz = Column(String(32))
    phone = Column(String(32))
    create_time = Column(DateTime, default=datetime.datetime.now)

