#!/usr/bin/env python3
#coding=utf-8

import sys
import re

def process_file_data(file_name, base_filter = 'PackDataView'):
    result = []
    with open(file_name, 'r') as f:
        for line in f:
            analysis_result = analysis_data(line, base_filter)
            if analysis_result:
                result.append(analysis_result)

    return result


def analysis_data(line, base_filter):
    date_filter = '\d*-\d*-\d*'
    time_filter = '\d*:\d*:\d*'
    dict_filter = '{.*}$'
    valid_line = re.search(base_filter, line)
    if valid_line:
        reslut = {
            'log_date': re.search(date_filter, line).group(),
            'log_time': re.search(time_filter, line).group(),
            'data': re.search(dict_filter, line).group()
            }
        return line

if __name__ == '__main__':
    if len(sys.argv) > 1 and re.search('.log$', sys.argv[1]):
        file_name = sys.argv[1]
        result = process_file_data(file_name = file_name))
    else:
        print("input file name")
