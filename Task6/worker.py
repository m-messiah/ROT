#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Messiah'

import zmq


class Worker():
    def __init__(self, port1, port2):
        self.context = zmq.Context()
        self.input = self.context.socket(zmq.SUB)
        self.input.connect("tcp://127.0.0.1:{}".format(port1))
        self.input.setsockopt(zmq.SUBSCRIBE, "")
        self.output = self.context.socket(zmq.PUB)
        self.output.bind("tcp://127.0.0.1:{}".format(port2))
        self.queue = []

    def run(self):
        while True:
            try:
                self.queue.append(self.input.recv(zmq.NOBLOCK))
            except zmq.core.error.ZMQError:
                pass
            if self.queue:
                for msg in self.queue:
                    if msg == "exit":
                        self.output.send("exit")
                    else:
                        self.output.send("{} = {}".format(msg, eval(msg)))
                    self.queue.remove(msg)

if __name__ == "__main__":
    W = Worker(5000, 6000)
    W.run()
