import argparse
import os
import sys

import pika


def consume(severity):
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()

    channel.exchange_declare(exchange="direct_logs", exchange_type="direct")

    result = channel.queue_declare(queue="", exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange="direct_logs", queue=queue_name, routing_key=severity)

    def callback(ch, method, properties, body):
        print(f" [x] Received {body.decode()}")

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    print(" [*] Waiting for logs. To exit press CTRL+C")

    channel.start_consuming()


def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("-s", "--severity", dest="severity")

        args = parser.parse_args()

        if args.severity:
            severity = args.severity
        else:
            severity = "info"

        consume(severity)
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)


if __name__ == "__main__":
    main()
