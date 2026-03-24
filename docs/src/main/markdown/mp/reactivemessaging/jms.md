# JMS Connector

## Contents

- [Overview](#_overview)

- [Maven Coordinates](#maven-coordinates)

- [Configuration](#_configuration)

- [Usage](#_usage)

## Overview

Connecting streams to JMS with Reactive Messaging couldn’t be easier.

## Maven Coordinates

To enable JMS Connector, add the following dependency to your project’s `pom.xml` (see [Managing Dependencies](../../about/managing-dependencies.md)).

``` xml
<dependency>
    <groupId>io.helidon.messaging.jms</groupId>
    <artifactId>helidon-messaging-jms</artifactId>
</dependency>
```

## Configuration

Connector name: `helidon-jms`

Type: [io.helidon.messaging.connectors.jms.JmsConfigBuilder](/apidocs/io.helidon.messaging.connectors.jms/io/helidon/messaging/connectors/jms/JmsConfigBuilder.html)

### Configuration options

<table style="width:100%;">
<caption>Optional configuration options</caption>
<colgroup>
<col style="width: 23%" />
<col style="width: 23%" />
<col style="width: 15%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">key</th>
<th style="text-align: left;">type</th>
<th style="text-align: left;">default value</th>
<th style="text-align: left;">description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>acknowledge-mode</code></p></td>
<td style="text-align: left;"><p>AcknowledgeMode (AUTO_ACKNOWLEDGE, CLIENT_ACKNOWLEDGE, DUPS_OK_ACKNOWLEDGE)</p></td>
<td style="text-align: left;"><p><code>AUTO_ACKNOWLEDGE</code></p></td>
<td style="text-align: left;"><p>JMS acknowledgement mode.</p>
<ul>
<li><p><strong>AUTO_ACKNOWLEDGE</strong> Acknowledges automatically after message reception over JMS api.</p></li>
<li><p><strong>CLIENT_ACKNOWLEDGE</strong> Message is acknowledged when org.eclipse.microprofile.reactive.messaging.Message.ack Message.ack() is invoked either manually or by org.eclipse.microprofile.reactive.messaging.Acknowledgment Acknowledgment policy.</p></li>
<li><p><strong>DUPS_OK_ACKNOWLEDGE</strong> Messages are acknowledged lazily which can result in duplicate messages being delivered.</p></li>
</ul>
<p>Allowed values:</p>
<ul>
<li><p><code>AUTO_ACKNOWLEDGE</code>: Acknowledges automatically after message reception over JMS api.</p></li>
<li><p><code>CLIENT_ACKNOWLEDGE</code>: Message is acknowledged when org.eclipse.microprofile.reactive.messaging.Message.ack is invoked either manually or by org.eclipse.microprofile.reactive.messaging.Acknowledgment policy.</p></li>
<li><p><code>DUPS_OK_ACKNOWLEDGE</code>: Messages are acknowledged lazily which can result in duplicate messages being delivered.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>destination</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Queue or topic name.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>jndi-initial-context-properties</code></p></td>
<td style="text-align: left;"><p>Map&lt;string, string&gt;</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Environment properties used for creating initial context java.naming.factory.initial, java.naming.provider.url.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>jndi-initial-factory</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>JNDI initial factory.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>jndi-jms-factory</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>JNDI name of JMS factory.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>jndi-provider-url</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>JNDI provider url.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>message-selector</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>JMS API message selector expression based on a subset of the SQL92. Expression can only access headers and properties, not the payload.</p>
<ul>
<li><p>Type: string</p></li>
<li><p>Example: NewsType = ’Sports’ OR NewsType = ’Opinion’</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>named-factory</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>To select from manually configured jakarta.jms.ConnectionFactory ConnectionFactories over {@link JmsConnector.JmsConnectorBuilder#connectionFactory(String, jakarta.jms.ConnectionFactory) JmsConnectorBuilder#connectionFactory()}.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>password</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Password used for creating JMS connection.</p>
<ul>
<li><p>Type: string</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>period-executions</code></p></td>
<td style="text-align: left;"><p>long</p></td>
<td style="text-align: left;"><p><code>100</code></p></td>
<td style="text-align: left;"><p>Period for executing poll cycles in millis.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>poll-timeout</code></p></td>
<td style="text-align: left;"><p>long</p></td>
<td style="text-align: left;"><p><code>50</code></p></td>
<td style="text-align: left;"><p>Timeout for polling for next message in every poll cycle in millis.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>queue</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Use supplied destination name and Type.QUEUE QUEUE as type.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>session-group-id</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>When multiple channels share same session-group-id, they share same JMS session.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>topic</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Use supplied destination name and Type.TOPIC TOPIC as type.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>transacted</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>Indicates whether the session will use a local transaction.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p>Type (QUEUE, TOPIC)</p></td>
<td style="text-align: left;"><p><code>QUEUE</code></p></td>
<td style="text-align: left;"><p>Specify if connection is Type.QUEUE queue or Type.TOPIC topic.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>QUEUE</code>: Queue connection type, every message is consumed by one client only.</p></li>
<li><p><code>TOPIC</code>: Topic connection type, every message is delivered to all subscribed clients.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>username</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>User name used for creating JMS connection.</p>
<ul>
<li><p>Type: string</p></li>
</ul></td>
</tr>
</tbody>
</table>

> [!TIP]
> Besides the configuration options above, custom attributes can be passed over configuration.

|  |  |
|----|----|
| `jndi.destination` | JNDI destination identifier. |
| `jndi.env-properties` | Environment properties used for creating initial context `java.naming.factory.initial`, `java.naming.provider.url` …​ |
| `producer.someproperty` | property with producer prefix is set to producer instance (for example WLS Unit-of-Order `WLMessageProducer.setUnitOfOrder("unit-1")` can be configured as `producer.unit-of-order=unit-1`) |

Custom Attributes Examples

### Configured JMS factory

The simplest possible usage is looking up JMS ConnectionFactory in the naming context.

*Example of connector config:*

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

### Injected JMS factory

In case you need more advanced setup, connector can work with injected factory instance.

*Inject:*

``` java
@Produces
@ApplicationScoped
@Named("active-mq-factory")
public ConnectionFactory connectionFactory() {
    return new ActiveMQConnectionFactory(config.get("jms.url").asString().get());
}
```

*Config:*

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

## Usage

### Consuming

*Consuming one by one unwrapped value:*

``` java
@Incoming("from-jms")
public void consumeJms(String msg) {
    System.out.println("JMS says: " + msg);
}
```

*Consuming one by one, manual ack:*

``` java
@Incoming("from-jms")
@Acknowledgment(Acknowledgment.Strategy.MANUAL)
public CompletionStage<Void> consumeJms(JmsMessage<String> msg) {
    System.out.println("JMS says: " + msg.getPayload());
    return msg.ack();
}
```

### Producing

*Example of producing to JMS:*

``` java
@Outgoing("to-jms")
public PublisherBuilder<String> produceToJms() {
    return ReactiveStreams.of("test1", "test2");
}
```

*Example of more advanced producing to JMS:*

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

*Example of even more advanced producing to JMS with custom mapper:*

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
