#!/usr/binpython

import MySQLdb

db = MySQLdb.connect("localhost", "mysql", "root", "123qwe")

cursor = db.cursor()
