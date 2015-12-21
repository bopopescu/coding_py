#!/usr/bin/env python3
#coding=utf-8
import pdb

def getLeft(index):
    return (index * 2) - 1

def getRight(index):
    return (index * 2)

def getParent(index):
    return (index // 2) -1

def swapValue(data, a_index, b_index):
    a = data[a_index]
    data[a_index] = data[b_index]
    data[b_index] = a
    return data

def adjustMaxHeap(data, i):
    data_size = len(data) - 1
    while 1:
        left = getLeft(i)
        right = getRight(i)
        index = i - 1
        largest = index

        if left <= data_size and data[index] < data[left]:
            largest = left
        else:
            largest = index

        if right <= data_size and data[right] > data[largest]:
            largest = right

        swapValue(data, index, largest)

        if i == largest + 1:
            return data
            break

        i = largest + 1

def buildMaxHeap(data):
    data_size = len(data)
    for i in range(data_size//2, 0, -1):
        data = adjustMaxHeap(data, i)

    return data

if __name__ == '__main__':
    #raw_list = [2,4,8,6,9,23,1,5]
    raw_list = [47, 42, 30, 22, 4, 19, 38]
    print('raw_list:')
    print(raw_list)
    new_list = buildMaxHeap(raw_list)
    print('new_list:')
    print(new_list)
            





