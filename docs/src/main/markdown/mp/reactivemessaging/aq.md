# Oracle AQ Connector

## Contents

- [Overview](#_overview)

- [Maven Coordinates](#maven-coordinates)

- [Configuration](#_configuration)

- [Usage](#_usage)

## Overview

Connecting streams to Oracle AQ with Reactive Messaging couldn’t be easier. This connector extends Helidon’s JMS connector with Oracle’s AQ-specific API.

## Maven Coordinates

To enable AQ Connector, add the following dependency to your project’s `pom.xml` (see [Managing Dependencies](../../about/managing-dependencies.md)).

``` xml
<dependency>
    <groupId>io.helidon.messaging.aq</groupId>
    <artifactId>helidon-messaging-aq</artifactId>
</dependency>
```

## Configuration

Connector name: `helidon-aq`

Type: [io.helidon.messaging.connectors.aq.AqConfigBuilder](/apidocs/io.helidon.messaging.connectors.aq/io/helidon/messaging/connectors/aq/AqConfigBuilder.html)

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
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>client-id</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Client identifier for JMS connection.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>data-source</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Mapping to javax.sql.DataSource DataSource supplied with {@link io.helidon.messaging.connectors.aq.AqConnector.AqConnectorBuilder#dataSource(String, javax.sql.DataSource) AqConnectorBuilder.dataSource()}.</p>
<ul>
<li><p>Type: string</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>destination</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Queue or topic name.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>durable</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>Indicates whether the consumer should be created as durable (only relevant for topic destinations).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>message-selector</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>JMS API message selector expression based on a subset of the SQL92. Expression can only access headers and properties, not the payload.</p>
<ul>
<li><p>Example: NewsType = ’Sports’ OR NewsType = ’Opinion’</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>named-factory</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Select jakarta.jms.ConnectionFactory ConnectionFactory in case factory is injected as a named bean or configured with name.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>non-local</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>When set to <code>true</code>, messages published by this connection, or any connection with the same client identifier, will not be delivered to this durable subscription.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>password</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Password used for creating JMS connection.</p></td>
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
<td style="text-align: left;"><p><code>subscriber-name</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Subscriber name used to identify a durable subscription.</p></td>
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
<td style="text-align: left;"><p>Specify if connection is io.helidon.messaging.connectors.jms.Type.QUEUE queue or io.helidon.messaging.connectors.jms.Type.TOPIC topic.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>username</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>User name used for creating JMS connection.</p></td>
</tr>
</tbody>
</table>

### Configured JMS Factory

The simplest possible usage is leaving construction of `AQjmsConnectionFactory` to the connector.

*Example of connector config:*

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

Its also possible and preferable to refer to [configured datasource](../persistence.md), in our example [Oracle UCP datasource](../persistence.md):

*Example of connector config with Oracle UCP datasource:*

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

### Injected JMS factory

If you need more advanced configurations, connector can work with injected `AQjmsConnectionFactory`:

*Inject:*

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

*Config:*

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

## Usage

### Consuming

*Consuming one by one unwrapped value:*

``` java
@Incoming("from-aq")
public void consumeAq(String msg) {
    System.out.println("Oracle AQ says: " + msg);
}
```

*Consuming one by one, manual ack:*

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

### Producing

*Producing to AQ:*

``` java
@Outgoing("to-aq")
public PublisherBuilder<String> produceToAq() {
    return ReactiveStreams.of("test1", "test2");
}
```
