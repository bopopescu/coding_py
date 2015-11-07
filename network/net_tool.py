#!/usr/bin/env python
#conding=utf-8

from daemon import Daemon
import socket
import select
import time
import pdb


__all__ = ["nbNet", "sendData_mh"]

class NetBase:
    def setFd(self, sock):
        dbgPrint("\n -- setFd start!")
        #创建state类的对象，里面放着每个socket连接的读写、状态信息
        tmp_state = STATE()
        tmp_state.sock_obj = sock
        #完成状态对象的初始化后，将其放入conn_state
        self.conn_state[sock.fileno()] = tmp_state
        self.conn_state[sock.fileno()].printState()
        dbgPrint("\n --- setFd end!")

    def accept(self, fd):
        dbPrint("\n -- accept start!")
        #取出state对象
        sock_state = self.conn_state[fd]
        #在socket_stat对象中取出socket连接对象
        sock = sock_stat.sock_obj
        #对指定socket进行非阻塞监听
        conn, addr = sock.accept()
        conn.setblocking(0)
        #返回socket连接
        return conn

    def close(self, fd):
        try:
            sock = self.conn_state[fd].sock_obj
            sock.close()
            self.epoll_sock.unregister(fd)
            self.conn_state.pop(fd)
        except:
            dbgPrint("Close fd : %s abnormal" % fd)
            pass

    def read(self, fd):
        try:
            sock_state = self.conn_state[fd]
            conn = sock_state.sock_obj
            if sock_state.need_read <= 0:
                raise socket.error


            one_read = conn.recv(sock_state.need_read)
            dbPrint("\ntread func fd: %d, one_read: %s, need_read: %d" % (fd, one_read, sock_state.need_read))
            if len(one_read) == 0:
                raise socket.error
            sock_state.buff_read += one_read
            sock_state.have_read += len(one_read)
            sock_state.need_read -= len(one_read)
            sock_state.printState()


            if sock_state.have_read == 10:
                if header_said_need_read <= 0:
                    raise socket.error
                sock_state.need_read += header_said_need_read
                sock_state.buff_read = ''
                sock_state.printState()
                return "readcontent"
            elif sock_state.need_read == 0:
                return "process"
            else:
                return "readmore"
        except (socket.error, ValueError), msg:
            try:
                if msg.errno == 11:
                    dbgPrint("11" + msg)
                    return "retry"
            except:
                pass
            return 'closing'

    def write(self, fd):
        sock_state = self.conn_state[fd]
        conn = sock_state.sock_obj
        last_havd_send = sock_state.have_write
        try:
            have_send = conn.send(sock_state.buff_write[last_have_send:])
            sock_state.have_write += have_send
            sock_state.need_write -= have_send
            if sock_state.need_write == 0 and sock_state.have_write != 0:
                sock_state.printState()
                dbgPrint('\n write data completed!')
                return "writecomplete"
            else:
                return "writemore"
        except socket.error, msg:
            return "closing"

    def run(self):
        while True:
            dbgPrint("\brun func loop:")
            #遍历conn_state字典，将每个连接的id返回,对业务逻辑并没有什么作用
            for i in self.conn_state.iterkeys():
                dbgPrint("\n - state of fd: %d" % i)
                self.conn_state[i].printState()
            epoll_list = self.epoll_sock.poll()
            #取出epoll中的fd和时间进行处理
            for fd, events in epoll_list:
                dbgPrint('\n -- run epoll return fd: %d. event: %s' % (fd, event))
                sock_state = self.conn_state[fd]
                if select.EPOLLHUP & events:
                    dbgPrint("EPOLLHUB")
                    sock_state.state = "closing"
                elif select.EPOLLERR & events:
                    dbPrint("EPOLLERR")
                    sock_state.state = "closing"
                #使用状态机进行处理各种状态
                self.state_machine(fd)
    def state_machine(self, fd):
        dbgPrint("\n -state machine: fd: %d, status: %s" % (fd, self.conn_state[fd].state)
        sock_state = self.conn_state[fd]
        #根据不同的状态调用不同的处理函数
        self.sm[sock_state.state](fd)

class Net(NetBase):
    def __init__(self, addr, port, logic):
        dbgPrint('\n__init__:start!')
        self.conn_state = {}
        #建立socket连接
        self.listen_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        self.listen_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.listen_sock.bind((addr, port))
        self.listen_sock.listen(10)
        #将socket连接加入到conn_state
        self.setFd(self.listen_sock)
        #初始化epoll
        self.epoll_sock = select.epoll()
        #注册epoll
        self.epoll_sock.register(self.listen_sock.fileno(), select.EPOLLIN)
        #逻辑函数
        self.logic = logic
        #下面的字典放着各种状态的处理函数
        slef.sm = {
            "accept" : self.accept2read,
            "read"   : self.read2process,
            "write"  : self.write2read,
            "process": self.process,
            "closing": self.close,
        }
        dbgPrint('\n__init__: end, register no: %s' % self.listen_sock.fileno() )

    def process(self, fd):
        sock_state = self.conn_state[fd]
        response = self.logic(sock_state.buff_read)
        sock_state.buff_write = "%010d%s" % (len(response), response)
        sock_state.need_write = len(sock_state.buff_write)
        sock_state.state = "write"
        self.epoll_sock.modify(fd, select.EPOLLOUT)
        sock_state.printState()
        #self.state_machine(fd)
    
    def accept2read(self, fd):
        conn = self.accept(fd)
        self.epoll_sock.register(conn.fileno(), select.EPOLLIN)
        #对新的连接进行初始化 
        self.setFd(conn)
        #新连接的初始状态为read
        self.conn_state[conn.fileno()].state = "read"
        # now end of accept, but the main process still on 'accept' status
        # waiting for new client to connect it.
        dbgPrint("\n -- accept end!")

    def read2process(self, fd):
        """fd is fileno() of socket"""
        #pdb.set_trace()
        read_ret = ""
        try:
            read_ret = self.read(fd)
        except (Exception), msg:
            dbgPrint(msg)
            read_ret = "closing"
        if read_ret == "process":
            # recv complete, change state to process it
            #sock_state.state = "process"
            self.process(fd)
        elif read_ret == "readcontent":
            pass
        elif read_ret == "readmore":
            pass
        elif read_ret == "retry":
            pass
        elif read_ret == "closing":
            self.conn_state[fd].state = 'closing'
            # closing directly when error.
            self.state_machine(fd)
        else:
            raise Exception("impossible state returned by self.read")

    def write2read(self, fd):
        try:
            write_ret = self.write(fd)
        except socket.error, msg:
            write_ret = "closing"

        if write_ret == "writemore":
            pass
        elif write_ret == "writecomplete":
            sock_state = self.conn_state[fd]
            conn = sock_state.sock_obj
            self.setFd(conn)
            self.conn_state[fd].state = "read"
            self.epoll_sock.modify(fd, select.EPOLLIN)
        elif write_ret == "closing":
            dbgPrint(msg)
            self.conn_state[fd].state = 'closing'
            # closing directly when error.
            self.state_machine(fd)
    

if __name__ == '__main__':
    def logic(d_in):
        return(d_in[::-1])

    reverseD = nbNet('0.0.0.0', 9076, logic)
    reverseD.run()

