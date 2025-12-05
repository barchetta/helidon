# Overview

Connecting streams to Kafka with Reactive Messaging is easy to do. There
is a standard Kafka client behind the scenes, all the
[producer](https://kafka.apache.org/28/documentation.html#producerconfigs)
and
[consumer](https://kafka.apache.org/28/documentation.html#consumerconfigs)
configs can be propagated through messaging config.

# Maven Coordinates

To enable Reactive Kafka Connector, add the following dependency to your
project’s `pom.xml` (see [Managing
Dependencies](../../about/managing-dependencies.md)).

``` xml
<dependency>
    <groupId>io.helidon.messaging.kafka</groupId>
    <artifactId>helidon-messaging-kafka</artifactId>
</dependency>
```

# Config Example

<div class="formalpara">

<div class="title">

Example of connector config:

</div>

``` yaml
mp.messaging:

  incoming.from-kafka:
    connector: helidon-kafka
    topic: messaging-test-topic-1
    auto.offset.reset: latest 
    enable.auto.commit: true
    group.id: example-group-id

  outgoing.to-kafka:
    connector: helidon-kafka
    topic: messaging-test-topic-1

  connector:
    helidon-kafka:
      bootstrap.servers: localhost:9092 
      key.serializer: org.apache.kafka.common.serialization.StringSerializer
      value.serializer: org.apache.kafka.common.serialization.StringSerializer
      key.deserializer: org.apache.kafka.common.serialization.StringDeserializer
      value.deserializer: org.apache.kafka.common.serialization.StringDeserializer
```

</div>

- Kafka client consumer’s property auto.offset.reset configuration for
  `from-kafka` channel only

- Kafka client’s property
  [bootstrap.servers](https://kafka.apache.org/28/documentation.html#consumerconfigs_bootstrap.servers)
  configuration for all channels using the connector

<div class="formalpara">

<div class="title">

Example of consuming from Kafka:

</div>

``` java
@Incoming("from-kafka")
public void consumeKafka(String msg) {
    System.out.println("Kafka says: " + msg);
}
```

</div>

<div class="formalpara">

<div class="title">

Example of producing to Kafka:

</div>

``` java
@Outgoing("to-kafka")
public PublisherBuilder<String> produceToKafka() {
    return ReactiveStreams.of("test1", "test2");
}
```

</div>

# NACK Strategy

|  |  |
|----|----|
| Strategy | Description |
| Kill channel | Nacked message sends error signal and causes channel failure so Messaging Health check can report it as DOWN |
| DLQ | Nacked messages are sent to specified dead-letter-queue |
| Log only | Nacked message is logged and channel continues normally |

## Kill channel

Default NACK strategy for Kafka connector. When

## Dead Letter Queue

Sends nacked messages to error topic,
[DLQ](https://en.wikipedia.org/wiki/Dead_letter_queue) is well known
pattern for dealing with unprocessed messages.

Helidon can derive connection settings for DLQ topic automatically if
the error topic is present on the same Kafka cluster. Serializers are
derived from deserializers used for consumption
`org.apache.kafka.common.serialization.StringDeserializer` \>
`org.apache.kafka.common.serialization.StringSerializer`. Note that the
name of the error topic is needed only in this case.

<div class="formalpara">

<div class="title">

Example of derived DLQ config:

</div>

``` yaml
mp.messaging:
  incoming:
    my-channel:
      nack-dlq: dql_topic_name
```

</div>

If a custom connection is needed, then use the 'nack-dlq' key for all of
the producer configuration.

<div class="formalpara">

<div class="title">

Example of custom DLQ config:

</div>

``` yaml
mp.messaging:
  incoming:
    my-channel:
      nack-dlq:
        topic: dql_topic_name
        bootstrap.servers: localhost:9092
        key.serializer: org.apache.kafka.common.serialization.StringSerializer
        value.serializer: org.apache.kafka.common.serialization.StringSerializer
```

</div>

## Log only

Only logs nacked messages and throws them away, offset is committed and
channel continues normally consuming subsequent messages.

<div class="formalpara">

<div class="title">

Example of log only enabled nack strategy

</div>

``` yaml
mp.messaging:
  incoming:
    my-channel:
      nack-log-only: true
```

</div>

# Examples

Don’t forget to check out the examples with pre-configured Kafka docker
image, for easy testing:

- <https://github.com/helidon-io/helidon-examples/tree/helidon-4.x/examples/messaging>
