Type:
[io.helidon.data.sql.datasource.ucp.UcpDataSourceConfig](/apidocs/io.helidon.data.sql.datasource.ucp/io/helidon/data/sql/datasource/ucp/UcpDataSourceConfig.html)

<div class="formalpara">

<div class="title">

Config key

</div>

``` text
ucp
```

</div>

This type provides the following service implementations:

- `io.helidon.data.sql.datasource.spi.DataSourceConfigProvider`

# Configuration options

| key | type | default value | description |
|----|----|----|----|
| `abandoned-connection-timeout` | int |   | Sets the abandoned connection timeout. See oracle.ucp.jdbc.PoolDataSource.setAbandonedConnectionTimeout(int) for details. |
| `commit-on-connection-return` | boolean |   | Sets the `boolean` value for the property that controls the behavior of UCP when a connection is released back to the pool with pending uncommitted changes in an active transaction. See oracle.ucp.jdbc.PoolDataSource.setCommitOnConnectionReturn(boolean) for details. |
| `connection-factory-class-name` | string |   | Sets the connection factory class name. See oracle.ucp.jdbc.PoolDataSource.setConnectionFactoryClassName(String) for details. |
| `connection-factory-properties` | Map |   | Sets the connection factory properties on the connection factory. See oracle.ucp.jdbc.PoolDataSource.setConnectionFactoryProperties(java.util.Properties) for details. |
| `connection-harvest-max-count` | int |   | Sets the maximum number of connections that may be harvested when the connection harvesting occurs. See oracle.ucp.jdbc.PoolDataSource.setConnectionHarvestMaxCount(int) for details. |
| `connection-harvest-trigger-count` | int |   | Sets the number of available connections below which the connection pool’s connection harvesting will occur. See oracle.ucp.jdbc.PoolDataSource.setConnectionHarvestTriggerCount(int) for details. |
| `connection-labeling-high-cost` | int |   | Sets the cost value which identifies a connection as "high-cost" for connection labeling. See oracle.ucp.jdbc.PoolDataSource.setConnectionLabelingHighCost(int) for details. |
| `connection-pool-name` | string |   | Sets the connection pool name. See oracle.ucp.jdbc.PoolDataSource.setConnectionPoolName(String) for details. |
| `connection-properties` | Map |   | Sets the connection properties on the connection factory. See oracle.ucp.jdbc.PoolDataSource.setConnectionProperties(java.util.Properties) for details. |
| `connection-repurpose-threshold` | int |   | Sets the connection repurpose threshold for the pool. See oracle.ucp.jdbc.PoolDataSource.setConnectionRepurposeThreshold(int) for details. |
| `connection-validation-timeout` | int |   | Sets the connection validation timeout in seconds. See oracle.ucp.jdbc.PoolDataSource.setConnectionValidationTimeout(int) for details. |
| `connection-wait-duration` | Duration |   | Configures how much time a connection request call may wait before it either successfully returns a connection or throws an exception. See oracle.ucp.jdbc.PoolDataSource.setConnectionWaitDuration(java.time.Duration) for details. |
| `create-connection-in-borrow-thread` | boolean |   | Set this flag to `true` to make UCP use the borrowing thread to create new connections. See oracle.ucp.jdbc.PoolDataSource.setCreateConnectionInBorrowThread(boolean) for details. |
| `data-source-name` | string |   | Sets the data source name. See oracle.ucp.jdbc.PoolDataSource.setDataSourceName(String) for details. |
| `database-name` | string |   | Sets the database name. See oracle.ucp.jdbc.PoolDataSource.setDatabaseName(String) for details. |
| `description` | string |   | Sets the data source description. See oracle.ucp.jdbc.PoolDataSource.setDescription(String) for details. |
| `fast-connection-failover-enabled` | boolean |   | Enables Fast Connection Failover (FCF) for the connection pool accessed using this pool-enabled data source. See oracle.ucp.jdbc.PoolDataSource.setFastConnectionFailoverEnabled(boolean) for details. |
| `high-cost-connection-reuse-threshold` | int |   | Sets the high-cost connection reuse threshold for connection labeling. See oracle.ucp.jdbc.PoolDataSource.setHighCostConnectionReuseThreshold(int) for details. |
| `inactive-connection-timeout` | int |   | Sets the inactive connection timeout. See oracle.ucp.jdbc.PoolDataSource.setInactiveConnectionTimeout(int) for details. |
| `initial-pool-size` | int |   | Sets the initial pool size. See oracle.ucp.jdbc.PoolDataSource.setInitialPoolSize(int) for details. |
| `max-connection-reuse-count` | int |   | Sets the maximum connection reuse count. See oracle.ucp.jdbc.PoolDataSource.setMaxConnectionReuseCount(int) for details. |
| `max-connection-reuse-time` | long |   | Sets the maximum connection reuse time in seconds. See oracle.ucp.jdbc.PoolDataSource.setMaxConnectionReuseTime(long) for details. |
| `max-connections-per-shard` | int |   | Sets the max number of connections that can be created per shard from this connection pool. See oracle.ucp.jdbc.PoolDataSource.setMaxConnectionsPerShard(int) for details. |
| `max-idle-time` | int |   | Sets the maximum idle time for available connections in the pool in seconds. See oracle.ucp.jdbc.PoolDataSource.setMaxIdleTime(int) for details. |
| `max-pool-size` | int |   | Sets the maximum number of connections. See oracle.ucp.jdbc.PoolDataSource.setMaxPoolSize(int) for details. |
| `max-statements` | int |   | Sets the maximum number of statements that may be pooled or cached on a connection. See oracle.ucp.jdbc.PoolDataSource.setMaxStatements(int) for details. |
| `min-idle` | int |   | Sets the minimum number of idle connections. See oracle.ucp.jdbc.PoolDataSource.setMinIdle(int) for details. |
| `min-pool-size` | int |   | Sets the minimum number of connections. See oracle.ucp.jdbc.PoolDataSource.setMinPoolSize(int) for details. |
| `network-protocol` | string |   | Sets the data source network protocol. See oracle.ucp.jdbc.PoolDataSource.setNetworkProtocol(String) for details. |
| `ons-configuration` | string |   | Sets the configuration string used for remote ONS subscription. See oracle.ucp.jdbc.PoolDataSource.setONSConfiguration(String) for details. |
| `port-number` | int |   | Sets the database port number. See oracle.ucp.jdbc.PoolDataSource.setPortNumber(int) for details. |
| `property-cycle` | int |   | Sets the property cycle in seconds. See oracle.ucp.jdbc.PoolDataSource.setPropertyCycle(int) for details. |
| `query-timeout` | int |   | Sets the number of seconds the driver will wait for a Statement object to execute to the given number of seconds. See oracle.ucp.jdbc.PoolDataSource.setQueryTimeout(int) for details. |
| `read-only-instance-allowed` | boolean |   | Sets the read-only instance allowed value on the datasource. See oracle.ucp.jdbc.PoolDataSource.setReadOnlyInstanceAllowed(boolean) for details. |
| `role-name` | string |   | Sets the data source role name. See oracle.ucp.jdbc.PoolDataSource.setRoleName(String) for details. |
| `seconds-to-trust-idle-connection` | int |   | Sets the time to trust an idle connection to skip a validation test in seconds. See oracle.ucp.jdbc.PoolDataSource.setSecondsToTrustIdleConnection(int) for details. |
| `server-name` | string |   | Sets the database server name. See oracle.ucp.jdbc.PoolDataSource.setServerName(String) for details. |
| `sharding-mode` | boolean |   | Change the mode of UCP when UCP is using a Sharded Database. See oracle.ucp.jdbc.PoolDataSource.setShardingMode(boolean) for details. |
| `sql-for-validate-connection` | string |   | Sets the SQL statement to validate the database connection. See oracle.ucp.jdbc.PoolDataSource.setSQLForValidateConnection(String) for details. |
| `time-to-live-connection-timeout` | int |   | Sets the maximum time a connection may remain in-use in seconds. See oracle.ucp.jdbc.PoolDataSource.setTimeToLiveConnectionTimeout(int) for details. |
| `timeout-check-interval` | int |   | Sets the timeout check interval in seconds. See oracle.ucp.jdbc.PoolDataSource.setTimeoutCheckInterval(int) for details. |
| `validate-connection-on-borrow` | boolean |   | Makes the pool validate the connection before returning it to the user by calling the JDBC API `isValid`. See oracle.ucp.jdbc.PoolDataSource.setValidateConnectionOnBorrow(boolean) for details. |
| `xa-data-source` | boolean |   | Support for distributed transactions. oracle.ucp.jdbc.PoolXADataSource instance is returned when `true`, oracle.ucp.jdbc.PoolDataSource instance is returned when `false`. Default value is `false`. |

Optional configuration options
