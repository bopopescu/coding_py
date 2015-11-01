#!/usr/bin/env python
#coding=utf-8

from twisted.internet import protocol, reactor, endpoints

class Echo(protocol.Protocol):
    def dataReceived(self, data):
        self.transport.write(data)


class EchoFactory(protocol.Protocol):
    def buildProtocol(self, addr):
        return Echo()


endpoints.serverFromString(reactor, "tcp:12345").listen(EchoFactory())
reactor.run()
