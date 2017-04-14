#!/usr/bin/env python3
#coding=utf-8

from sqlalchemy import Column, ForeignKey
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
    user = rela


class Parent(Base):
    __tablename__ = "parent"
    id = Column(Integer, Primary_key=True)
    name = Column(CHAR(50))
    child = relationship("child", backref="parent")


class Child(Base):
    __tablename__ = "child"
    id = Column(Integer, Primary_key=True)
    name = Column(CHAR(50))
    parent_id = Column(Integer,ForeignKey('parent.id'))

