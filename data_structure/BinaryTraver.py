#!/usr/bin/env python
#coding=utf-8

from myTree import BinaryTree

def preorder_traverse(binary_tree):
    reslut = []
    parent_stack = []
    if binary_tree.root:
        node = binary_tree.root
        while node:
            result.append(node.getValue())
            parent_stack.append(node)
            node = node.getLeftChild() 
            if not node:
                while not node:
                    node = parent_stack.pop()
                    node = node.getRightChild()

    return reslut


bt = BinaryTree(24)
bt.insert_left(15)
#print(bt.root.getLeftChild())
#bt.root.getLeftChild().insert_left(4)
#bt.root.getLeftChild().insert_right(43)
#bt.insert_right(27)
#bt.root.getRightChild().insert_left(87)
