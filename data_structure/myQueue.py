#!/usr/bin/env python3
#coding=utf-8

import queue
import time

class myQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def put(self, item):
        self.items.append(item)
        
    def get(self):
        if self.is_empty():
            return 0
        return self.items.pop(self.items[0])

    def getSize(self):
        return len(self.items)

if __name__ == '__main__':
    n = 10000
    atime = time.time()
    q1 = myQueue()
    for i in range(n):
        q1.put(i)

    print(q1.getSize())
    btime = time.time()
    print("myQueue:")
    print(btime - atime)

    atime = time.time()
    q2 = queue.Queue()

    for i in range(n):
        q2.put(i)

    print(q2.qsize())
    btime = time.time()
    print("CPython queue:")
    print(btime - atime)

