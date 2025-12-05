# Overview

Connecting streams to JMS with Reactive Messaging couldn’t be easier.

# Maven Coordinates

To enable JMS Connector, add the following dependency to your project’s
`pom.xml` (see [Managing
Dependencies](../../about/managing-dependencies.md)).

``` xml
<dependency>
    <groupId>io.helidon.messaging.jms</groupId>
    <artifactId>helidon-messaging-jms</artifactId>
</dependency>
```

# Configuration

Connector name: `helidon-jms`

|  |  |
|----|----|
| `username` | User name used to connect JMS session |
| `password` | Password to connect JMS session |
| `type` | Possible values are: `queue`, `topic` |
| `destination` | Queue or topic name |
| `acknowledge-mode` | Possible values are: `AUTO_ACKNOWLEDGE`- session automatically acknowledges a client’s receipt of a message, `CLIENT_ACKNOWLEDGE` - receipt of a message is acknowledged only when `Message.ack()` is called manually, `DUPS_OK_ACKNOWLEDGE` - session lazily acknowledges the delivery of messages. Default value: `AUTO_ACKNOWLEDGE` |
| `transacted` | Indicates whether the session will use a local transaction. Default value: `false` |
| `message-selector` | JMS API message selector expression based on a subset of the SQL92. Expression can only access headers and properties, not the payload. |
| `client-id` | Client identifier for JMS connection. |
| `durable` | True for creating durable consumer (only for topic). Default value: `false` |
| `subscriber-name` | Subscriber name for durable consumer used to identify subscription. |
| `non-local` | If true then any messages published to the topic using this session’s connection, or any other connection with the same client identifier, will not be added to the durable subscription. Default value: `false` |
| `named-factory` | Select in case factory is injected as a named bean or configured with name. |
| `poll-timeout` | Timeout for polling for next message in every poll cycle in millis. Default value: `50` |
| `period-executions` | Period for executing poll cycles in millis. Default value: `100` |
| `session-group-id` | When multiple channels share same `session-group-id`, they share same JMS session and same JDBC connection as well. |
| `jndi.jms-factory` | JNDI name of JMS factory. |
| `jndi.destination` | JNDI destination identifier. |
| `jndi.env-properties` | Environment properties used for creating initial context `java.naming.factory.initial`, `java.naming.provider.url` …​ |
| `producer.someproperty` | property with producer prefix is set to producer instance (for example WLS Unit-of-Order `WLMessageProducer.setUnitOfOrder("unit-1")` can be configured as `producer.unit-of-order=unit-1`) |

Attributes

## Configured JMS factory

The simplest possible usage is looking up JMS ConnectionFactory in the
naming context.

<div class="formalpara">

<div class="title">

Example of connector config:

</div>

``` yaml
mp.messaging:

  incoming.from-jms:
    connector: helidon-jms
    destination: messaging-test-queue-1
    type: queue

  outgoing.to-jms:
    connector: helidon-jms
    destination: messaging-test-queue-1
    type: queue

  connector:
    helidon-jms:
      user: Gandalf
      password: mellon
      jndi:
        jms-factory: ConnectionFactory
        env-properties:
          java.naming:
            factory.initial: org.apache.activemq.jndi.ActiveMQInitialContextFactory
            provider.url: tcp://localhost:61616
```

</div>

## Injected JMS factory

In case you need more advanced setup, connector can work with injected
factory instance.

<div class="formalpara">

<div class="title">

Inject:

</div>

``` java
@Produces
@ApplicationScoped
@Named("active-mq-factory")
public ConnectionFactory connectionFactory() {
    return new ActiveMQConnectionFactory(config.get("jms.url").asString().get());
}
```

</div>

<div class="formalpara">

<div class="title">

Config:

</div>

``` yaml
jms:
  url: tcp://127.0.0.1:61616

mp:
  messaging:
    connector:
      helidon-jms:
        named-factory: active-mq-factory

    outgoing.to-jms:
      connector: helidon-jms
      session-group-id: order-connection-1
      destination: TESTQUEUE
      type: queue

    incoming.from-jms:
      connector: helidon-jms
      session-group-id: order-connection-1
      destination: TESTQUEUE
      type: queue
```

</div>

# Usage

## Consuming

<div class="formalpara">

<div class="title">

Consuming one by one unwrapped value:

</div>

``` java
@Incoming("from-jms")
public void consumeJms(String msg) {
    System.out.println("JMS says: " + msg);
}
```

</div>

<div class="formalpara">

<div class="title">

Consuming one by one, manual ack:

</div>

``` java
@Incoming("from-jms")
@Acknowledgment(Acknowledgment.Strategy.MANUAL)
public CompletionStage<Void> consumeJms(JmsMessage<String> msg) {
    System.out.println("JMS says: " + msg.getPayload());
    return msg.ack();
}
```

</div>

## Producing

<div class="formalpara">

<div class="title">

Example of producing to JMS:

</div>

``` java
@Outgoing("to-jms")
public PublisherBuilder<String> produceToJms() {
    return ReactiveStreams.of("test1", "test2");
}
```

</div>

<div class="formalpara">

<div class="title">

Example of more advanced producing to JMS:

</div>

``` java
@Outgoing("to-jms")
public PublisherBuilder<Message<String>> produceToJms() {
    return ReactiveStreams.of("test1", "test2")
            .map(s -> JmsMessage.builder(s)
                    .correlationId(UUID.randomUUID().toString())
                    .property("stringProp", "cool property")
                    .property("byteProp", 4)
                    .property("intProp", 5)
                    .onAck(() -> CompletableFuture.completedStage(null)
                            .thenRun(() -> System.out.println("Acked!")))
                    .build());
}
```

</div>

<div class="formalpara">

<div class="title">

Example of even more advanced producing to JMS with custom mapper:

</div>

``` java
@Outgoing("to-jms")
public PublisherBuilder<Message<String>> produceToJms() {
    return ReactiveStreams.of("test1", "test2")
            .map(s -> JmsMessage.builder(s)
                    .customMapper((p, session) -> {
                        TextMessage textMessage = session.createTextMessage(p);
                        textMessage.setStringProperty("custom-mapped-property", "XXX" + p);
                        return textMessage;
                    })
                    .build()
            );
}
```

</div>
