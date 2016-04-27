#!/usr/bin/env python3
# coding=utf-8

import os
import re
import shutil

def match_file(root_dir, _re):
    match_list = []
    for root, dirs, files in os.walk(root_dir):
        for d in dirs:
            if re.match(d, _re):
                match_list.append(os.path.join(root, d))
    
    return match_list

def del_action(del_list):
    for _dir in del_list:
        shutil.rmtree(_dir)

if __name__ == '__main__':
    del_list = match_file('/Users/*****/work_file/*****/', '__pycache__')
    del_action(del_list)
    print('done')
