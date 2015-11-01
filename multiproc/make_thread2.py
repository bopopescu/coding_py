#/usr/bin/env python
#coding=utf-8

import threading
import time

class Th(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.t_name = name
    def run(self):
        print "This is " + self.t_name

if __name__ == '__main__':
    for i in range(9):
        thread1 = Th("Thread" + str(i))
        thread1.start()
    time.sleep(2)
