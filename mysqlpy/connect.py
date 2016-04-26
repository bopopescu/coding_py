#!/usr/bin/env python
#conding=utf-8


#import MySQLdb
import sys
import os.path
ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.extend([ROOT_PATH])

from conf.local_config import DB_HOST, DB_PORT, DB_USER, DB_PASSWD, DB_NAME
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

# def return_db_handle():
#    return MySQLdb.connect(DB_HOST, DB_USER, DB_PASSWD, "mytest")

DEFAULT_READ_TIMEOUT = 10
DEBUG = True


def make_engine(host, port, user, passwd, dbname, **kws):

    engine = 'mysql+mysqlconnector'
    options = {}
    options['connect_timeout'] = 1

    return create_engine(
        '%s://%s:%s@%s:%s/%s?charset=utf8&use_unicode=1' % (engine, user, passwd, host, port, dbname),
        pool_size=2,
        max_overflow=-1,
        pool_recycle=120,
        echo=DEBUG,
        connect_args=options,
        **kws
    )


def make_sql_engine():
    engine = make_engine(DB_HOST, int(DB_PORT), DB_USER, DB_PASSWD, DB_NAME)
    return engine


def make_sqlalchemy_db_read_handle(engine):
    Session = scoped_session(sessionmaker())
    Session.configure(bind=engine, autocommit=True, autoflush=True, expire_on_commit=True)

    return Session

def make_sqlalchemy_db_write_handle(engine):
    Session = scoped_session(sessionmaker())
    Session.configure(bind=engine, autocommit=False, autoflush=False, expire_on_commit=False)

    return Session



if __name__ == '__main__':
    #db = return_db_handle()
    #cursor = db.cursor()
    #cursor.execute("SELECT VERSION()")
    #data = cursor.fetchone()
    #print "Database version: %s" % data
    #db.close()
    engine = make_sql_engine()
    # db_handle = sqlalchemy_db_handle(engine)
    # print(db_handle.query)
