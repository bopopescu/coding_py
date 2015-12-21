#!/usr/bin/env python3
#coding=utf-8

class ChildTree:
    def __init__(self, val):
        self.data = val
        self.left_child = None
        self.right_child = None

    def getLeftChild(self):
        return self.left_child

    def getRightChild(self):
        return self.right_child

    def getValue(self):
        return self.data

    def setLeftChild(self):
        self.left_child = ChildTree(None)
        return self.left_child

    def setRightChild(self):
        self.right_child = ChildTree(None)
        return self.right_child

    def setValue(self, val):
        self.data = val

class BinaryTree:
    def __init__(self, root):
        self.root = ChildTree(root)

    def createTree(self, node):
        if node == self.root:
            print("Now set root value,")
        val = input("please input node value:")
        if val != '0':
            print('=============================')
            node.setValue(val)
            print("Now insert left node,")
            self.createTree(node.setLeftChild())
            print("Now insert right node,")
            self.createTree(node.setRightChild())
        else:
            print("/------skip this node------/")


    def insert_left(self, new_node):
        if self.root.left_child == None:
            self.root.left_child = ChildTree(new_node)
        else:
            tmp = ChildTree(new_node)
            tmp.setLeftChild(self.root.getLeftChild())
            self.root.setLeftChild(tmp)

    def insert_right(self, new_node):
        if self.root.right_child == None:
            self.root.right_child = ChildTree(new_node)
        else:
            tmp = ChildTree(new_node)
            tmp.setRightChild(self.root.getRightChild())
            self.root.setRightChild(tmp)

if __name__ == '__main__':
    bt = BinaryTree(24)
    bt.createTree(bt.root)
    print(bt.root.getLeftChild().getValue())
    print(bt.root.getRightChild().getValue())
