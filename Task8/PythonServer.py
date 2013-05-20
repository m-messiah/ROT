#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Messiah'

import sys

sys.path.append('./gen-py')

from helloworld import HelloWorld
from helloworld.ttypes import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

import socket


class HelloWorldHandler:
    def __init__(self):
        self.log = {}

    def ping(self):
        print "ping()"

    def add(self, a, b):
        c = int(a) + int(b)
        print "{} + {} = {}".format(a, b, c)
        return int(c)


handler = HelloWorldHandler()
processor = HelloWorld.Processor(handler)
transport = TSocket.TServerSocket(port=9090)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

print "Starting python server..."
try:
    server.serve()
except KeyboardInterrupt:
    print "Kill signal received..."
print "done!"