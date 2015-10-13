#!/usr/bin/env python
#coding=utf-8
import re
import sys

def readfile(filename):
    f = open(filename)
    word_dict = {}
    i = 0
    while 1:
        word = ''
        buf = ''
        while 1:
            buf = f.read(1)
            if not re.search('[a-zA-Z]| ',buf):
                while buf != ' ':
                    buf = f.read(1)
                    if buf == '':
                        break
                break
            elif buf == ' ':
                break
            word = word + buf
        if buf == '':
            break
        word_dict[word] = word_dict.get(word, 0) + 1
    f.close()
    return word_dict

def count_words(filename):
    f = open(filename)
    count = 0
    while 1:
        buf = f.read(1024)
        buf_list = buf.split(' ')
#剔除/n
        for words in buf_list:
            words = words.split('\n')
            if len(words) > 1:
                count += len(words) - 1
                for check in words:
                    if check == '':
                        count -= 1
        if len(buf) == 0:
            break
        print buf_list
        count += len(buf_list)
#如果read到的数据在边界位置不是完整的单词，则单词个数减一。
        if buf[len(buf) - 1] != ' ' and len(buf) == 1024:
            count -= 1
    f.close()
    return count

if __name__ == '__main__':
#    print readfile(sys.argv[1])
    print count_words(sys.argv[1])

