#/usr/bin/env python
#coding=utf-8

import thread
import time

def f(name):
    print "this is " + name

if __name__ == '__main__':
    for i in range(1,10):
        thread.start_new_thread(f, (str(i),))
    time.sleep(5)
