#!/usr/bin/env python3
#coding=utf-8

from myTree import BinaryTree
import pdb

def preorder_traverse(binary_tree):
    result = []
    parent_stack = []
    if binary_tree.root:
        node = binary_tree.root
        while node:
            val = node.getValue()
            if val:
                result.append(val)
            parent_stack.append(node)
            node = node.getLeftChild() 
            if not node:
                while not node:
                    if len(parent_stack) != 0:
                        node = parent_stack.pop()
                        node = node.getRightChild()
                    else:
                        break

    return result

def inorder_traverse(binary_tree):
    result = []
    parent_stack = []
    if binary_tree.root:
        node = binary_tree.root
        while node:
            parent_stack.append(node)
            node = node.getLeftChild()
            while not node:
                if len(parent_stack) != 0:
                    node = parent_stack.pop()
                    val = node.getValue()
                    if val:
                        result.append(val)
                    node = node.getRightChild()
                else:
                    break
    return result

def postorder_traverse(binary_tree):
    result = []
    stack_1 = []
    stack_2 = []
    stack_1.append(binary_tree.root)
    while len(stack_1) != 0:
        node = stack_1.pop()
        stack_2.append(node.getValue())
        if node.getLeftChild():
            stack_1.append(node.getLeftChild())
        if node.getRightChild():
            stack_1.append(node.getRightChild())
    stack_2.reverse()
    return stack_2


bt = BinaryTree(24)
bt.createTree(bt.root)
print("先序遍历")
print(preorder_traverse(bt))
print("中序遍历")
print(inorder_traverse(bt))
print("后序遍历")
print(postorder_traverse(bt))

