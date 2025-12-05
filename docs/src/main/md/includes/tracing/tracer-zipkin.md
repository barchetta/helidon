Helidon is integrated with the Zipkin tracer.

The Zipkin builder is loaded through `ServiceLoader` and configured. You
could also use the Zipkin builder directly, though this would create a
source-code dependency on the Zipkin tracer.

# Maven Coordinates

To enable Zipkin Tracing, add the following dependency to your project’s
`pom.xml` (see [Managing
Dependencies](../../about/managing-dependencies.md)).

``` xml
<dependency>
    <groupId>io.helidon.tracing.providers</groupId>
    <artifactId>helidon-tracing-providers-zipkin</artifactId>
</dependency>
```

# Configuring Zipkin

Zipkin tracer configuration

Type: io.opentracing.Tracer

This is a standalone configuration type, prefix from configuration root:
`tracing`

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
<td style="text-align: left;"><p><code>api-version</code></p></td>
<td style="text-align: left;"><p>Version (V1, V2)</p></td>
<td style="text-align: left;"><p><code>V2</code></p></td>
<td style="text-align: left;"><p>Version of Zipkin API to use. Defaults
to Version.V2.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>V1</code>: Version 1.</p></li>
<li><p><code>V2</code>: Version 2.</p></li>
</ul></td>
</tr>
</tbody>
</table>

The following is an example of a Zipkin configuration, specified in the
YAML format.

``` yaml
tracing:
  zipkin:
    service: "helidon-service"
    protocol: "https"
    host: "zipkin"
    port: 9987
    api-version: 1
    # this is the default path for API version 2
    path: "/api/v2/spans"
    tags:
      tag1: "tag1-value"
      tag2: "tag2-value"
    boolean-tags:
      tag3: true
      tag4: false
    int-tags:
      tag5: 145
      tag6: 741
```

Example of Zipkin trace:

<figure>
<img
src="/Users/jdipol/GitHub/barchetta/helidon/docs/src/main/asciidoc/images/webserver/zipkin.png"
alt="Zipkin example" />
</figure>
