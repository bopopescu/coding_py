#!/usr/bin/env python

import urllib2
from multiprocessing.dummy import Pool as ThreadPool

urls = [
    'http://www.baidu.com',
    'http://www.163.com',
    'http://www.qq.com',
]

pool = ThreadPool(4)

def url_print(url):
    response = urllib2.urlopen(url)
    return response.read()

results = pool.map(url_print, urls)
pool.close()
pool.join()
print results
