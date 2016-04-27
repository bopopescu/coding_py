#!/usr/bin/env python3
#conding=utf-8

import random, string
import sys
import os.path
ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.extend([ROOT_PATH])
from mysqlpy.connect import make_sqlalchemy_db_write_handle,make_sqlalchemy_db_read_handle ,make_sql_engine, Base
from mysqlpy.model.mytest import User, InviteCodeModel


class InviteCode:
    
    def __init__(self, code_length):
        self.code_length = code_length

    def generate_code(self):
        string_list = [i for i in (string.ascii_letters + string.digits)]
        
        self.invite_code = InviteCodeModel(key=''.join([random.choice(string_list) for i in range(self.code_length)]))

    def get_invite_code(self):
        return self.invite_code

    def init_mysql_read_session(self):
        engine = make_sql_engine()
        self.r_Session = make_sqlalchemy_db_read_handle(engine)

    def init_mysql_write_session(self):
        engine = make_sql_engine()
        self.w_Session = make_sqlalchemy_db_write_handle(engine)
        Base.metadata.create_all(engine)

    def save_to_mysql(self):
        if self.invite_code:
            try:
                self.w_Session.add(self.invite_code)
            except Exception as e:
                self.w_Session.rollback()
            finally:
                self.w_Session.commit()
        else:
            return "Pleas generate a invite code"

    def distribute_code_to_user(self, user_id, invite_code_id=None):
        try:
            if not invite_code_id and self.invite_code:
                self.w_Session.query(InviteCodeModel).\
                    filter(InviteCodeModel.key == self.invite_code).\
                    update({'user_id': user_id})
            elif invite_code_id:
                self.w_Session.query(InviteCodeModel). \
                    filter(InviteCodeModel.id == invite_code_id). \
                    update({'user_id': user_id})
        except:
            self.w_Session.rollback()
        finally:
            self.w_Session.commit()

    def close(self):
        self.w_Session.remove()
        self.r_Session.remove()



if __name__ == "__main__":
    a = InviteCode(12)
    print(a.generate_code())
    a.init_mysql_read_session()
    a.init_mysql_write_session()
    a.distribute_code_to_user(user_id=1, invite_code_id=1)
    # a.save_to_mysql()
    a.close()
    # a.create_user_obj()
    # a.test_save_handle()

