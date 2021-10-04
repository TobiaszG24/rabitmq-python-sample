from time import sleep
import pika
from utils import parameters
import logging

logging.basicConfig(filename='logs/publisher.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

connection = pika.BlockingConnection(parameters)

channel = connection.channel()

channel.queue_declare(queue='hello')

logging.warning("started, sleep 10 seconds")
sleep(10)

channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
logging.warning(" [x] Sent 'Hello World!'")

connection.close()