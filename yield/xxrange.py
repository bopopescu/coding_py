#!/usr/bin/env python
#coding=utf-8

class xxrange:
    def __init__(self, *args, **kwargs):
        if len(args) == 1:
            self.lower = 0
            self.upper = args[0]
            self.step = 1
        elif len(args) == 2:
            print "haha"
            self.lower = args[0]
            self.upper = args[1]
            self.step = 1
        elif len(args) == 3:
            self.lower = args[0]
            self.upper = args[1]
            self.step = args[2]
        else:
            return 0
    def __iter__(self):
        step = self.step
        start = self.lower
        stop = self.upper
        while start < stop:
            yield start
            start += step

for i in xxrange(10,20):
    print i,
