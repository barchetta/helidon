# Overview

Connecting streams to Oracle AQ with Reactive Messaging couldn’t be
easier. This connector extends Helidon’s JMS connector with Oracle’s
AQ-specific API.

# Maven Coordinates

To enable AQ Connector, add the following dependency to your project’s
`pom.xml` (see [Managing
Dependencies](../../about/managing-dependencies.md)).

``` xml
<dependency>
    <groupId>io.helidon.messaging.aq</groupId>
    <artifactId>helidon-messaging-aq</artifactId>
</dependency>
```

# Configuration

Connector name: `helidon-aq`

|  |  |
|----|----|
| `datasource` | name of the datasource bean used to connect Oracle DB with AQ |
| `url` | jdbc connection string used to connect Oracle DB with AQ (forbidden when `datasource` is specified) |
| `username` | User name used to connect Oracle DB with AQ (forbidden when `datasource` is specified) |
| `password` | Password to connect Oracle DB with AQ (forbidden when `datasource` is specified) |
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

Attributes

## Configured JMS Factory

The simplest possible usage is leaving construction of
`AQjmsConnectionFactory` to the connector.

<div class="formalpara">

<div class="title">

Example of connector config:

</div>

``` yaml
mp:
  messaging:

    connector:
      helidon-aq:
        transacted: false
        acknowledge-mode: CLIENT_ACKNOWLEDGE
        url: jdbc:oracle:thin:@(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(Host=192.168.0.123)(Port=1521))(CONNECT_DATA=(SID=TESTSID)))
        user: gandalf
        password: mellon

    outgoing.to-aq:
      connector: helidon-aq
      destination: TESTQUEUE
      type: queue

    incoming.from-aq:
      connector: helidon-aq
      destination: TESTQUEUE
      type: queue
```

</div>

Its also possible and preferable to refer to [configured
datasource](../persistence.md), in our example [Oracle UCP
datasource](../persistence.md):

<div class="formalpara">

<div class="title">

Example of connector config with Oracle UCP datasource:

</div>

``` yaml
javax:
  sql:
    DataSource:
      aq-test-ds:
        connectionFactoryClassName: oracle.jdbc.pool.OracleDataSource
        URL: jdbc:oracle:thin:@exampledb_high?TNS_ADMIN=/home/gandalf/wallets/Wallet_EXAMPLEDB
        user: gandalf
        password: SuperSecretPassword1234

mp:
  messaging:
    connector:
      helidon-aq:
        transacted: false
        acknowledge-mode: CLIENT_ACKNOWLEDGE
        data-source: aq-test-ds
    outgoing.toJms:
      connector: helidon-aq
      destination: TESTQUEUE
      type: queue
    incoming.fromJms:
      connector: helidon-aq
      destination: TESTQUEUE
      type: queue
```

</div>

## Injected JMS factory

If you need more advanced configurations, connector can work with
injected `AQjmsConnectionFactory`:

<div class="formalpara">

<div class="title">

Inject:

</div>

``` java
@Produces
@ApplicationScoped
@Named("aq-orderdb-factory")
public AQjmsConnectionFactory connectionFactory() throws JMSException {
    AQjmsQueueConnectionFactory fact = new AQjmsQueueConnectionFactory();
    fact.setJdbcURL(config.get("jdbc.url").asString().get());
    fact.setUsername(config.get("jdbc.user").asString().get());
    fact.setPassword(config.get("jdbc.pass").asString().get());
    return fact;
}
```

</div>

<div class="formalpara">

<div class="title">

Config:

</div>

``` yaml
jdbc:
  url: jdbc:oracle:thin:@(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(Host=192.168.0.123)(Port=1521))(CONNECT_DATA=(SID=TESTSID)))
  user: gandalf
  pass: mellon

mp:
  messaging:
    connector:
      helidon-aq:
        named-factory: aq-orderdb-factory

    outgoing.to-aq:
      connector: helidon-aq
      session-group-id: order-connection-1
      destination: TESTQUEUE
      type: queue

    incoming.from-aq:
      connector: helidon-aq
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
@Incoming("from-aq")
public void consumeAq(String msg) {
    System.out.println("Oracle AQ says: " + msg);
}
```

</div>

<div class="formalpara">

<div class="title">

Consuming one by one, manual ack:

</div>

``` java
@Incoming("from-aq")
@Acknowledgment(Acknowledgment.Strategy.MANUAL)
public CompletionStage<Void> consumeAq(AqMessage<String> msg) {
    // direct commit
    //msg.getDbConnection().commit();
    System.out.println("Oracle AQ says: " + msg.getPayload());
    // ack commits only in non-transacted mode
    return msg.ack();
}
```

</div>

## Producing

<div class="formalpara">

<div class="title">

Producing to AQ:

</div>

``` java
@Outgoing("to-aq")
public PublisherBuilder<String> produceToAq() {
    return ReactiveStreams.of("test1", "test2");
}
```

</div>
