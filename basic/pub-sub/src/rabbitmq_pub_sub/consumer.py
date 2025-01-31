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

        channel.queue_declare(queue="pub-sub", durable=True)

        def callback(ch, method, properties, body):
            response_time = body.count(b".")
            print(f" [x] Received {body.decode()}")
            time.sleep(response_time)
            print(f" [x] Done after {response_time} seconds")
            ch.basic_ack(delivery_tag=method.delivery_tag)

        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue="pub-sub", on_message_callback=callback)

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
