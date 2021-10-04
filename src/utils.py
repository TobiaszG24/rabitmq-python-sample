import pika

credentials = pika.PlainCredentials('ezarzadzanie', 'changeme')
parameters = pika.ConnectionParameters('rabbitmq', 5672, '/', credentials)
