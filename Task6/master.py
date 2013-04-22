#!/usr/bin/python
# -*- coding: utf-8 -*-
from IN import INT64_MAX, INT64_MIN

__author__ = 'Messiah'

import zmq
import random
REPEATS = 100


class Master():
    def __init__(self, port1, port2):
        self.context = zmq.Context()
        self.output = self.context.socket(zmq.PUB)
        self.output.bind("tcp://127.0.0.1:{}".format(port1))
        self.input = self.context.socket(zmq.SUB)
        self.input.connect("tcp://127.0.0.1:{}".format(port2))
        self.input.setsockopt(zmq.SUBSCRIBE, "")

    def run(self):
        self.output.send("hello")
        for i in range(REPEATS):
            #msg = "{}**{}".format(random.randint(0, INT64_MAX),
            #                     random.randint(10000, 20000))
            msg = "{}+{}".format(random.randint(INT64_MIN, INT64_MAX),
                                 random.randint(INT64_MIN, INT64_MAX))
            self.output.send(msg)
            print msg
            for i in range(100000):
                try:
                    msg = self.input.recv(zmq.NOBLOCK)
                except zmq.core.error.ZMQError:
                    pass
                else:
                    print msg

        self.output.send("exit")
        print "exit"
        while True:
            try:
                msg = self.input.recv(zmq.NOBLOCK)
            except zmq.core.error.ZMQError:
                pass
            else:
                if msg == "exit":
                    return
                print msg


if __name__ == "__main__":
    M = Master(5000, 6000)
    M.run()
