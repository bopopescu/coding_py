#!/usr/bin/env python
#coding=utf-8

from daemon import Daemon
import socket
import time
from multiprocessing import Pool
import Queue
import threading

html = """HTTP/1.1 200 OK\r\nContent-Type: image/jpeg\r\nConnection: close\r\nContent-Length: """
html404 = """HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\nContent-Length: 13\r\n\r\n<h1>404 </h1>"""
queue = Queue.Queue(20)

class agentD(Daemon):
    def run(self):
        listen_fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        listen_fd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listen_fd.bind(("0.0.0.0", 9000))
        listen_fd.listen(10)
        while True:
            conn, addr = listen_fd.accept()
            print "coming", conn, addr
            raw = {
                'conn':conn,
                'addr':addr
                }
            print raw
            try:
                print queue.qsize()
                queue.put(raw)
                print queue.get()
            except Exception as e:
                print e


def worker(name):
    while True:
        if queue.qsize() > 0:
            raw = queue.get()
            conn = raw['raw']
            addr = raw['addr']
            read_data = conn.recv(1000)
            pic_name = read_data.split(" ")[1][1:]
            print pic_name
            try:
                with file(pic_name) as f:
                    pic_conntent = f.read()
                    length = len(pic_content)
                    http_resp = html
                    http_resp += "%d\r\n\r\b" % length
                    print html_resp
                    html_resp += pic_conntent
            except:
                print "404"
                html_resp = html404

            while len(html_resp) > 0:
                sent_cnt = conn.send(html_resp)
                print "send: ", sent_cnt
                html_resp = html[sent_cnt:]
            conn.close()
def init_agent(name):
    print name
    agented = agentD(pidfile = "agentd.pid", stdout = "agentd.log", stderr = "agentd.log")
    agented.run()

if __name__ == '__main__':
    #agented = agentD(pidfile = "agentd.pid", stdout = "agentd.log", stderr = "agentd.log")
    #agented.run()
    #queue = Queue()
    max_processes = 2
    pool = Pool(processes = 2)
    task_list = list(range(max_processes))
    for i in task_list:
        print queue.qsize()
        if not i:
            pool.apply_async(init_agent, (i,))
        else:
            pool.apply_async(worker, (i,))

    pool.close()
    pool.join()
