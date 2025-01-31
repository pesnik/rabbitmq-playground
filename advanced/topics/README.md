# Topics
This helps when the routing needs to be done with multiple criteria.

## Topic exchange
Messages sent to a topic exchange can't have an arbitrary routing_key - it must
be a list of words, delimited by dots. A few valid routing key examples:
stock.usd.nyse, nyse.vmw, quick.orange.rabbit.

there are two important special cases for binding keys:

- * (star) can substitute for exactly one word.
- # (hash) can substitute for zero or more words.

# CLI
```sh
producer -t "kern.critical" -m "A critical kernel error"
consumer -t "#"
consumer -t "*.critical"
```
