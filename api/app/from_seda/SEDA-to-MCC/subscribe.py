#!/usr/bin/env python
import pika
import requests
import json

credentials = pika.PlainCredentials('signals', 'insecure')
parameters = pika.ConnectionParameters('localhost',
                                       5672,
                                       'vhost',
                                       credentials)

def callback(ch, method, properties, body):
    with open('file.json') as local_file:
        local_file.write(json.dumps(body))

    # print(" [x] Received %r" % body)
    print("Received !!!!!")

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='hello1', durable=True)

channel.basic_consume(queue='hello1', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
