import os
import sys

import pika


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)


def main():
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host="localhost")
        )
        channel = connection.channel()

        channel.queue_declare(queue="rpc_queue")

        def on_request(ch, method, props, body):
            n = int(body)

            response = fib(n)

            ch.basic_publish(
                exchange="",
                routing_key=props.reply_to,
                properties=pika.BasicProperties(correlation_id=props.correlation_id),
                body=str(response),
            )
            ch.basic_ack(delivery_tag=method.delivery_tag)

        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue="rpc_queue", on_message_callback=on_request)

        print(" [x] Awaiting RPC requests")
        channel.start_consuming()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except:
            os._exit(0)


if __name__ == "__main__":
    main()
