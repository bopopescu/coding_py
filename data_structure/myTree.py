#!/usr/bin/env python
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

    def setLeftChild(self, new_tree):
        self.left_child = new_tree

    def setRightChild(self, new_tree):
        self.right_child = new_tree

    def setValue(self, val):
        self.data = val

class BinaryTree:
    def __init__(self, root):
        self.root = ChildTree(root)

    def insert_left(self, new_node):
        if self.left_child == None:
            self.left_child == ChildTree(new_node)
        else:
            tmp = ChildTree(new_node)
            tmp.setLeftChild(self.root.getLeftChild())
            self.root.setLeftChild(tmp)

    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child == ChildTree(new_node)
        else:
            tmp = ChildTree(new_node)
            tmp.setRightChild(self.root.getRightChild())
            self.root.setRightChild(tmp)

