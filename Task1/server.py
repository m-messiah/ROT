#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket

HOST = ''
PORT = 27001
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
while True:
    conn, addr = s.accept()
    print 'Connected by', addr
    while True:
        data = ""
        c = ''
        while c != '\n':
            c = conn.recv(1)
            if c:
                data += c
            else:
                break
        if data and data != "quit\n":
            try:
                conn.sendall("{0}\n".format(eval(data.strip())))
            except:
                conn.sendall("Invalid input\n")
        else:
            break
    conn.close()
