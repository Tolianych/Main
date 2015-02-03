'''
Created on May 26, 2014

@author: s.botyan
'''
import pika
import logging
import time

hour = 3600

logging.basicConfig()

credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('bear.pyn.ru', 5672, credentials = credentials)

connection = pika.BlockingConnection(parameters)
print "Connected!"
channel = connection.channel()

#channel.basic_publish(exchange='mobile_notifier', routing_key='mobile_notifier.messages', body='{"foundQty":2241,"applicantId":18669440,"vacancySavedSearchId":6285801}')
while hour > 0:
    i = 50
    while i > 0:
        channel.basic_publish(exchange='mobile_notifier', routing_key='vacancySavedSearch.performed', body='{"foundQty":2241,"applicantId":18669440,"vacancySavedSearchId":6285801}')
        i -= 1
    time.sleep(1)
    if hour % 60 == 0:
        minutes = hour / 60
        print "Estimate: " + str(minutes) + " min."
    hour -= 1
print "Sent!"

connection.close()