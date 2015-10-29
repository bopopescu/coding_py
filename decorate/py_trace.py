#!/usr/bin/env python
#coding=utf-8

import sys,os,linecache

def trace(f):
    def globaltrace(frame, why, arg):
        if why == 'call' : return localtrace
        return None
    def localtrace(frame, why, arg):
        if why == 'line':
            filename = frame.f_code.co_filename
            lineno = frame.f_lineno
            bname = os.path.basename(filename)
            print "%s(%s):%s" % (bname, lineno,\
                                        linecache.getline(\
                                        filename, lineno)),
        return localtrace
    def _f(*args, **kwargs):
        sys.settrace(globaltrace)
        result = f(*args, **kwargs)
        sys.settrace(None)
        return result
    return _f
@trace
def a():
    print 1
    for i in range(1,10):
        print i

a()
