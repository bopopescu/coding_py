#!/usr/bin/env python
#coding=utf-8


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    def getNext(self):
        return self.next

    def setNext(self, item):
        self.next = item

    def getPrev(self):
        return self.prev

    def setPrev(self, item):
        self.prev = item

class LinkList:
    def __init__(self):
        self.head = Node(None)

    def add(self, item):
        tmp = Node(item)
        tmp.setPrev(self.head)
        self.head.setNext(tmp)
        self.head = tmp

    def getLength(self):
        self.cur = self.head
        count = 0
        while self.cur.getPrev() != None:
            count += 1
            self.cur = self.cur.getPrev()

        print("\nthe length of list is %d" % count)

    def print_list(self):
        self.cur = self.head
        while self.cur.getPrev() != None:
            print(self.cur.data, end = ' ')
            self.cur = self.cur.getPrev()
            


if __name__ == '__main__':
    l = LinkList()
    for i in range(10):
        l.add(str(i))
    l.print_list()
    l.getLength()
