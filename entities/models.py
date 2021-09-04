import datetime, sys
sys.path('..')
from sqlalchemy import create_engine    # 连接引擎
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index
from utils.core import load_config_yaml


Base = declarative_base()   # 创建表的models， django是models.Models

config = load_config_yaml()

def init_db():
    engine = create_engine(
    config['DB'],
    )


