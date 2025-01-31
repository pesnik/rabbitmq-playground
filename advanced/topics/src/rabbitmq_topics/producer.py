import argparse

import pika


def send_message(message, severity):
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()

    channel.exchange_declare(exchange="topic_logs", exchange_type="topic")

    channel.basic_publish(exchange="topic_logs", routing_key=severity, body=message)
    print(f" [x] Sent [{severity}] {message}")

    connection.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--message", dest="message")
    parser.add_argument("-t", "--topic", dest="topic")

    args = parser.parse_args()

    if args.message and args.topic:
        message = args.message
        severity = args.topic
    else:
        message = "[info] getting connection <ip>:<port>"
        severity = "info"

    send_message(message, severity)


if __name__ == "__main__":
    main()
