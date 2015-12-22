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
    parent_stack = []
    if binary_tree.root:
        node = binary_tree.root
        while node:
            if node.data:
                parent_stack.append(node)
            node = node.getLeftChild()
            pdb.set_trace()
            while not node:
                if len(parent_stack) != 0:
                    node = parent_stack.pop()
                    if not node.getRightChild():
                        val = node.getValue()
                        if val:
                            reslut.append(val)
                    else:
                        node = node.getRightChild()
                else:
                    break
    return result

                    

bt = BinaryTree(24)
bt.createTree(bt.root)
print("先序遍历")
print(preorder_traverse(bt))
print("中序遍历")
print(inorder_traverse(bt))
print("后序遍历")
print(postorder_traverse(bt))

