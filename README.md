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
├── deployment/
│   ├── docker/
│   │   ├── standalone/
│   │   │   ├── Dockerfile
│   │   │   ├── docker-compose.yml
│   │   │   └── README.md
│   │   ├── cluster/
│   │   │   ├── Dockerfile
│   │   │   ├── docker-compose.yml
│   │   │   └── README.md
│   │   └── custom/
│   │       ├── Dockerfile
│   │       ├── docker-compose.yml
│   │       └── README.md
│   ├── kubernetes/
│   │   ├── standalone/
│   │   │   ├── deployment.yaml
│   │   │   ├── service.yaml
│   │   │   ├── configmap.yaml
│   │   │   └── README.md
│   │   ├── cluster/
│   │   │   ├── statefulset.yaml
│   │   │   ├── service.yaml
│   │   │   ├── configmap.yaml
│   │   │   ├── pvc.yaml
│   │   │   └── README.md
│   │   └── helm/
│   │       ├── Chart.yaml
│   │       ├── values.yaml
│   │       ├── templates/
│   │       │   ├── deployment.yaml
│   │       │   ├── service.yaml
│   │       │   ├── configmap.yaml
│   │       │   └── pvc.yaml
│   │       └── README.md
│   ├── terraform/
│   │   ├── aws/
│   │   │   ├── main.tf
│   │   │   ├── variables.tf
│   │   │   ├── outputs.tf
│   │   │   └── README.md
│   │   ├── gcp/
│   │   │   ├── main.tf
│   │   │   ├── variables.tf
│   │   │   ├── outputs.tf
│   │   │   └── README.md
│   │   └── azure/
│   │       ├── main.tf
│   │       ├── variables.tf
│   │       ├── outputs.tf
│   │       └── README.md
│   └── README.md
├── basic/
│   ├── hello-world/
│   ├── work-queues/
│   └── pub-sub/
├── advanced/
│   ├── routing/
│   ├── topics/
│   ├── rpc/
│   └── dead-letter/
├── patterns/
│   ├── competing-consumers/
│   ├── priority-queue/
│   └── retry-mechanism/
├── production-ready/
│   ├── high-availability/
│   ├── monitoring/
│   └── security/
└── industry-solutions/
    ├── distributed-commerce/
    │   ├── order-orchestration/    # FastAPI service
    │   ├── inventory-management/   # Django service
    │   ├── payment-gateway/        # Spring Boot service
    │   └── notification-engine/    # Node.js service
    │
    ├── stream-analytics-engine/
    │   ├── event-ingestion/        # Flask service
    │   ├── stream-processor/       # Python service
    │   └── metrics-dashboard/      # React app
    │
    ├── realtime-collaboration-platform/
    │   ├── messaging-core/         # WebSocket server
    │   ├── presence-orchestrator/  # User state management
    │   └── archive-service/        # Message persistence
    │
    ├── distributed-media-processor/
    │   ├── ingestion-gateway/      # Upload handling
    │   ├── processing-cluster/     # Worker pool
    │   └── orchestration-service/  # Progress tracking
    │
    └── industrial-iot-platform/
        ├── device-orchestrator/    # MQTT integration
        ├── telemetry-processor/    # Stream processing
        ├── monitoring-service/     # Alert system
        └── analytics-gateway/      # Time-series API
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

## Industry Solutions Overview

### 1. Distributed Commerce Platform
Enterprise-grade distributed transaction system:
- Order orchestration with saga pattern
- Distributed inventory management
- Payment processing integration
- Notification orchestration
- Priority-based message routing
- Transaction consistency patterns

### 2. Stream Analytics Engine
High-throughput event processing system:
- Event ingestion pipeline
- Real-time stream processing
- Aggregation algorithms
- Live metrics visualization
- Event sourcing patterns

### 3. Realtime Collaboration Platform
Enterprise messaging infrastructure:
- WebSocket integration layer
- State synchronization
- Message persistence architecture
- Presence management system
- Offline data handling

### 4. Distributed Media Processor
Scalable media processing framework:
- Multi-stage processing pipeline
- Worker pool orchestration
- Progress tracking system
- Error recovery mechanisms
- Result aggregation patterns

### 5. Industrial IoT Platform
Enterprise IoT message handling system:
- Protocol bridge architecture
- Telemetry processing pipeline
- Monitoring and alerting system
- Time-series data management
- Device state orchestration

## Implementation Standards

Each solution includes:
1. System architecture documentation
2. Service-specific implementation guides
3. Container orchestration configuration
4. Integration test suites
5. Performance analysis
6. Monitoring implementation
7. Failure recovery scenarios
8. API specifications

## Technology Stack

Solutions showcase RabbitMQ integration with:
- Python (FastAPI, Flask, Django)
- Java (Spring Boot)
- Node.js (Express, NestJS)
- Go (Performance-critical services)
- React/Vue.js (Frontend implementations)
- PostgreSQL, MongoDB, Redis (Data layer)

## Learning Objectives

Each solution emphasizes:
1. Enterprise messaging patterns
2. Fault tolerance strategies
3. Scalability architectures
4. System observability
5. Security implementations
6. Data consistency mechanisms
7. Integration architectures

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
