#!/usr/bin/env python

import urllib, urllib2, re

response = urllib2.urlopen('http://cpu.zol.com.cn/546/5465527.html')
html = response.read()
p = re.compile('[iI][0-9][-\s]+[a-zA-Z0-9]*')
result = p.findall(html)
print result

