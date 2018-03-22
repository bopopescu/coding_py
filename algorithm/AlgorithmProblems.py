#!/usr/bin/env python
#coding=utf-8
import collections
import re
import random
import math
import sys

# tools
def stdin_readline(end_pattern='\n'):
    buf = []
    while True:
        stdin = sys.stdin.readline().strip('\n')
        if not stdin or (re.match(end_pattern, stdin)):
            break
        buf.append(stdin.split(' '))

    return buf


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
    # 小时和分钟十位1和个位2的下标
    index1 = 2
    index2 = 3

    min_val = num_string[0]

    for i in range(5, -1, -1):
        # 最小时间
        min_rst[i] = num_string[i]
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

    # 使用内建方法
    count = collections.Counter(num_string)
    count = dict(count)

    min_val = num_string[0]
    count_num = 0
    cl2 = 0
    c0_5 = 0
    c6_9 = 0
    for key, value in count.items():
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



# 2. 输入两个链表，找出它们的第一个公共结点。



# 3. 统计词频

def words_ana():

    # input : 
    # (行数)3
    # (单词个数)3 SQL DW AND
    # 1 AND
    # 3 SQL SQL DW
    # (结束)2

    # output : 
    #           AND 1
    #           SQL 2
    #           DW 1
    #           (单词) (词频)

    hashmap = {}
    data = stdin_readline()
    line_num = int(data[0][0])
    for line_index in range(1, line_num + 1):
        line = data[line_index]
        for index in range(1, int(line[0]) + 1):
            item = line[index]
            import pdb;pdb.set_trace()
            if hashmap.get(item, None) is None:
                hashmap[item] = 1
            else:
                hashmap[item] += 1

    for k, v in hashmap.items():
        print('%s %d' % (k, v))



# 4. 动态规划问题：
# 一土豪要怎样刷礼物才能让主播拿到人气最佳的称号(支持度达到end)
# 支持方法:
#     - x个C币 +2 支持度
#     - y个C币 *2 支持度
#     - z个C币 -2 支持度

def cal_c_coin():
    # input : 1 0.1 2 1 10
    # output : 
    #           *2
    #           *2
    #           *2
    #           *2
    #           0.4

    # 数据读取
    data = stdin_readline()[0]
    # 提取数据
    x = float(data[0])
    y = float(data[1])
    z = float(data[2])
    start = int(data[3])
    end = int(data[4])

    _range = end - start

    # 现在的支持度
    cur_point = start
    # 土豪所花的金币数目
    cur_used_coins = 0

    while (cur_point < end):
        # 计算下一步所需要的金币数
        # 取到终点所产生的代价最小的方案
        if (((end-cur_point)/2) * x) < ((math.sqrt((end-cur_point))) * y):
            # x的情况
            cur_used_coins = cur_used_coins + x
            cur_point = cur_point + 2
            print("+2")
        else:
            # y的情况
            cur_used_coins = cur_used_coins + y
            cur_point = cur_point * 2
            print("*2")

    print(cur_used_coins)


# 测试部分
def test():

    # tools
    data = stdin_readline()
    print(data)

    # 1. 给6位随机数，计算出最小时间、最大时间并判断是否符合时间规则
    random_list = [str(random.randint(0, 9)) for i in range(6)]
    random_string = ''.join(random_list)
    # get_maxmin_time(random_string)

    # 2. 输入两个链表，找出它们的第一个公共结点

    # 3. 统计词频
    # words_ana()
    # 4. 动态规划问题：
    # cal_c_coin()

test()