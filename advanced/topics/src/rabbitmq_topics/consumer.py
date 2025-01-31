import argparse
import os
import sys

import pika


def consume(topic):
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()

    channel.exchange_declare(exchange="topic_logs", exchange_type="topic")

    result = channel.queue_declare(queue="", exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange="topic_logs", queue=queue_name, routing_key=topic)

    def callback(ch, method, properties, body):
        print(f" [x] {method.routing_key}:{body.decode()}")

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    print(" [*] Waiting for logs. To exit press CTRL+C")

    channel.start_consuming()


def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("-t", "--topic", dest="topic")

        args = parser.parse_args()

        if args.topic:
            topic = args.topic
        else:
            topic = "info"

        consume(topic)
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)


if __name__ == "__main__":
    main()
