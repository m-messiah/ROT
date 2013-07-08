#!/usr/bin/python3
# -*- coding: utf-8 -*-
import math
from xmlrpc.server import SimpleXMLRPCServer

__author__ = 'Messiah'
HOST = "localhost"
PORT = 8080


class Solver(object):
    def __init__(self):
        pass

    def solve(self, a=0, b=0, c=0):
        try:
            a, b, c = (float(a),
                       float(b),
                       float(c))
        except ValueError:
            return "Incorrect input", 0
        if a == 0:
            return "It's not a quadratic equation", 0
        D = b ** 2 - 4 * a * c
        if D < 0:
            return "Not real roots", 0
        x1 = (-b + math.sqrt(D)) / 2 / a
        if D == 0:
            x2 = x1
        else:
            x2 = (-b - math.sqrt(D)) / 2 / a
        return x1, x2


if __name__ == "__main__":
    server = SimpleXMLRPCServer((HOST, PORT))
    print("Listening on", PORT)
    S = Solver()
    server.register_function(S.solve, "solve")
    server.serve_forever()
