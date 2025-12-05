# Overview

Neo4j is a graph database management system developed by Neo4j, Inc. It
is an ACID-compliant transactional database with native graph storage
and processing. Neo4j is available in a GPL3-licensed open-source
“community edition”.

# Maven Coordinates

To enable Neo4j, add the following dependency to your project’s
`pom.xml` (see [Managing
Dependencies](../../about/managing-dependencies.md)).

``` xml
<dependency>
   <groupId>io.helidon.integrations.neo4j</groupId>
   <artifactId>helidon-integrations-neo4j</artifactId>
</dependency>
```

> [!NOTE]
> Check [Neo4j Metrics propagation](#_neo4j_metrics_propagation) and
> [Neo4j Health Checks](#_neo4j_health_checks) for additional
> dependencies for *Neo4j* `Metrics` and `Health Checks` integration.

# Usage

The support for Neo4j is implemented in Neo4j driver level. Just add the
dependency, add configuration in `microprofile-config.properties` file
and Neo4j driver will be configured by Helidon and can be injected using
CDI.

First describe Neo4j connection properties:

``` properties
# Neo4j settings
neo4j.uri=bolt://localhost:7687
neo4j.authentication.username=neo4j
neo4j.authentication.password=secret
neo4j.pool.metricsEnabled=true
```

Then just inject the driver:

``` java
@Inject
public MovieRepository(Driver driver) {
    this.driver = driver;
}
```

The driver can be used according to the [Neo4j
documentation](https://neo4j.com/developer/java/).

# Configuration

Type:
[io.helidon.integrations.neo4j.Neo4j](/apidocs/io.helidon.integrations.neo4j/io/helidon/integrations/neo4j/Neo4j.html)

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
<td
style="text-align: left;"><p><code>authentication-enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Enable authentication.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>certificate</code></p></td>
<td style="text-align: left;"><p>Path</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Set certificate path.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>connection-acquisition-timeout</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p><code>PT1M</code></p></td>
<td style="text-align: left;"><p>Set connection acquisition
timeout.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>encrypted</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Enable encrypted field.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>hostname-verification-enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Enable hostname verification.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>idle-time-before-connection-test</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p><code>PT1MS</code></p></td>
<td style="text-align: left;"><p>Set idle time.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>log-leaked-sessions</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Enable log leaked sessions.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>max-connection-lifetime</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p><code>PT5H</code></p></td>
<td style="text-align: left;"><p>Set max life time.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>max-connection-pool-size</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>100</code></p></td>
<td style="text-align: left;"><p>Set pool size.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>metrics-enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Enable metrics.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>password</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Create password.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>trust-strategy</code></p></td>
<td style="text-align: left;"><p>TrustStrategy (TRUST_ALL_CERTIFICATES,
TRUST_CUSTOM_CA_SIGNED_CERTIFICATES,
TRUST_SYSTEM_CA_SIGNED_CERTIFICATES)</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Set trust strategy.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>TRUST_ALL_CERTIFICATES</code>: Trust all.</p></li>
<li><p><code>TRUST_CUSTOM_CA_SIGNED_CERTIFICATES</code>: Trust custom
certificates.</p></li>
<li><p><code>TRUST_SYSTEM_CA_SIGNED_CERTIFICATES</code>: Trust system
CA.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>uri</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Create uri.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>username</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Create username.</p></td>
</tr>
</tbody>
</table>

# Examples

This example implements a simple Neo4j REST service using MicroProfile.
For this example a working Neo4j database is required. The Neo4j Movie
database is used for this example.

Bring up a Neo4j instance via Docker

``` bash
docker run --publish=7474:7474 --publish=7687:7687 -e 'NEO4J_AUTH=neo4j/secret'  neo4j:latest
```

Go to the Neo4j browser and play the first step of the movies graph:
[`:play movies`](http://localhost:7474/browser/?cmd=play&arg=movies)

Now go to the `pom.xml` and add the following dependencies:

``` xml
<dependencies>
    <dependency>
        <groupId>io.helidon.integrations.neo4j</groupId>
        <artifactId>helidon-integrations-neo4j</artifactId>
    </dependency>
    <dependency>
        <groupId>io.helidon.integrations.neo4j</groupId>
        <artifactId>helidon-integrations-neo4j-metrics</artifactId>
    </dependency>
    <dependency>
        <groupId>io.helidon.integrations.neo4j</groupId>
        <artifactId>helidon-integrations-neo4j-health</artifactId>
    </dependency>
</dependencies>
```

Next add the connection configuration properties for Neo4j:

``` properties
# Neo4j settings
neo4j.uri=bolt://localhost:7687
neo4j.authentication.username=neo4j
neo4j.authentication.password=secret
neo4j.pool.metricsEnabled=true

# Enable the optional MicroProfile Metrics REST.request metrics
metrics.rest-request.enabled=true
```

This includes both connection information and enables Neo4j metrics
propagation.

Finally, we are able to inject and use the `Neo4j` driver.

``` java
@ApplicationScoped
public class MovieRepository {

    private final Driver driver;

    @Inject
    public MovieRepository(Driver driver) { 
        this.driver = driver;
    }

    List<Movie> findAll() { 
        try (var session = driver.session()) {
            var query = """
                        match (m:Movie)
                        match (m) <- [:DIRECTED] - (d:Person)
                        match (m) <- [r:ACTED_IN] - (a:Person)
                        return m, collect(d) as directors, collect({name:a.name, roles: r.roles}) as actors
                        """;

            return session.executeRead(tx -> tx.run(query).list(r -> {
                var movieNode = r.get("m").asNode();

                var directors = r.get("directors").asList(v -> {
                    var personNode = v.asNode();
                    return new Person(personNode.get("born").asInt(), personNode.get("name").asString());
                });

                var actors = r.get("actors").asList(v -> {
                    return new Actor(v.get("name").asString(), v.get("roles").asList(
                            Value::asString));
                });

                return new Movie(
                        movieNode.get("title").asString(),
                        movieNode.get("tagline").asString(),
                        movieNode.get("released").asInt(),
                        directors,
                        actors);
            }));
        }
    }
}
```

- `Neo4j` driver constructor injection

- Use of `Neo4j` driver to extract all Movies

Movies can now be returned as JSON objects:

``` java
@GET
@Produces(MediaType.APPLICATION_JSON)
public List<Movie> getAllMovies() {
    return movieRepository.findAll();
}
```

Now build and run.

``` bash
mvn package
java -jar target/helidon-examples-integration-neo4j-mp.jar
```

Exercise the application:

``` bash
curl -X GET http://localhost:8080/movies

# Try health
curl -s -X GET http://localhost:8080/health

# Try metrics in Prometheus Format
curl -s -X GET http://localhost:8080/metrics

# Try metrics in JSON Format
curl -H 'Accept: application/json' -X GET http://localhost:8080/metrics
```

Full example code is available in [Helidon GitHub
Repository](https://github.com/oracle/helidon/tree/master/examples/integrations/neo4j/neo4j-mp).

# Additional Information

## Neo4j Metrics propagation

Neo4j’s metrics can be propagated to the user as `MicroProfile` metrics.
This is implemented in a separate Maven module. Just add

``` xml
<dependency>
   <groupId>io.helidon.integrations.neo4j</groupId>
   <artifactId>helidon-integrations-neo4j-metrics</artifactId>
</dependency>
```

> [!NOTE]
> Works with *Neo4j Integration* main dependency described in [Maven
> Coordinates](#maven-coordinates).

To enable metrics in Neo4j, add the following property to
`microprofile-config.properties`:

``` properties
neo4j.pool.metricsEnabled=true
```

By applying these two actions, Neo4j metrics will be automatically added
to the output of the `/metrics` endpoint.

## Neo4j Health Checks

If your application is highly dependent on Neo4j database, health and
liveness checks are essential for this application to work correctly.

`MicroProfile` Health checks for Neo4j are implemented in a separate
Maven module:

``` xml
<dependency>
   <groupId>io.helidon.integrations.neo4j</groupId>
   <artifactId>helidon-integrations-neo4j-health</artifactId>
</dependency>
```

> [!NOTE]
> Works with *Neo4j Integration* main dependency described in [Maven
> Coordinates](#maven-coordinates).

Health checks for Neo4j will be included in `/health` endpoint output.

# References

- [Neo4j official website](https://neo4j.com/)

- [Neo4j Java developer guide](https://neo4j.com/developer/java/)
