# Overview

Helidon SE OCI Integration provides easy access to Oracle Cloud
Infrastructure using the OCI Java SDK.

# Usage

It is recommended that you use the OCI Java SDK directly, in particular
the Async clients. All you need to do is configure and create an OCI SDK
Client object. The configuration primarily consists of setting up
authenticate with OCI.

## Configuring the OCI SDK Client

Authentication with OCI is abstracted through
`AuthenticationDetailsProvider`.

If your environment is already set up to work with the OCI SDK or the
OCI command line, then it is very likely you do not need to do any
additional configuration. It is recommended that you do this first, and
verify your configuration by using the [OCI
CLI](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/javasdk.htm)
to access the service.

``` java
ConfigFile config = ConfigFileReader.parse("~/.oci/config", "DEFAULT");
AuthenticationDetailsProvider authProvider = new ConfigFileAuthenticationDetailsProvider(config);
```

You also need to add the following dependency to your application for
this

``` xml
<dependency>
    <groupId>com.oracle.oci.sdk</groupId>
    <artifactId>oci-java-sdk-common-httpclient-jersey3</artifactId>
    <scope>runtime</scope>
</dependency>
```

## Accessing OCI Services

Once you have authentication with OCI configured, you can use it to
access any OCI service supported by the OCI SDK. You will need to add
dependencies for the specific ODI SDK clients you will use.

# Examples

This example describes how to access OCI Object Storage.

As mentioned above in [Accessing OCI
Services](#_accessing_oci_services), you need to add a dependency on the
OCI SDK Object Storage API:

``` xml
<dependency>
    <groupId>com.oracle.oci.sdk</groupId>
    <artifactId>oci-java-sdk-objectstorage</artifactId>
</dependency>
```

## Creating an Object Storage Client

Now you can create OCI SDK Clients.

``` java
ConfigFile config = ConfigFileReader.parse("~/.oci/config", "DEFAULT");
AuthenticationDetailsProvider authProvider = new ConfigFileAuthenticationDetailsProvider(config);
ObjectStorageAsync objectStorageAsyncClient = new ObjectStorageAsyncClient(authProvider);
```

## Using the Object Storage client

Once you have created an ObjectStorage client you can use it as
described in:

- [OCI SDK Object Storage
  Javadocs](https://docs.oracle.com/en-us/iaas/tools/java/latest/com/oracle/bmc/objectstorage/package-summary.html)

- [OCI Object Storage
  Overview](https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/objectstorageoverview.htm)

# References

- [OCI SDK Usage
  Examples](https://github.com/helidon-io/helidon-examples/tree/helidon-4.x/examples/integrations/oci)

- [OCI
  Documentation](https://docs.oracle.com/en-us/iaas/Content/home.htm)
