#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Messiah'

import xmlrpclib

proxy = xmlrpclib.ServerProxy("http://localhost:8080")
while True:
    print "===================\nQuadratic solver"
    try:
        a, b, c = (float(raw_input("Enter A: ")),
                   float(raw_input("Enter B: ")),
                   float(raw_input("Enter C: ")))
        if a == b == c == 0:
            break
        print "Roots for {0}x^2 + ({1})x + ({2})".format(a, b, c)
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
        print "are x1 = {0}, x2 = {1}".format(x1, x2)