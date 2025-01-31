# Publish/Subscribe
Deliver a message to multiple consumers.

## Exchanges
A producer can never send a message direct to the queue, instead it will send
that to an exchange.

There are few exchange type named: *direct*, *topic*, *headers*, *fanout*.

## Temporary queues
Giving a queue a name is important when we want to share the quey between producers
and consumers.

When provided an empty string as queue name while declaring queue, Rabbit will
assign a random name to the queue.

```py
result = channel.queue_declare(queue='')
# print(result.method.queue)
```

If we want the queue to be deleted whenever the consumer connection is closed,
the queue should be deleted, then we have to use `exclusive=True`.

```py
channel.queue_declare(queue='', exclusive=True)
```

## Bindings
The relationship between queue and exchange is called a *binding*.

```py
channel.exchange_declare(exchange='logs', exchange_type='fanout')
result = channel.queue_declare(queue='')

channel.queue_bind(exchange='logs', queue=result.method.queue)
```

# CLI
```sh
# producer
poetry run producer -m "I am dummy"
producer -m "I am dummy"

# consumer
poetry run consumer
consumer
```
