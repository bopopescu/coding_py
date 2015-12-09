#!/usr/bin/env python
#coding=utf-8


def adjust_range(data, step):
    position_list = set()
    result = []
    for num in data:
        position_list.add(num//step)

    for item in list(position_list):
        start = item * step
        end = (item + 1) * step
        result.append([start, end])

    return result


if __name__ == '__main__':
    print(adjust_range([2,19,3,4,24,16,1804,1805],10))
     

