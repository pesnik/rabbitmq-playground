import argparse

import pika


def send_message(message: str):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()

    channel.queue_declare(queue="pub-sub", durable=True)

    channel.basic_publish(
        exchange="",
        routing_key="pub-sub",
        body=message,
        properties=pika.BasicProperties(delivery_mode=pika.DeliveryMode.Persistent),
    )
    print(f" [x] Sent {message}")

    connection.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--message", dest="message")

    args = parser.parse_args()

    if args.message:
        message = args.message
    else:
        message = "Hello, pika."

    send_message(message)


if __name__ == "__main__":
    main()
