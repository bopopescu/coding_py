#!/usr/bin/env python
#coding=utf-8
import collections
import re
import random

# 1. 给6位随机数，计算出最小时间、最大时间并判断是否符合时间规则

def get_maxmin_time(num_string):
    print('-------------')
    print("Random String: %s" % num_string)
    vaild, num_string, count = check_valid_num_string(num_string)
    if not vaild:
        print("String is invalid")
        return False

    max_rst = [None for i in range(6)]
    min_rst = [None for i in range(6)]
    # hour_set = False
    index1 = 2
    index2 = 3

    min_val = num_string[0]

    for i in range(5, -1, -1):
        # 最小时间
        min_rst[i] = num_string[i]
        # if max_rst_full:
        #     break

        # 最大时间
        if not max_rst[1] and min_val < '2' and not count.get('2', None):
            max_rst[1] = num_string[i]
        # 优先设置小时
        elif not max_rst[0] and num_string[i] <= '2':
            max_rst[0] = num_string[i]
        elif not max_rst[1] and num_string[i] <= '3':
            max_rst[1] = num_string[i]
        # 设置分和秒的个位
        elif index1 <= 4 and num_string[i] <= '5':
            max_rst[index1] = num_string[i]
            index1 += 2
        # 设置分和秒的十位
        elif index2 <= 5:
            max_rst[index2] = num_string[i]
            index2 += 2

    print("max_date:")
    print(''.join(str(num) for num in max_rst))
    print("min_date:")
    print(''.join(str(num) for num in min_rst))


    return True



def check_valid_num_string(num_string):

    if len(num_string) != 6:
        return False

    num_string = sorted(num_string)

    # 不用自建方法
    # count = [0 for i in range(len(num_string))]

    # 使用自建方法
    count = collections.Counter(num_string)
    count = dict(count)

    min_val = num_string[0]
    count_num = 0
    cl2 = 0
    c0_5 = 0
    c6_9 = 0
    for key, value in count.items():
        # count_num += value
        # 统计小于2的个数
        if key < '2':
            cl2 += value
        # 统计大于0小于等于5数字的个数
        if key <= '5':
            c0_5 += value
    # 统计大于等于6小于9数字的个数
    c6_9 = len(num_string) - c0_5

    if min_val > '2':
        return False, num_string, count
    elif min_val < '2' and c6_9 > 3:
        return False, num_string, count
    elif min_val is '2' and c6_9 > 2:
        return False, num_string, count

    return True, num_string, count

random_list = [str(random.randint(0, 9)) for i in range(6)]
random_string = ''.join(random_list)
get_maxmin_time(random_string)
# get_maxmin_time('029142')
# get_maxmin_time('199999')
# get_maxmin_time('294512')
# get_maxmin_time('654321')
# get_maxmin_time('831041')
