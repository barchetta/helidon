# AqConfigBuilder (messaging.connectors.aq) Configuration

Type: [io.helidon.messaging.connectors.aq.AqConfigBuilder](/apidocs/io.helidon.messaging.connectors.aq/io/helidon/messaging/connectors/aq/AqConfigBuilder.html)

## Configuration options

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
