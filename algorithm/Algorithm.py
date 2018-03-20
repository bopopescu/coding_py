# coding:utf-8
import random

class Algorithm(object):

    @staticmethod
    def swap(swap_list, index_a, index_b):
        tmp = swap_list[index_a]
        swap_list[index_a] = swap_list[index_b]
        swap_list[index_b] = tmp

        return swap_list

    @classmethod
    def insert_sort(cls, sort_list):
        N = len(sort_list)
        for i in range(N):
            j = i
            while (j > 0) & (sort_list[j-1] > sort_list[j]):
                sort_list = cls.swap(sort_list, j, j-1)
                j -= 1

        return sort_list

    @classmethod
    def bubble_sort(cls, sort_list):
        N = len(sort_list)
        for i in range(N):
            for j in range(N - i - 1):
                if sort_list[j] > sort_list[j+1]:
                    cls.swap(sort_list, j, j+1)

        return sort_list

    @classmethod
    def select_sort(cls, sort_list):
        N = len(sort_list)
        for i in range(N):
            min_index = i
            for j in range(i+1, N):
                if sort_list[min_index] > sort_list[j]:
                    min_index = j                         # 找出最小下标
                cls.swap(sort_list, i, min_index)
        return sort_list

    @classmethod
    def shell_sort(cls, sort_list):
        N = len(sort_list)
        gap = 1

        while N/3 > gap:  # 保证3*gap不会越界
            gap = 3*gap + 1   # 找出最大的gap, Knunth's 提出的递增序列

        while gap >= 1:
            for i in range(gap, N):
                for j in range(i, 0, -gap):
                    if sort_list[j] < sort_list[j-gap]:
                        cls.swap(sort_list, j, j-gap)
            gap //= 3

        return sort_list

    @classmethod
    def partion(cls, sort_list, lo, hi):
        p = sort_list[lo]
        cur_lo = lo
        cur_hi = hi
        while True:
            for i in range(cur_hi, cur_lo - 1, -1):
                cur_hi = i
                if sort_list[i] < p:
                    break

            for j in range(cur_lo, cur_hi + 1):
                cur_lo = j
                if sort_list[j] > p:
                    break

            if cur_lo >= cur_hi:
                break

            cls.swap(sort_list, cur_hi, cur_lo)
        cls.swap(sort_list, lo, cur_hi)
        return cur_hi

    @classmethod
    def quick_sort(cls, sort_list, lo, hi):
        N = len(sort_list) - 1
        if lo <= hi:
            mid = cls.partion(sort_list, lo, hi)
            cls.quick_sort(sort_list, lo, mid - 1)
            cls.quick_sort(sort_list, mid + 1, hi)

        return sort_list



    @classmethod
    def demo_function(cls):
        sort_list = []
        for i in range(10):
            sort_list.append(round(random.random() * 100, 4))
        sort_algorithm = {
            "insert_sort": cls.insert_sort,
            "shell_sort": cls.insert_sort,
            "bubble_sort": cls.insert_sort,
            # "quick_sort": cls.quick_sort,
        }
        print("Before Sort:\n")
        print(sort_list)
        print("\nAfter Sort:\n")
        for name, func in sort_algorithm.items():
            print(name)
            print(func(sort_list.copy()))

        print("\nAfter Sort:\n")
        print("quict_sort:")
        # sort_list = [2, 4, 6, 2 ,7,8]
        ans = cls.quick_sort(sort_list.copy(), 0, len(sort_list) - 1)
        print(ans)


Algorithm.demo_function()
# Algorithm.quick_sort([3,6, 2,1], 0, 4)






