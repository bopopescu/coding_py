#!/usr/bin/env python3
#coding=utf-8

class myDeque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def addFront(self, item):
        return self.items.append(item)

    def addRear(self, item):
        return self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def getSize(self):
        return len(self.items)


if __name__ == '__main__':
    dq = myDeque()
    dq.addFront('hello')
    dq.addFront('nihao')
    dq.addRear('你好')

    print(dq.removeFront())
    print(dq.removeRear())
    print(dq.getSize())
