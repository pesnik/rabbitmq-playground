import os
import sys
import time

import pika


def main():
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host="localhost")
        )
        channel = connection.channel()

        channel.exchange_declare(exchange="logs", exchange_type="fanout")

        result = channel.queue_declare(queue="", durable=True, exclusive=True)
        queue_name = result.method.queue

        channel.queue_bind(exchange="logs", queue=queue_name)

        def callback(ch, method, properties, body):
            response_time = body.count(b".")
            print(f" [x] Received {body.decode()}")
            time.sleep(response_time)
            print(f" [x] Done after {response_time} seconds")
            ch.basic_ack(delivery_tag=method.delivery_tag)

        channel.basic_consume(queue=queue_name, on_message_callback=callback)

        print(" [*] Waiting for messages. To exit press CTRL+C")
        channel.start_consuming()

    except KeyboardInterrupt:
        print("Interrupt")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)


if __name__ == "__main__":
    main()
