# JdbcParametersConfig (dbclient.jdbc) Configuration

Type: [io.helidon.dbclient.jdbc.JdbcParametersConfig](/apidocs/io.helidon.dbclient.jdbc/io/helidon/dbclient/jdbc/JdbcParametersConfig.html)

*Config key*

``` text
parameters
```

## Configuration options

| key | type | default value | description |
|----|----|----|----|
| `set-object-for-java-time` | boolean | `true` | Set all `java.time` Date/Time values directly using java.sql.PreparedStatement.setObject(int, Object). This option shall work fine for recent JDBC drivers. Default value is `true`. |
| `string-binding-size` | int | `1024` | String values with length above this limit will be bound using java.sql.PreparedStatement.setCharacterStream(int, java.io.Reader, int) if useStringBinding() is set to `true`. Default value is `1024`. |
| `timestamp-for-local-time` | boolean | `true` | Use java.sql.PreparedStatement.setTimestamp(int, java.sql.Timestamp) to set java.time.LocalTime values when `true` or use java.sql.PreparedStatement.setTime(int, java.sql.Time) when `false`. Default value is `true`. This option is vendor specific. Most of the databases are fine with java.sql.Timestamp, but for example SQL Server requires java.sql.Time. This option does not apply when setObjectForJavaTime() is set to `true`. |
| `use-byte-array-binding` | boolean | `true` | Use java.sql.PreparedStatement.setBinaryStream(int, java.io.InputStream, int) binding for `byte[]` values. Default value is `true`. |
| `use-n-string` | boolean | `false` | Use SQL `NCHAR`, `NVARCHAR` or `LONGNVARCHAR` value conversion for String values. Default value is `false`. |
| `use-string-binding` | boolean | `true` | Use java.sql.PreparedStatement.setCharacterStream(int, java.io.Reader, int) binding for String values with length above stringBindingSize() limit. Default value is `true`. |

Optional configuration options
