Type:
[io.helidon.data.sql.datasource.jdbc.JdbcDataSourceConfig](/apidocs/io.helidon.data.sql.datasource.jdbc/io/helidon/data/sql/datasource/jdbc/JdbcDataSourceConfig.html)

<div class="formalpara">

<div class="title">

Config key

</div>

``` text
jdbc
```

</div>

This type provides the following service implementations:

- `io.helidon.data.sql.datasource.spi.DataSourceConfigProvider`

# Configuration options

| key | type | default value | description |
|----|----|----|----|
| `auto-commit` | boolean |   | Set the default auto-commit behavior of create connections. |
| `catalog` | string |   | Set the default catalog name to be set on connections. |
| `properties` | Map\<string, string\> |   | Add properties (name/value pair) that will be used to configure the DataSource/Driver. Property values are limited to String values. |
| `read-only` | boolean |   | Whether the connection should be read only. |
| `schema` | string |   | Set the default schema name to be set on connections. |
| `transaction-isolation` | TransactionIsolation (TRANSACTION_READ_UNCOMMITTED, TRANSACTION_READ_COMMITTED, TRANSACTION_REPEATABLE_READ, TRANSACTION_SERIALIZABLE) |   | Set the default transaction isolation level. |

Optional configuration options
