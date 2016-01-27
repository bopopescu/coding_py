#!/usr/bin/env python3
#coding=utf-8

import sys
import re

from pprint import pprint

def process_file_data(file_name, base_filter = 'PackDataView',
                        key_filter = None, value_filter = None):
    result = []
    with open(file_name, 'r') as f:
        for line in f:
            choose_result = choose_data(line, base_filter)
            if choose_result:
                result.append(choose_result)
    if key_filter and value_filter:
        result = analysis_data(result, key_filter, value_filter)

    return result


def choose_data(line, base_filter):
    date_filter = '\d*-\d*-\d*'
    time_filter = '\d*:\d*:\d*'
    dict_filter = '{.*}$'
    valid_line = re.search(base_filter, line)
    if valid_line:
        result = {
            'log_date': re.search(date_filter, line).group(),
            'log_time': re.search(time_filter, line).group(),
            'data': eval(re.search(dict_filter, line).group())
            }
        return result

def analysis_data(p_data, key_filter, value_filter):
    order_list = []
    result = []
    for line in p_data:
        for order in line['data'].values():
            if order[key_filter] == value_filter:
                order_list.append(order)
        result.append({
                'log_date': line['log_date'],
                'log_time': line['log_time'],
                'data': order_list
            }
        )
    return result

if __name__ == '__main__':
    key_filter = 'sort_id'
    value_filter = 246
    if len(sys.argv) > 1 and re.search('.log$', sys.argv[1]):
        file_name = sys.argv[1]
        pprint(process_file_data(file_name = file_name, key_filter=key_filter, value_filter=value_filter))
    else:
        print("input file name")
