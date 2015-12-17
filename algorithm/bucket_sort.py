#!/usr/bin/env python3
#coding=utf-8
import pdb
import random
import time


if __name__ == '__main__':
    raw_list = [random.randint(0,100) for i in range(10)]
    bucket_size = 10
    max_num = max(raw_list)
    bucket_count = 1
    result = []
    #pdb.set_trace()
    while (bucket_size*bucket_count) - max_num < 0:
        bucket_count *= 10

    atime = time.time()
    bucket = [[] for i in range(bucket_count)]

    for num in raw_list:
        #pdb.set_trace()
        bucket[(num//(bucket_size + 1))].extend([num])

    for index, bucket_item in enumerate(bucket):
        if bucket_item != []:
            result.extend(sorted(bucket_item))


    print("before sort:")
    print(raw_list)
    print("new list:")
    print(result)
    btime = time.time()
    print("total time:")
    print(btime - atime)

    atime = time.time()
    print("cpython sort:")
    new_list = sorted(raw_list)
    print(new_list)
    btime = time.time()
    print("total time:")
    print(btime - atime)
