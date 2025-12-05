Type:
[io.helidon.data.sql.datasource.DataSourceConfig](/apidocs/io.helidon.data.sql.datasource/io/helidon/data/sql/datasource/DataSourceConfig.html)

This is a standalone configuration type, prefix from configuration root:
`data.sources.sql`

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
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>@default</code></p></td>
<td style="text-align: left;"><p>javax.sql.DataSource name. Optional
name to distinguish several data sources of the same type. First
available data source is returned when name is not set.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>provider</code></p></td>
<td
style="text-align: left;"><p>io.helidon.data.sql.datasource.ProviderConfig
(service provider interface)</p>
<p>Such as:</p>
<ul>
<li><p><a
href="../config/io_helidon_data_sql_datasource_hikari_HikariDataSourceConfig.xml">hikari
(HikariDataSourceConfig)</a></p></li>
<li><p><a
href="../config/io_helidon_data_sql_datasource_jdbc_JdbcDataSourceConfig.xml">jdbc
(JdbcDataSourceConfig)</a></p></li>
<li><p><a
href="../config/io_helidon_data_sql_datasource_ucp_UcpDataSourceConfig.xml">ucp
(UcpDataSourceConfig)</a></p></li>
</ul></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Configuration of the used provider,
such as UCP.</p></td>
</tr>
</tbody>
</table>
