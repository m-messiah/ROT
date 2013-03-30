#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Messiah'
HOST = "localhost"
PORT = 8080

import xmlrpclib

proxy = xmlrpclib.ServerProxy("http://{}:{}".format(HOST, PORT))
while True:
    print "===================\nQuadratic solver"
    try:
        a, b, c = (float(raw_input("Enter A: ")),
                   float(raw_input("Enter B: ")),
                   float(raw_input("Enter C: ")))
        if a == b == c == 0:
            break
        print "Roots for {}x^2 + ({})x + ({})".format(a, b, c)
    except ValueError:
        print "Incorrect input"
        continue

    try:
        x1, x2 = proxy.solve(a, b, c)
        x1, x2 = float(x1), float(x2)
    except ValueError:
        print x1
        continue
    except Exception as e:
        print "Something wrong with server: ", e
    else:
        print "are x1 = {}, x2 = {}".format(x1, x2)
