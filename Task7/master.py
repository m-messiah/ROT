#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

__author__ = 'Messiah'

from pika import BlockingConnection, ConnectionParameters, BasicProperties
import random
from IN import INT64_MAX, INT64_MIN
import logging

logging.basicConfig()


def main(a, b):
    connection = BlockingConnection(ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='calc', durable=True)

    message = "{}+{}".format(a, b)

    channel.basic_publish(exchange='',
                          routing_key='calc',
                          body=message,
                          properties=BasicProperties(
                              delivery_mode=2,  # make message persistent
                          ))

    print " [x] Sent {}".format(message)


if __name__ == '__main__':
    if len(sys.argv) > 2:
        main(sys.argv[1], sys.argv[2])
    else:
        main(random.randint(INT64_MIN, INT64_MAX),
             random.randint(INT64_MIN, INT64_MAX))