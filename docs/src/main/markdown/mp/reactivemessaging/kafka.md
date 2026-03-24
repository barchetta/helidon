# Kafka Connector

## Contents

- [Overview](#_overview)

- [Maven Coordinates](#maven-coordinates)

- [Config](#_config)

- [Consuming Messages](#_consuming_messages)

- [Producing Messages](#_producing_messages)

- [NACK Strategy](#_nack_strategy)

- [Examples](#_examples)

## Overview

Connecting streams to Kafka with Reactive Messaging is easy to do. There is a standard Kafka client behind the scenes, all the [producer](https://kafka.apache.org/28/documentation.html#producerconfigs) and [consumer](https://kafka.apache.org/28/documentation.html#consumerconfigs) configs can be propagated through messaging config.

## Maven Coordinates

To enable Reactive Kafka Connector, add the following dependency to your project’s `pom.xml` (see [Managing Dependencies](../../about/managing-dependencies.md)).

``` xml
<dependency>
    <groupId>io.helidon.messaging.kafka</groupId>
    <artifactId>helidon-messaging-kafka</artifactId>
</dependency>
```

## Config

*Example of connector config:*

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

- Kafka client consumer’s property auto.offset.reset configuration for `from-kafka` channel only

- Kafka client’s property [bootstrap.servers](https://kafka.apache.org/28/documentation.html#consumerconfigs_bootstrap.servers) configuration for all channels using the connector

> [!TIP]
> Besides the following configuration options, any property from [consumer](https://kafka.apache.org/documentation/#consumerconfigs) or [producer](https://kafka.apache.org/documentation/#producerconfigs) configuration can be passed to the underlying Kafka client.

Type: [io.helidon.messaging.connectors.kafka.KafkaConfigBuilder](/apidocs/io.helidon.messaging.connectors.kafka/io/helidon/messaging/connectors/kafka/KafkaConfigBuilder.html)

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
<td style="text-align: left;"><p><code>acks</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The number of acknowledgments the producer requires the leader to have received before considering a request complete. This controls the durability of records that are sent.</p>
<p>The following settings are allowed:</p>
<ul>
<li><p><strong>acks=0</strong> If set to zero then the producer will not wait for any acknowledgment from the server at all. The record will be immediately added to the socket buffer and considered sent. No guarantee can be made that the server has received the record in this case, and the retries configuration will not take effect (as the client won’t generally know of any failures). The offset given back for each record will always be set to -1.</p></li>
<li><p><strong>acks=1</strong> This will mean the leader will write the record to its local log but will respond without awaiting full acknowledgement from all followers. In this case should the leader fail immediately after acknowledging the record but before the followers have replicated it then the record will be lost.</p></li>
<li><p><strong>acks=all</strong> This means the leader will wait for the full set of in-sync replicas to acknowledge the record. This guarantees that the record will not be lost as long as at least one in-sync replica remains alive. This is the strongest available guarantee. This is equivalent to the acks=-1 setting.</p></li>
<li><p>Type: string</p></li>
<li><p>Default: 1</p></li>
<li><p>Valid Values: [all, -1, 0, 1]</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>auto-offset-reset</code></p></td>
<td style="text-align: left;"><p>KafkaConfigBuilder.AutoOffsetReset (LATEST, EARLIEST, NONE)</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>What to do when there is no initial offset in Kafka or if the current offset does not exist any more on the server (e.g. because that data has been deleted):</p>
<ul>
<li><p>earliest: automatically reset the offset to the earliest offset</p></li>
<li><p>latest: automatically reset the offset to the latest offset</p></li>
<li><p>none: throw exception to the consumer if no previous offset is found for the consumer’s group</p></li>
<li><p>Type: string</p></li>
<li><p>Default: latest</p></li>
<li><p>Valid Values: [latest, earliest, none]</p></li>
</ul>
<p>Allowed values:</p>
<ul>
<li><p><code>LATEST</code>: Automatically reset the offset to the earliest offset.</p></li>
<li><p><code>EARLIEST</code>: Automatically reset the offset to the latest offset.</p></li>
<li><p><code>NONE</code>: Throw exception to the consumer if no previous offset is found for the consumer’s group.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>batch-size</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The producer will attempt to batch records together into fewer requests whenever multiple records are being sent to the same partition. This helps performance on both the client and the server. This configuration controls the default batch size in bytes. No attempt will be made to batch records larger than this size. Requests sent to brokers will contain multiple batches, one for each partition with data available to be sent. A small batch size will make batching less common and may reduce throughput (a batch size of zero will disable batching entirely). A very large batch size may use memory a bit more wastefully as we will always allocate a buffer of the specified batch size in anticipation of additional records.</p>
<ul>
<li><p>Type: int</p></li>
<li><p>Default: 16384</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>bootstrap-servers</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>A list of host/port pairs to use for establishing the initial connection to the Kafka cluster. The client will make use of all servers irrespective of which servers are specified here for bootstrapping—this list only impacts the initial hosts used to discover the full set of servers. This list should be in the form <code>host1:port1,host2:port2,…​.</code> Since these servers are just used for the initial connection to discover the full cluster membership (which may change dynamically), this list need not contain the full set of servers (you may want more than one, though, in case a server is down).</p>
<ul>
<li><p>Type: list</p></li>
<li><p>Default: ""</p></li>
<li><p>Valid Values: non-null string</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>buffer-memory</code></p></td>
<td style="text-align: left;"><p>long</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The total bytes of memory the producer can use to buffer records waiting to be sent to the server. If records are sent faster than they can be delivered to the server the producer will block for <code>max.block.ms</code> after which it will throw an exception. This setting should correspond roughly to the total memory the producer will use, but is not a hard bound since not all memory the producer uses is used for buffering. Some additional memory will be used for compression (if compression is enabled) as well as for maintaining in-flight requests.</p>
<ul>
<li><p>Type: long</p></li>
<li><p>Default: 33554432</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>compression-type</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The compression type for all data generated by the producer. The default is none (i.e. no compression). Valid values are none, gzip, snappy, lz4, or zstd. Compression is of full batches of data, so the efficacy of batching will also impact the compression ratio (more batching means better compression).</p>
<ul>
<li><p>Type: string</p></li>
<li><p>Default: none</p></li>
<li><p>Valid Values: [none, gzip, snappy, lz4, zstd]</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>dlq-topic</code></p></td>
<td style="text-align: left;"><p>String[]</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Names of the "dead letter queue" topics to be used in case message is nacked.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>enable-auto-commit</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>If true the consumer’s offset will be periodically committed in the background.</p>
<ul>
<li><p>Type: boolean</p></li>
<li><p>Default: true</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>group-id</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>A unique string that identifies the consumer group this consumer belongs to. This property is required.</p>
<ul>
<li><p>Type: string</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>key-deserializer</code></p></td>
<td style="text-align: left;"><p>Class</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Deserializer class for key that implements the org.apache.kafka.common.serialization.Deserializer interface.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>key-serializer</code></p></td>
<td style="text-align: left;"><p>Class</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Serializer class for key that implements the org.apache.kafka.common.serialization.Serializer interface.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>period-executions</code></p></td>
<td style="text-align: left;"><p>long</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Period between successive executions of polling loop.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>poll-timeout</code></p></td>
<td style="text-align: left;"><p>long</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The maximum time to block polling loop in milliseconds.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>retries</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Setting a value greater than zero will cause the client to resend any record whose send fails with a potentially transient error. Note that this retry is no different than if the client resent the record upon receiving the error. Allowing retries without setting <code>max.in.flight.requests.per.connection</code> to 1 will potentially change the ordering of records because if two batches are sent to a single partition, and the first fails and is retried but the second succeeds, then the records in the second batch may appear first. Note additionally that produce requests will be failed before the number of retries has been exhausted if the timeout configured by delivery.timeout.ms expires first before successful acknowledgement. Users should generally prefer to leave this config unset and instead use delivery.timeout.ms to control retry behavior.</p>
<ul>
<li><p>Type: int</p></li>
<li><p>Default: 2147483647</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>topic</code></p></td>
<td style="text-align: left;"><p>String[]</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Names of the topics to consume from.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>topic-pattern</code></p></td>
<td style="text-align: left;"><p>Pattern</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Pattern for topic names to consume from.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>value-deserializer</code></p></td>
<td style="text-align: left;"><p>Class</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Deserializer class for value that implements the org.apache.kafka.common.serialization.Deserializer interface.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>value-serializer</code></p></td>
<td style="text-align: left;"><p>Class</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Serializer class for value that implements the org.apache.kafka.common.serialization.Serializer interface.</p></td>
</tr>
</tbody>
</table>

## Consuming Messages

*Example of consuming from Kafka:*

``` java
@Incoming("from-kafka")
public void consumeKafka(String msg) {
    System.out.println("Kafka says: " + msg);
}
```

## Producing Messages

*Example of producing to Kafka:*

``` java
@Outgoing("to-kafka")
public PublisherBuilder<String> produceToKafka() {
    return ReactiveStreams.of("test1", "test2");
}
```

## NACK Strategy

|  |  |
|----|----|
| Strategy | Description |
| Kill channel | Nacked message sends error signal and causes channel failure so Messaging Health check can report it as DOWN |
| DLQ | Nacked messages are sent to specified dead-letter-queue |
| Log only | Nacked message is logged and channel continues normally |

### Kill channel

Default NACK strategy for Kafka connector. When

### Dead Letter Queue

Sends nacked messages to error topic, [DLQ](https://en.wikipedia.org/wiki/Dead_letter_queue) is well known pattern for dealing with unprocessed messages.

Helidon can derive connection settings for DLQ topic automatically if the error topic is present on the same Kafka cluster. Serializers are derived from deserializers used for consumption `org.apache.kafka.common.serialization.StringDeserializer` \> `org.apache.kafka.common.serialization.StringSerializer`. Note that the name of the error topic is needed only in this case.

*Example of derived DLQ config:*

``` yaml
mp.messaging:
  incoming:
    my-channel:
      nack-dlq: dql_topic_name
```

If a custom connection is needed, then use the 'nack-dlq' key for all of the producer configuration.

*Example of custom DLQ config:*

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

### Log only

Only logs nacked messages and throws them away, offset is committed and channel continues normally consuming subsequent messages.

*Example of log only enabled nack strategy*

``` yaml
mp.messaging:
  incoming:
    my-channel:
      nack-log-only: true
```

## Examples

Don’t forget to check out the examples with pre-configured Kafka docker image, for easy testing:

- <https://github.com/helidon-io/helidon-examples/tree/helidon-4.x/examples/messaging>
