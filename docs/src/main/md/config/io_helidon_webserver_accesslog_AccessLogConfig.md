Type:
[io.helidon.webserver.accesslog.AccessLogFeature](/apidocs/io.helidon.webserver.accesslog/io/helidon/webserver/accesslog/AccessLogFeature.html)

<div class="formalpara">

<div class="title">

Config key

</div>

``` text
access-log
```

</div>

This type provides the following service implementations:

- `io.helidon.webserver.spi.ServerFeatureProvider`

# Configuration options

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
<td style="text-align: left;"><p><code>enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether this feature will be
enabled.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>format</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The format for log entries (similar to
the Apache <code>LogFormat</code>).</p>
<table class="config">
<caption>Log format elements</caption>
<tbody>
<tr>
<td>%h</td>
<td>IP address of the remote host</td>
<td>HostLogEntry</td>
</tr>
<tr>
<td>%l</td>
<td>The client identity. This is always undefined in Helidon.</td>
<td>UserIdLogEntry</td>
</tr>
<tr>
<td>%u</td>
<td>User ID as asserted by Helidon Security.</td>
<td>UserLogEntry</td>
</tr>
<tr>
<td>%t</td>
<td>The timestamp</td>
<td>TimestampLogEntry</td>
</tr>
<tr>
<td>%r</td>
<td>The request line (`"GET /favicon.ico HTTP/1.0"`)</td>
<td>RequestLineLogEntry</td>
</tr>
<tr>
<td>%s</td>
<td>The status code returned to the client</td>
<td>StatusLogEntry</td>
</tr>
<tr>
<td>%b</td>
<td>The entity size in bytes</td>
<td>SizeLogEntry</td>
</tr>
<tr>
<td>%D</td>
<td>The time taken in microseconds (start of request until last byte
written)</td>
<td>TimeTakenLogEntry</td>
</tr>
<tr>
<td>%T</td>
<td>The time taken in seconds (start of request until last byte
written), integer</td>
<td>TimeTakenLogEntry</td>
</tr>
<tr>
<td>%{header-name}i</td>
<td>Value of header `header-name`</td>
<td>HeaderLogEntry</td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>logger-name</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td
style="text-align: left;"><p><code>io.helidon.webserver.AccessLog</code></p></td>
<td style="text-align: left;"><p>Name of the logger used to obtain
access log logger from System.getLogger(String). Defaults to
AccessLogFeature.DEFAULT_LOGGER_NAME.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sockets</code></p></td>
<td style="text-align: left;"><p>string[]</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>List of sockets to register this
feature on. If empty, it would get registered on all sockets. The logger
used will have the expected logger with a suffix of the socket
name.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>weight</code></p></td>
<td style="text-align: left;"><p>double</p></td>
<td style="text-align: left;"><p><code>1000.0</code></p></td>
<td style="text-align: left;"><p>Weight of the access log feature. We
need to log access for anything happening on the server, so weight is
high: io.helidon.webserver.accesslog.AccessLogFeature.WEIGHT.</p></td>
</tr>
</tbody>
</table>
