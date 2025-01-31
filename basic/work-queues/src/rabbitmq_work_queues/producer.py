import pika
import argparse

def send_message(message: str):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='work-queues')

    channel.basic_publish(exchange='', routing_key='work-queues', body=message)
    print(f" [x] Sent '{message}'")

    connection.close()


def main():
    parser = argparse.ArgumentParser(description='Send message to RabbitMQ queue')
    parser.add_argument('message', type=str, nargs='*', help='Message to send to the queue')
    parser.add_argument('-m', '--message', type=str, dest='message_flag', help='Alternative way to specify message using flag')

    args = parser.parse_args()

    if args.message_flag:
        message = args.message_flag
    else:
        message = ' '.join(args.message) if args.message else 'Hello...'

    send_message(message)

if __name__ == '__main__':
    main()
