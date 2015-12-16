#!/usr/bin/env python
#coding=utf-8

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return 0
        return self.items.pop()

    def getPeek(self):
        return self.items[len(self.items) - 1]

    def getSize(self):
        return len(self.items)


if __name__ == '__main__':
    s = Stack()

    for i in range(10):
        s.push(i)

    print("stack peek:")
    print(s.getPeek())
    print("stack size:")
    print(s.getSize())

    for i in range(10):
        print("pop %d" % s.pop())

    print(".....After pop.....")
    #print("stack peek:")
    #print(s.getPeek())
    print("stack size:")
    print(s.getSize())


