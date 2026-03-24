# HikariDataSourceConfig (data.sql.datasource.hikari) Configuration

Type: [io.helidon.data.sql.datasource.hikari.HikariDataSourceConfig](/apidocs/io.helidon.data.sql.datasource.hikari/io/helidon/data/sql/datasource/hikari/HikariDataSourceConfig.html)

*Config key*

``` text
hikari
```

This type provides the following service implementations:

- `io.helidon.data.sql.datasource.spi.DataSourceConfigProvider`

## Configuration options

| key | type | default value | description |
|----|----|----|----|
| `allow-pool-suspension` | boolean |   | Set whether pool suspension is allowed. See com.zaxxer.hikari.HikariConfig.setAllowPoolSuspension(boolean) for details. |
| `auto-commit` | boolean |   | Set the default auto-commit behavior of connections in the pool. See com.zaxxer.hikari.HikariConfig.setAutoCommit(boolean) for details. |
| `catalog` | string |   | Set the default catalog name to be set on connections. See com.zaxxer.hikari.HikariConfig.setCatalog(String) for details. |
| `connection-init-sql` | string |   | Set the SQL string that will be executed on all new connections when they are created, before they are added to the pool. See com.zaxxer.hikari.HikariConfig.setConnectionInitSql(String) for details. |
| `connection-test-query` | string |   | Set the SQL query to be executed to test the validity of connections. See com.zaxxer.hikari.HikariConfig.setConnectionTestQuery(String) for details. |
| `connection-timeout` | long |   | Set the maximum number of milliseconds that a client will wait for a connection from the pool. See com.zaxxer.hikari.HikariConfig.setConnectionTimeout(long) for details. |
| `health-check-properties` | Map\<string, string\> |   | Add properties (name/value pair) that will be used to configure the connection pool health check. See com.zaxxer.hikari.HikariConfig.addHealthCheckProperty(String, String) for details. |
| `idle-timeout` | long |   | This property controls the maximum amount of time that a connection is allowed to sit idle in the pool. See com.zaxxer.hikari.HikariConfig.setIdleTimeout(long) for details. |
| `initialization-fail-timeout` | long |   | Set the pool initialization failure timeout. See com.zaxxer.hikari.HikariConfig.setInitializationFailTimeout(long) for details. |
| `isolate-internal-queries` | boolean |   | Configure whether internal pool queries, principally aliveness checks, will be isolated in their own transaction via java.sql.Connection.rollback(). See com.zaxxer.hikari.HikariConfig.setIsolateInternalQueries(boolean) for details. |
| `keepalive-time` | long |   | This property controls the keepalive interval for a connection in the pool. See com.zaxxer.hikari.HikariConfig.setKeepaliveTime(long) for details. |
| `leak-detection-threshold` | long |   | This property controls the amount of time that a connection can be out of the pool before a message is logged indicating a possible connection leak. See com.zaxxer.hikari.HikariConfig.setLeakDetectionThreshold(long) for details. |
| `max-lifetime` | long |   | This property controls the maximum lifetime of a connection in the pool. See com.zaxxer.hikari.HikariConfig.setMaxLifetime(long) for details. |
| `maximum-pool-size` | int |   | The property controls the maximum size that the pool is allowed to reach, including both idle and in-use connections. See com.zaxxer.hikari.HikariConfig.setMaximumPoolSize(int) for details. |
| `minimum-idle` | int |   | The property controls the minimum number of idle connections that HikariCP tries to maintain in the pool, including both idle and in-use connections. See com.zaxxer.hikari.HikariConfig.setMinimumIdle(int) for details. |
| `pool-name` | string |   | Set the name of the connection pool. See com.zaxxer.hikari.HikariConfig.setPoolName(String) for details. |
| `properties` | Map\<string, string\> |   | Add properties (name/value pair) that will be used to configure the DataSource/Driver. Property values are limited to String values. See com.zaxxer.hikari.HikariConfig.addDataSourceProperty(String, Object) for details. |
| `read-only` | boolean |   | Configures the Connections to be added to the pool as read-only Connections. See com.zaxxer.hikari.HikariConfig.setReadOnly(boolean) for details. |
| `register-mbeans` | boolean |   | Configures whether HikariCP self-registers the com.zaxxer.hikari.HikariConfigMXBean and com.zaxxer.hikari.HikariPoolMXBean in JMX. See com.zaxxer.hikari.HikariConfig.setRegisterMbeans(boolean) for details. |
| `schema` | string |   | Set the default schema name to be set on connections. See com.zaxxer.hikari.HikariConfig.setSchema(String) for details. |
| `transaction-isolation` | TransactionIsolation (TRANSACTION_READ_UNCOMMITTED, TRANSACTION_READ_COMMITTED, TRANSACTION_REPEATABLE_READ, TRANSACTION_SERIALIZABLE) |   | Set the default transaction isolation level. See com.zaxxer.hikari.HikariConfig.setTransactionIsolation(String) for details. |
| `validation-timeout` | long |   | Sets the maximum number of milliseconds that the pool will wait for a connection to be validated as alive. See com.zaxxer.hikari.HikariConfig.setValidationTimeout(long) for details. |

Optional configuration options
