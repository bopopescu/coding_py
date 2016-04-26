#!/usr/bin/env python3
#coding=utf-8

from sqlalchemy import Column
from sqlalchemy import Integer, String
from sqlalchemy.dialects.mysql import VARCHAR
from mysqlpy.connect import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    age = Column(Integer)
    password = Column(String(50))


class InviteCodeModel(Base):
    __tablename__ = 'tbl_invite_code'

    id = Column(Integer, primary_key=True)
    key = Column(String(40))
    user_id = Column(Integer)