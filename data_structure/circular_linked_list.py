#!/usr/bin/env pyhton
#coding=utf-8
import pdb
import time



class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def setData(self, newData):
        self.data = newData

    def getNext(self):
        return self.next

    def setNext(self, nextNode):
        self.next = nextNode

class CircularLinkedList:
    def __init__(self):
        self.head = ListNode(None)
        self.head.setNext(self.head)

    def getHead(self):
        return self.head

    def isEmpty(self):
        return self.head.getNext() is None

    def add(self, item):
        tmp = ListNode(item)
        tmp.setNext(self.head.getNext())
        self.head.setNext(tmp)

    def remove(self, item):
        prevNode = self.head
        while prevNode.getNext() != self.head:
            curNode = prevNode.getNext()
            if curNode.data == item:
                prevNode.setNext(curNode.getNext())
            prevNode = prevNode.getNext()

    def search(self, item):
        curNode = self.head.getNext()
        while curNode != self.head:
            if curNode.data == item:
                print('found')
                return True
        return False





    def printList(self):
        curNode = self.head.getNext()
        while curNode != self.head:
            print(curNode.getData())
            curNode = curNode.getNext()



if __name__ == '__main__':
    LinkedList = CircularLinkedList()
    count = 10
    tmp = []
    atime = time.time()
    for i in range(count):
        LinkedList.add(i)
    btime = time.time()
    print(btime - atime)
    atime = time.time()
    [ i for i in range(count)]
    btime = time.time()
    print(btime - atime)
    atime = time.time()
    for i in range(count):
        tmp.append(i) 
    btime = time.time()
    print(btime - atime)
    #LinkedList.printList()
