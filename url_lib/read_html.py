#!/usr/bin/env python
#coding=utf-8

import urllib2
import urllib

def return_html():
    response = urllib2.urlopen('http://163.com')
    html = response.read()
    return html
def return_html_by_request():
    req = urllib2.Request('http://163.com')
    response = urllib2.urlopen(req)
    html = response.read()
    return html
def post_to_server():
    url = 'http://127.0.0.1:888/cgi-bin/register.cgi'
    values = {'name':'leung',
            'location':'51reboot',
            'language':'Python'}
    data = urllib.urlencode(values)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    the_page = response.read()
    return 1
def get_to_server():
    data = {}
    data['name'] = 'leung'
    data['location'] = '51reboot'
    data['language'] = 'python'
    url_values = urllib.urlencode(data)
    print url_values

    url = 'http://127.0.0.1:888'
    full_url = url + '?' + url_values
    data = urllib2.urlopen(full_url)
def post_to_server_with_agent():
    url = 'http://127.0.0.1:888'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.154 Safari/537.36 LBBROWSER'
    values = {'name':'leung',
            'location':'51reboot',
            'language':'Python'}
    headers = {'User-Agent':user_agent}
    data = urllib.urlencode(values)
    req = urllib2.Request(url, data, headers)
    response = urllib2.urlopen(req)
    the_page = response.read()
    return 1
def get_url():
    url = 'http://weibo.com'
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)

    print "URL:", url
    print "After redirection:",response.geturl()

if __name__ == '__main__':
#    print return_html_by_request()
#    get_to_server()
#    post_to_server_with_agent()
    get_url()
