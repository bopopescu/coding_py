#!/usr/bin/env python
#coding=utf-8
import collections
import re
import random
import math
import sys
# import Collections

# tools
def stdin_readline(end_pattern='\n$', type=None):
    buf = []
    while True:
        stdin = sys.stdin.readline().strip('\n')
        if not stdin or (re.match(end_pattern, stdin)):
            break
        stdin = stdin.split(' ')
        # cleaning
        stdin = list(filter(lambda s:s and s.strip(),stdin))
        if type is int:
            stdin = [int(item) for item in stdin]
        buf.append(stdin)

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

# 5. 

def ana_questions():
    rst = []
    line_num = int(sys.stdin.readline().strip('\n').split(' ')[0])
    for line_index in range(line_num):
        data = sys.stdin.readline().strip('\n').split(' ')
        question_name = data[0]
        pub_cnt = int(data[1])
        pass_cnt = int(data[2])

        feedback = pass_cnt / pub_cnt
        if 0 < feedback <= 0.3:
            diff = 5
        elif 0.3 < feedback <= 0.6:
            diff = 4
        elif 0.6 < feedback <= 1:
            diff = 3
        else:
            continue
        rst.append((question_name, diff))

    sorted(rst, key=lambda x:x[0])

    for item in rst:
        print("%s %s" % (item[0], item[1]))

# 6. 为了不断优化推荐效果，今日头条每天要存储和处理海量数据。假设有这样一种场景：我们对用户按照它们的注册时间先后来标号，对于一类文章，每个用户都有不同的喜好值，我们会想知道某一段时间内注册的用户（标号相连的一批用户）中，有多少用户对这类文章喜好值为k。因为一些特殊的原因，不会出现一个查询的用户区间完全覆盖另一个查询的用户区间(不存在L1<=L2<=R2<=R1)。

# 输入描述:
# 输入： 第1行为n代表用户的个数 第2行为n个整数，第i个代表用户标号为i的用户对某类文章的喜好度 第3行为一个正整数q代表查询的组数  第4行到第（3+q）行，每行包含3个整数l,r,k代表一组查询，即标号为l<=i<=r的用户中对这类文章喜好值为k的用户的个数。 数据范围n <= 300000,q<=300000 k是整型


# 输出描述:
# 输出：一共q行，每行一个整数代表喜好值为k的用户的个数

def toutiao_1():
    hashmap = {}
    data = stdin_readline(type=int)
    line_num = data[0][0]
    like_list = data[1]
    for index in range(len(like_list)):
        if like_list[index] not in hashmap:
            hashmap[like_list[index]] = [index]
        else:
            hashmap[like_list[index]].append(index)
    q_num = data[2]
    q_data_list = data[3:]

    rst = []

    for q_data in q_data_list:
        cnt = 0
        l = q_data[0]
        r = q_data[1]
        k = q_data[2]
        # import pdb;pdb.set_trace()
        if hashmap.get(k, None):
            index_h = half_search(hashmap[k], l-1)
            index_t = half_search(hashmap[k], r-1)
            if like_list[hashmap[k][index_h]] == k:
                cnt += 1
            if like_list[hashmap[k][index_t]] == k:
                cnt += 1
            rst.append(cnt + (index_t - index_h - 1))
        else:
            rst.append(0)
        # tmp_like_seg = like_list[l-1:r-1]
        # tmp_like_seg = collections.Counter(tmp_like_seg)
        # rst.append(tmp_like_seg.get(k, 0))
        # sorted(tmp_like_seg)
        # k_index = half_search(tmp_like_seg, k)
        # if tmp_like_seg[k_index] == k:
        #     cnt = 1
        # else:
        # while True:
        #     if tmp_like_seg[k_index] == k:
        #         cnt += 1
        #     []
    for result in rst:
        print(result)

def half_search(arr, key):
    _min = 0
    _max = len(arr)

    while _min <= _max:
        mid = (_min+_max) >> 1

        if key < arr[mid]:
            _min = mid - 1
        elif key > arr[mid]:
            _max = mid + 1
        else:
            return mid
    return _min

# 7.
def toutiao11():
    lines = stdin_readline(type=int)
    val_num = lines[0][0]
    diff = lines[0][1]
    data1 = lines[1]

    data2 = [(item + diff) for item in data1]

    rst = set(data1) & set(data2)
    print(len(rst))

    return 0

# 8.
def toutiao2(n=None):
    # plan 1:
    #   m = s
    #   s = s + s
    # plan 2:
    #   s = s + m
    if n is None:
        lines = stdin_readline(type=int)
        sum_bits = lines[0][0]
    else:
        sum_bits = int(n)

    min_cnt = sys.maxsize

    # i means m, j means s
    dp = [[0 for j in range(sum_bits)] for i in range(sum_bits//2)]
    # length of m
    for i in range(sum_bits//2):
        l_m = i + 1
        # length of s
        for j in range(sum_bits):
            if i == j == 0:
                continue
            l_s = j + 1
            if l_s <= l_m:
                dp[i][j] = sys.maxsize
            elif l_s > l_m:
                if not (l_s & 1):
                    p1_min_val = sys.maxsize
                    if l_s // 2 == l_m:
                        for k in range(l_m):
                            if p1_min_val > dp[k][l_s//2 - 1]:
                                p1_min_val = dp[k][l_s//2 - 1]
                    if p1_min_val == 0 or p1_min_val < dp[i][l_s - l_m - 1]:
                        dp[i][j] = p1_min_val + 1
                        continue

                if dp[i][l_s - l_m - 1] != 0 or ((l_s - l_m) & 1) == 0:
                    dp[i][j] = dp[i][l_s - l_m - 1] + 1

        if dp[i][sum_bits - 1] != 0 and dp[i][sum_bits - 1] < min_cnt:
            min_cnt = dp[i][sum_bits - 1]

    print(min_cnt)

            


# 9. 
def printer(str_val):
    # 0   1   2   3   4
    # 5   6   7   8   9
    # 10  11  12  13  14
    # 15  16  17  18  19
    # 20  21  22  23  24
    hashmap = {}

    hashmap[0] = [0, 1, 2, 3, 4, 5, 9, 10,
                  14, 15, 19, 20, 21, 22, 23, 24]

    hashmap[1] = [4, 9, 14, 19, 24]

    hashmap[2] = [0, 1, 2, 3, 4, 9,
                  10, 11, 12, 13, 14,
                  15, 20, 21, 22, 23, 24]

    hashmap[3] = [0, 1, 2, 3, 4, 9,
                  10, 11, 12, 13, 14,
                  19, 20, 21, 22, 23, 24]

    hashmap[4] = [0, 4, 5, 9, 10, 11, 12, 13, 14,
                  19, 24]

    hashmap[5] = [0, 1, 2, 3, 4, 5, 10, 11, 12, 13, 14,
                  19, 20, 21, 22, 23, 24]

    hashmap[6] = [0, 1, 2, 3, 4, 5,10, 11, 12, 13, 14,
                  15, 19, 20, 21, 22, 23, 24]

    hashmap[7] = [0, 1, 2, 3, 4, 9, 14, 19, 24]

    hashmap[8] = [0, 1, 2, 3, 4, 5, 9,
                  10, 11, 12, 13, 14, 15, 19,
                  20, 21, 22, 23, 24]

    hashmap[9] = [0, 1, 2, 3, 4, 5, 9,
                  10, 11, 12, 13, 14, 19,
                  20, 21, 22, 23, 24]

    num_length = len(str_val)

    p_matrix = [hashmap[num] for num in str_val]

    # p_6 = hashmap[val]
    index = 0
    for i in range(5):
        print('')
        for num_index in range(num_length):
            for j in range(5):
                # p_6 = 
                if index in p_6:
                    print('6', end='')
                else:
                    print('.', end='')

                index += 1

# 10. 动态规划问题
# 有数组penny，penny中所有的值都为正数且不重复。每个值代表一种面值的货币，每种面值的货币可以使用任意张，再给定一个整数aim(小于等于1000)代表要找的钱数，求换钱有多少种方法。

# 给定数组penny及它的大小(小于等于50)，同时给定一个整数aim，请返回有多少种方法可以凑成aim。

# 测试样例：
# [1,2,4],3,3
# 返回：2

def count_ways(penny, n, aim):
    dp = [[0 for j in range(aim + 1)]for i in range(n)]
    # 将能被第零种货币组成的情况
    dp[0] = [1 if i % penny[0] == 0 else 0 for i in range(aim + 1)]
    # 组成0的情况只有一种，那就是不用货币
    for i in range(n):
        dp[i][0] = 1

    for i in range(n):
        for j in range(aim+1):
            # 如果aim比增加后的金钱数小
            if j - penny[i] < 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-penny[i]]

    return dp[-1][-1]

# 11. 有n级台阶，一个人每次上一级或者两级，问有多少种走完n级台阶的方法。为了防止溢出，请将结果Mod 1000000007

# 给定一个正整数int n，请返回一个数，代表上楼的方式数。保证n小于等于100000。

# 测试样例：
# 1
# 返回：1

def go_up_stairs(n):
    if n <= 2:
        result = [1, 2, 3]
        print(result[n-1])
        return 0
    f1 = 1
    f2 = 2
    f = f1 + f2
    for i in range(2, n):
        f = f1 + f2
        f1 = f2
        f2 = f
    print(f)
    return 0

# 12. 有一个矩阵map，它每个格子有一个权值。从左上角的格子开始每次只能向右或者向下走，最后到达右下角的位置，路径上所有的数字累加起来就是路径和，返回所有的路径中最小的路径和。

# 给定一个矩阵map及它的行数n和列数m，请返回最小路径和。保证行列数均小于等于100.

# 测试样例：
# [[1,2,3],[1,1,1]],2,3
# 返回：4

def minimum_path(mmap, n, m):
    dp = [[0 for j in range(m)] for i in range(n)]
    # dp[i][j] 走到坐标(i, j)的最小路径
    # 只能往右走或者往下走
    dp[0][0] = mmap[0][0]
    for i in range(1, m):
        dp[0][i] = dp[0][i-1] + mmap[0][i]

    for j in range(1, n):
        dp[j][0] = dp[j-1][0] + mmap[j][0]

    for i in range(1, n):
        for j in range(1, m):
            if dp[i-1][j] <= dp[i][j-1]:
                dp[i][j] = dp[i-1][j] + mmap[i][j]
            else:
                dp[i][j] = dp[i][j-1] + mmap[i][j]

    return dp[-1][-1]




# 测试部分
def test():

    # tools
    # data = stdin_readline(type=int)
    # print(data)

    # 1. 给6位随机数，计算出最小时间、最大时间并判断是否符合时间规则
    random_list = [str(random.randint(0, 9)) for i in range(6)]
    random_string = ''.join(random_list)
    # get_maxmin_time(random_string)

    # 2. 输入两个链表，找出它们的第一个公共结点

    # 3. 统计词频
    # words_ana()
    # 4. 动态规划问题：
    # cal_c_coin()
    # 5. 
    # ana_questions()

    # 6. 
    # toutiao_1()
    # print(half_search([-2, 2 ,3, 4, 5, 100, 200,240,2344], 0))

    # 7 .
    # toutiao11()

    # 8. 
    for i in range(4, 17):
        toutiao2(i)

    # 9. 
    # printer(2)

    # 10.
    # count_ways([1,2,4],3,3)

    # 11. 
    # go_up_stairs(4)

    # 12.
    # minimum_path([[1,2,3],[1,1,1]],2,3)

test()