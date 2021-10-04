import pika, sys, os
from utils import parameters
import logging

logging.basicConfig(filename='logs/consumer.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

def main():
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        logging.warning(" [x] Received %r" % body)

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logging.warning('Keyboard Interrupt')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)