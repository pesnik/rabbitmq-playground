import pika

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()

    channel.queue_declare(queue="hello")

    channel.basic_publish(exchange='',
                        routing_key='hello',
                        body='hello world!')
    print("[x] sent hello-world")

    connection.close()

if __name__ == '__main__':
    main()
