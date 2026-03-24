# JmsConfigBuilder (messaging.connectors.jms) Configuration

Type: [io.helidon.messaging.connectors.jms.JmsConfigBuilder](/apidocs/io.helidon.messaging.connectors.jms/io/helidon/messaging/connectors/jms/JmsConfigBuilder.html)

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
