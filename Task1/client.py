#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import socket


class Client(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def connect(self):
        self.sock = socket.create_connection((self.host, self.port))

    def send_request(self, req):
        return self.sock.send("{}\n".format(req).encode())

    def get_reply(self):
        recv = self.sock.recv(512)
        return recv.decode()


def print_help(argv):
    usage = "Usage: {0} host port".format(argv[0])
    print(usage)


def main():
    if len(sys.argv) != 3:
        print_help(sys.argv)
        sys.exit(1)
    host, port = sys.argv[1:3]
    client = Client(host, port)
    client.connect()
    while True:
        req = input("Client> ")
        client.send_request(req)
        if req == "quit":
            break
        print("Server> {0}".format(client.get_reply().strip()))


if __name__ == "__main__":
    main()
