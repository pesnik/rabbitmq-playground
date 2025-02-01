import argparse
import uuid

import pika


class RpcClient(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host="localhost")
        )
        self.channel = self.connection.channel()

        queue = self.channel.queue_declare(queue="", exclusive=True)
        self.callback_queue = queue.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True,
        )

        self.response = None
        self.corr_id = None

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n) -> bytes:
        self.response = None
        self.corr_id = str(uuid.uuid4())

        self.channel.basic_publish(
            exchange="",
            routing_key="rpc_queue",
            properties=pika.BasicProperties(
                reply_to=self.callback_queue, correlation_id=self.corr_id
            ),
            body=str(n),
        )

        while self.response is None:
            self.connection.process_data_events(time_limit=30)

        return self.response


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", dest="fib")

    args = parser.parse_args()
    if args.fib:
        n = args.fib
    else:
        n = 5

    client = RpcClient()

    response = client.call(n)
    print(f" [.] Fibonacci({n}): {response.decode()}")


if __name__ == "__main__":
    main()
