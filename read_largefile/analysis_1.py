#!/usr/bin/env python3
#coding=utf-8

import sys
import re
import time
import json
from multiprocessing import Pool, Queue

from pprint import pprint

def process_file_data(file_name, base_filter = 'PackDataView',
                        key_filter = None, value_filter = None,
                        data_visible = True, p = None, q = None):
    result = []
    generator = load_file(file_name)
    for i in range(p_num):
        p.apply_async(choose_data, args = (generator, base_filter, data_visible, q,))
        #choose_result = choose_data(line, base_filter, data_visible)
    p.close()
    p.join()
    if not q.empty():
        for choose_result in q.get():
            if choose_result:
                if key_filter and value_filter:
                    choose_result = analysis_data(choose_result, key_filter, value_filter)
                result.append(choose_result)
    #if key_filter and value_filter:
    #    result = analysis_data(result, key_filter, value_filter)

    return result

def load_file(file_name):
    with open(file_name, 'r') as f:
        for line in f:
            yield line


def choose_data(generator, base_filter, data_visible, q):
    time.sleep(10)
    date_filter = '\d*-\d*-\d*'
    time_filter = '\d*:\d*:\d*'
    dict_filter = '{.*}$'
    batch_filter = "'batch': \d*"
    data = ''
    for line in generator:
        valid_line = re.search(base_filter, line)
        if valid_line:
            data = re.search(dict_filter, line)
            if data:
                data = eval(data.group())
                result = {
                    'log_date': re.search(date_filter, line).group(),
                    'log_time': re.search(time_filter, line).group(),
                    'data': data if data_visible else {},
                    'batch': ''
                    }
                if data:
                    result.update(eval("{%s}" % re.search(batch_filter, line).group()))
                q.put(result)

def analysis_data(line, key_filter, value_filter):
    result = []
    order_list = []
    for order in line['data'].values():
        if order[key_filter] == value_filter:
            order_list.append(order)
    result = {
        'log_date': line['log_date'],
        'log_time': line['log_time'],
        'batch': line['batch'],
        'data': order_list
    }

    return result

if __name__ == '__main__':
    atime = time.time()
    key_filter = 'sort_id'
    value_filter = 2
    data_visible = False
    p_num = 4
    process = Pool(p_num)
    queue = Queue()

    if len(sys.argv) > 1 and re.search('.log', sys.argv[1]):
        file_name = sys.argv[1]
        result = process_file_data(file_name = file_name, key_filter=key_filter,
                                    value_filter=value_filter, data_visible = data_visible,
                                    p = process, q = queue)
        pprint(result)
        print(len(result))
    else:
        print("input file name")
    btime = time.time()

    print("total time : %s" % (btime - atime))
