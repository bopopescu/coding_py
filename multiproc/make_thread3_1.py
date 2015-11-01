#/usr/bin/env python
#coding=utf-8

import threading
import time

class Th(threading.Thread):
    def __init__(self, thread_name):
        threading.Thread.__init__(self)
        self.setName(thread_name)
    def run(self):
        #threadLock.acquire()
        print "This is thread " + self.getName()
        for i in range(5):
            #time.sleep(1)
            print str(i)
        print self.getName() + " is over"
        #threadLock.release()
if __name__ == '__main__':
    threadLock = threading.Lock()
    thread1 = Th('T1')
    thread2 = Th('T2')
    thread3 = Th('T3')
    thread1.start()
    thread2.start()
    thread3.start()
    #thread1.join()
    print "main thread is over"
