# RabbitMQ Playground

This repository serves as a practical playground for exploring and mastering RabbitMQ, an open-source message broker that supports multiple messaging protocols. Through this playground, you'll learn message queuing patterns, exchange types, and best practices for building robust distributed systems.

## Learning Objectives

- Understand core RabbitMQ concepts and components
- Master different exchange types (Direct, Fanout, Topic, Headers)
- Implement various messaging patterns
- Handle message persistence and durability
- Practice error handling and dead letter exchanges
- Explore message routing strategies
- Implement reliable publishing and consuming patterns

## Project Structure

```
rabbitmq-playground/
├── basic/
│   ├── hello-world/         # Simple producer/consumer example
│   ├── work-queues/         # Task distribution scenarios
│   └── pub-sub/             # Basic publish/subscribe patterns
├── advanced/
│   ├── routing/             # Direct and topic exchange examples
│   ├── rpc/                 # Remote procedure call pattern
│   └── dead-letter/         # Dead letter exchange handling
├── patterns/
│   ├── competing-consumers/ # Load balancing across consumers
│   ├── priority-queue/      # Message prioritization
│   └── retry-mechanism/     # Failed message retry implementation
└── production-ready/
    ├── high-availability/   # Clustering and mirroring
    ├── monitoring/          # Health checks and monitoring
    └── security/            # SSL/TLS and authentication
```

## Prerequisites

- Docker and Docker Compose
- Python 3.8+
- Pika (Python RabbitMQ client)
- Basic understanding of message queuing concepts

## Getting Started

1. Start RabbitMQ server using Docker:
```bash
docker-compose up -d
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Access RabbitMQ Management UI:
- URL: http://localhost:15672
- Default credentials: guest/guest

## Learning Path

### 1. Fundamentals
- Basic producer/consumer implementation
- Understanding queues and message acknowledgment
- Exploring message persistence
- Working with exchanges and bindings

### 2. Exchange Types
- Direct exchange for routing based on exact matching
- Fanout exchange for broadcast scenarios
- Topic exchange for pattern-based routing
- Headers exchange for attribute-based routing

### 3. Advanced Patterns
- Implementing reliable publishing
- Setting up dead letter exchanges
- Creating retry mechanisms
- Handling message priorities
- Building request-reply patterns

### 4. Production Considerations
- High availability setup
- Monitoring and alerting
- Security best practices
- Performance optimization

## Best Practices Covered

- Message persistence and durability
- Proper channel and connection handling
- Error handling and recovery
- Queue naming conventions
- Consumer acknowledgments
- Publisher confirms
- Flow control

## Contributing

Feel free to contribute additional examples, patterns, or improvements through pull requests.

## Resources

- [RabbitMQ Official Documentation](https://www.rabbitmq.com/documentation.html)
- [RabbitMQ Best Practices](https://www.rabbitmq.com/production-checklist.html)
- [Messaging Patterns](https://www.rabbitmq.com/getstarted.html)
