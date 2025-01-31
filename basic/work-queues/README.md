# Work Queues
The main purpose of using work queues is to avoid doing a resource-intensive task
immediately and having to wait for it to complete. Instead we schedule the task
to be done later. We encapsulate a _task_ as a message and send it to the queue.
A worker process running in the background will pop the tasks and eventually
execute the job. When we run many workers the tasks will be shared between them.

## Round-robin dispatching
By default, RabbitMQ will send each message to the next consumer, in sequence.

## Message acknowledgement
If not handled, once RabbitMQ delivers a message to the consumer, it immediately
marks it for deletion.

## Message durability
When RabbitMQ crashes it will forget the queues unless we tell it not to. In this
case we need to mark both the queue and the messages as durable.

```py
channel.queue_declare(queue='task_queue', durable=True)

channel.basic_publish(exchange='',
                        routing_key='task_queue',
                        body=message,
                        properties=pika.BasicProperties(
                            delivery_mode = pika.DeliveryMode.Persistent
                        ))
```

# Fair Dispatch
By default RabbitMQ will do round-robin dispatch. If we use the Channel#basic_qos
method with `prefetch_count=1`, then RabbitMQ won't give more than one message to a
worker i.e until a worker processed and acknowledged the previous one, don't dispatch
a message to this worker.

```py
channel.basic_qos(prefetch_count=1)
```
NB: we may need to use message TTL.

# Commands
```sh
poetry run producer
poetry run consumer
```

## Command Options for Producer
```sh
poetry run producer Hello World...
poetry run producer "Hello, Pesnik."
poetry run producer -m "Hello World."
poetry run producer --message "Hello World"
```
