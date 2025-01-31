# Routing
Routing helps to subscribe to a subset of messages.

## Direct exchange
This exchange type depicts the scenario where a message goes to the queues whose
*binding key* exactly matches the *routing key* of the message.

## Multiple bindings
If multiple matched binding_key found, then direct exchange behaves like fanout.


# CLI
```sh
producer -m "[error] Connection failed with return code 12." -s "error"
consumer -s "error"
```
