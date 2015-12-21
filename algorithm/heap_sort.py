#!/usr/bin/env python3
#coding=utf-8

import random
from myMaxHeap import *
import pdb

def heap_sort(data):
    data_size = len(data)
    count = data_size//2
    new_list = buildMaxHeap(data)
    result = []
    print('new_list:')
    print(new_list)

    while len(data) != 0:
        result.append(data.pop(0))
        count -= 1
        for i in range(len(data)//2, 0, -1):
            data = adjustMaxHeap(data, i)
        #pdb.set_trace()

    return result

if __name__ == '__main__':
    raw_list = [random.randint(0,100) for i in range(10)]
    print("raw_list:")
    print(raw_list)
    new_list = heap_sort(raw_list)
    print("sorted :")
    print(new_list)
