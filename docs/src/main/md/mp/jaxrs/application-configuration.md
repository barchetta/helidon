Your application can use the MicroProfile Config or Helidon Config (or
both). MicroProfile Config offers portability to other MicroProfile
servers. Helidon Config supports a full tree structure, including
repeating elements.

# Configuring the Application

You can inject values that the application can access from both
MicroProfile Config and from Helidon Config.

<div class="formalpara">

<div class="title">

Jakarta REST - inject a single config property

</div>

``` java
@Inject
public MyResource(@ConfigProperty(name = "app.name") String appName) {
    this.applicationName = appName;
}
```

</div>

You can also inject the whole configuration instance, either
`io.helidon.config.Config` or `org.eclipse.microprofile.config.Config`.

<div class="formalpara">

<div class="title">

Jakarta REST - inject config

</div>

``` java
@Inject
public MyResource(Config config) {
    this.config = config;
}
```

</div>
