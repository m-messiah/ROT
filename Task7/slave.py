#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Messiah'
from pika import BlockingConnection, ConnectionParameters


def main():
    connection = BlockingConnection(ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='calc', durable=True)
    print ' [*] Waiting for messages. To exit press CTRL+C'

    def callback(ch, method, properties, body):
        print " [x] Persistence {}".format(properties.delivery_mode == 2)
        print " [x] Received: {}".format(body)
        try:
            print " [.] Caclulated: {} = {}".format(body, eval(body))
        except SyntaxError:
            print " [.] Invalid syntax"
        print " [x] Done"
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(callback,
                          queue='calc')
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print "[*] Exit"
        return


if __name__ == '__main__':
    main()
