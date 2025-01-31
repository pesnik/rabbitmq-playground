import pika
import sys
import os


def main():
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host="localhost"))
        channel = connection.channel()

        channel.queue_declare("hello")

        def callback(ch, method, properties, body):
            print(f" [x] Received {body}")

        channel.basic_consume(queue='hello',
                            auto_ack=True,
                            on_message_callback=callback)

        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)


if __name__ == '__main__':
    main()
