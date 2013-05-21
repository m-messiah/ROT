#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Messiah'

import sys

sys.path.append('./gen-py')

from Parser import Parser
from Parser.ttypes import *
from re import findall, MULTILINE, DOTALL
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer


class ParserHandler:
    def __init__(self):
        self.log = {}

    def ping(self):
        print "ping()"

    def count(self, page, tag):
        c = len(findall("<{0}.*?>.*?</{0}>".format(tag),
                        page, MULTILINE | DOTALL))
        c += len(findall("<{0}[^<>]*?/>".format(tag),
                         page, MULTILINE | DOTALL))
        return c


handler = ParserHandler()
processor = Parser.Processor(handler)
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
