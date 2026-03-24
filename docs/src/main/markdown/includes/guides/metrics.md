# What You Need

This guide describes how to create a sample Helidon {intro-project-name} project that can be used to run some basic examples using both built-in and custom {metrics} with Helidon.

## What You Need

For this 30 minute tutorial, you will need the following:

|  |  |
|----|----|
| [Java SE 21](https://www.oracle.com/technetwork/java/javase/downloads) ([Open JDK 21](http://jdk.java.net)) | Helidon requires Java 21+ (25+ recommended). |
| [Maven 3.8+](https://maven.apache.org/download.cgi) | Helidon requires Maven 3.8+. |
| [Docker 18.09+](https://docs.docker.com/install/) | If you want to build and run Docker containers. |
| [Kubectl 1.16.5+](https://kubernetes.io/docs/tasks/tools/install-kubectl/) | If you want to deploy to Kubernetes, you need `kubectl` and a Kubernetes cluster (you can [install one on your desktop](../../about/kubernetes.md)). |
| [Helm](https://github.com/helm/helm) | To manage Kubernetes applications. |

*Verify Prerequisites*

``` bash
java -version
mvn --version
docker --version
kubectl version
```

*Setting JAVA_HOME*

``` bash
# On Mac
export JAVA_HOME=`/usr/libexec/java_home -v 21`

# On Linux
# Use the appropriate path to your JDK
export JAVA_HOME=/usr/lib/jvm/jdk-21
```

### Create a Sample Helidon {h1-prefix} Project

Use the Helidon {h1-prefix} Maven archetype to create a simple project that can be used for the examples in this guide.

*Run the Maven archetype*

``` bash
mvn -U archetype:generate -DinteractiveMode=false \
    -DarchetypeGroupId=io.helidon.archetypes \
    -DarchetypeArtifactId=helidon-quickstart-{flavor-lc} \
    -DarchetypeVersion={helidon-version} \
    -DgroupId=io.helidon.examples \
    -DartifactId=helidon-quickstart-{flavor-lc} \
    -Dpackage=io.helidon.examples.quickstart.{flavor-lc}
```

### Using the Built-In {metrics_uc}

Helidon provides three built-in scopes of metrics: base, vendor, and application. Here are the metric endpoints:

1.  `{metrics-endpoint}?scope=base` - Base {metrics}

2.  `{metrics-endpoint}?scope=vendor` - Helidon-specific {metrics}

3.  `{metrics-endpoint}?scope=application` - Application-specific metrics data.

Applications can add their own custom scopes as well simply by specifying a custom scope name when registering a {metric}.

> [!NOTE]
> The `{metrics-endpoint}` endpoint returns data for all scopes.

The built-in {metrics} fall into these categories:

1.  JVM behavior (in the base scope), and

2.  basic key performance indicators for request handling (in the vendor scope).

A later section describes the [key performance indicator {metrics}](#basic-and-extended-kpi) in detail.

The following example demonstrates how to use the other built-in {metrics}. All examples are executed from the root directory of your project (helidon-quickstart-{flavor-lc}).

    <dependency>
        <groupId>io.helidon.metrics</groupId>
        <artifactId>helidon-metrics</artifactId>
    </dependency>

*Build the application and then run it:*

``` bash
mvn package
java -jar target/helidon-quickstart-{flavor-lc}.jar
```

> [!NOTE]
> Metrics output can be returned in either text format (the default), or JSON. The text format uses OpenMetrics (Prometheus) Text Format, see <https://prometheus.io/docs/instrumenting/exposition_formats/#text-format-details>.

*Verify the metrics endpoint in a new terminal window:*

``` bash
curl http://localhost:8080{metrics-endpoint}
```

You can get the same data in JSON format.

*Verify the metrics endpoint with an HTTP accept header:*

``` bash
curl -H "Accept: application/json"  http://localhost:8080{metrics-endpoint}
```

        "gc.total;name=G1 Young Generation": 2,
        "cpu.systemLoadAverage": 11.0546875,
        "classloader.loadedClasses.count": 5124.0,
        "thread.count": 23.0,
        "classloader.unloadedClasses.total": 0,
        "vthreads.recentPinned": {
          "count": 0,
          "max": 0.0,
          "mean": 0.0,
          "elapsedTime": 0.0,
          "p0.5": 0.0,
          "p0.75": 0.0,
          "p0.95": 0.0,
          "p0.98": 0.0,
          "p0.99": 0.0,
          "p0.999": 0.0
        },
        "jvm.uptime": 138.233,
        "gc.time;name=G1 Young Generation": 0,
        "memory.committedHeap": 541065216,
        "thread.max.count": 26.0,
        "vthreads.pinned": 0,
        "cpu.availableProcessors": 8.0,
        "classloader.loadedClasses.total": 5124,
        "thread.daemon.count": 20.0,
        "memory.maxHeap": 8589934592,
        "memory.usedHeap": 2.774652E+7,
        "thread.starts": 28.0,
        "vthreads.submitFailures": 0
    // end::base-metrics-json-output[]
    // tag::vendor-metrics-json-output[]
      "vendor": {
        "requests.count": 3
      }

You can get a single metric by specifying the scope and name as query parameters in the URL.

*Get the Helidon `requests.count` {metric}:*

``` bash
curl -H "Accept: application/json"  'http://localhost:8080{metrics-endpoint}?scope=vendor&name=requests.count'
```

*JSON response:*

``` json
{
  "requests.count": 6
}
```

The `base` {metrics} illustrated above provide some insight into the behavior of the JVM in which the server runs.

The `vendor` {metric} shown above gives an idea of the request traffic the server is handling. See the [later section](#basic-and-extended-kpi) for more information on the basic and extended key performance indicator {metrics}.

### Controlling Metrics Behavior

By adding a `metrics` section to your application configuration you can control how the Helidon metrics subsystem behaves in any of several ways.

- [Disable metrics subsystem entirely](#disabling-entirely).

- Select whether to collect [extended key performance indicator {metrics}](#basic-and-extended-kpi).

- Control reporting of [virtual threads {metrics}](#controlling-vthreads).

#### Disabling Metrics Subsystem Entirely

You can disable the metrics subsystem entirely using configuration:

With metrics processing disabled, Helidon never updates any {metrics} and the `{metrics-endpoint}` endpoints respond with `404`.

#### Enabling and Disabling Metrics Usage by a Component

Helidon contains several components and integrations which register and update metrics. Depending on how the component is written, you might be able to disable just that component’s use of metrics:

*Configuration properties file disabling a component’s use of metrics*

``` properties
some-component.metrics.enabled=false
```

Check the documentation for a specific component to find out whether that component uses metrics and whether it allows you to disable that use. If you disable a component’s use of metrics, Helidon does not register the component’s metrics in the visible metrics registries nor do those metrics ever update their values. The response from the `/metrics` endpoint excludes that component’s metrics.

Note that if you disable metrics processing entirely, no component updates its metrics regardless of any component-level metrics settings.

#### Controlling Metrics By Registry Type and Metric Name

You can control the collection and reporting of metrics by registry type and metric name within registry type.

##### Disabling All Metrics of a Given Registry Type

To disable all metrics in a given registry type (application, vendor, or base), add one or more groups to the configuration:

*Disabling `base` and `vendor` metrics (properties format)*

``` properties
metrics.registries.0.type = base
metrics.registries.0.enabled = false
metrics.registries.1.type = vendor
metrics.registries.1.enabled = false
```

*Disabling `base` and `vendor` metrics (YAML format)*

``` yaml
metrics:
  registries:
    - type: base
      enabled: false
    - type: vendor
      enables: false
```

##### Controlling Metrics by Metric Name

You can be even more selective. Within a registry type you can configure up to two regular expression patterns:

- one matching metric names to *exclude*, and

- one matching metric names to *include*.

Helidon updates and reports a metric only if two conditions hold:

- the metric name *does not* match the `exclude` regex pattern (if you define one), and

- either

  - there is no `include` regex pattern, or

  - the metric name matches the `include` pattern.

> [!CAUTION]
> Make sure any `include` regex pattern you specify matches *all* the metric names you want to capture.

Suppose your application creates and updates a group of metrics with names such as `myapp.xxx.queries`, `myapp.xxx.creates`, `myapp.xxx.updates`, and `myapp.xxx.deletes` where `xxx` can be either `supplier` or `customer`.

The following example gathers all metrics *except* those from your application regarding suppliers:

*Disabling metrics by name (properties format)*

``` properties
metrics.registries.0.type = application
metrics.registries.0.filter.exclude = myapp\.supplier\..*
```

The following settings select the particular subset of the metrics created in your application code representing updates of customers and suppliers:

*Enabling metrics by name (properties format)*

``` properties
metrics.registries.0.type = application
metrics.registries.0.filter.include = myapp\..*\.updates
```

If you use the YAML configuration format, enclose the regex patterns in single-quote marks:

*Enabling metrics by name (YAML format)*

``` yaml
metrics:
  registries:
    - type: application
      filter:
        include: 'myapp\..*\.updates'
```

The next example selects only your application’s metrics while excluding those which refer to deletions:

*Combining `include` and `exclude`*

``` properties
metrics.registries.0.type = application
metrics.registries.0.filter.include = myapp\..*
metrics.registries.0.filter.exclude = myapp\..*/deletes
```

Helidon would not update or report the metric `myapp.supplier.queries`, for example. To include metrics from your application for both updates and queries (but not for other operations), you could change the settings in the previous example to this:

    metrics.registries.0.type = application
    metrics.registries.0.filter.include = myapp\..*\.updates|myapp\..*\.queries
    metrics.registries.0.filter.exclude = myapp\..*/deletes

#### Collecting Basic and Extended Key Performance Indicator (KPI) Metrics

Any time you include the Helidon metrics module in your application, Helidon tracks a basic performance indicator {metric}: a `Counter` of all requests received (`requests.count`).

Helidon {h1-prefix} also includes additional, extended KPI metrics which are disabled by default:

- current number of requests in-flight - a `Gauge` (`requests.inFlight`) of requests currently being processed

- long-running requests - a `Counter` (`requests.longRunning`) measuring the total number of requests which take at least a given amount of time to complete; configurable, defaults to 10000 milliseconds (10 seconds)

- load - a `Counter` (`requests.load`) measuring the number of requests worked on (as opposed to received)

- deferred - a `Gauge` (`requests.deferred`) measuring delayed request processing (work on a request was delayed after Helidon received the request)

You can enable and control these {metrics} using configuration:

#### Controlling Meters Related to Virtual Threads Behavior

Helidon optionally maintains several {metrics} related to virtual threads as summarized in the next table. Helidon might rely on Java Flight Recorder (JFR) events and JMX MBeans in computing the {metric} values. Be aware that limitations or changes in the values provided by these sources are outside the control of Helidon.

For performance reasons Helidon does not report virtual thread {metrics} unless you enable them using configuration.

| {metric_uc} name | Usage | Source |
|----|----|----|
| `vthreads.count` | Current number of active virtual threads. | JFR `jdk.virtualThreadStart` and `jdk.virtualThreadEnd` events |
| `vthreads.pinned` | Number of times virtual threads have been pinned. | JFR `jdk.virtualThreadPinned` event |
| `vthreads.recentPinned` | Distribution of the duration of thread pinning. <sup>1</sup> | JFR `jdk.virtualThreadPinned` event |
| `vthreads.started` | Number of virtual threads started. | JFR `jdk.virtualThreadStart` event |
| `vthreads.submitFailed` | Number of times submissions of a virtual thread to a platform carrier thread failed. | JFR `jdk.virtualThreadSubmitFailed` event |

{metrics_uc} for Virtual Threads

<sup>1</sup> Distribution summaries can discard stale data, so the `recentPinned` summary might not reflect all thread pinning activity. <sup>1</sup> Distribution summaries can discard stale data, so the `recentPinned` summary might not reflect all thread pinning activity.

#### Configuring Virtual Threads {metrics_uc}

##### Enabling Virtual Threads {metrics_uc}

Gathering data to compute the {metrics} for virtual threads is designed to be as efficient as possible, but doing so still imposes a load on the server and by default Helidon does not report {metrics} related to virtual threads.

To enable the {metrics} describing virtual threads include a config setting as shown in the following example.

##### Controlling Measurements of Pinned Virtual Threads

*Enabling virtual thread {metrics}*

Helidon measures pinned virtual threads only when the thread is pinned for a length of time at or above a threshold. Control the threshold as shown in the example below.

*Setting virtual thread pinning threshold to 100 ms*

The threshold value is a `Duration` string, such as `PT0.100S` for 100 milliseconds.

### Metrics Metadata

Each {metric} has associated metadata that includes:

1.  name: The name of the {metric}.

2.  units: The unit of the {metric} such as time (seconds, milliseconds), size (bytes, megabytes), etc.

3.  a description of the {metric}.

You can get the metadata for any scope, such as `{metrics-endpoint}?scope=base`, as shown below:

*Get the metrics metadata using HTTP OPTIONS method:*

``` bash
 curl -X OPTIONS -H "Accept: application/json"  'http://localhost:8080{metrics-endpoint}?scope=base'
```

*JSON response (truncated):*

``` json
{
   "classloader.loadedClasses.count": {
      "type": "gauge",
      "description": "Displays the number of classes that are currently loaded in the Java virtual machine."
    },
   "jvm.uptime": {
      "type": "gauge",
      "unit": "seconds",
      "description": "Displays the start time of the Java virtual machine in milliseconds. This attribute displays the approximate time when the Java virtual machine started."
    },
   "memory.usedHeap": {
      "type": "gauge",
      "unit": "bytes",
      "description": "Displays the amount of used heap memory in bytes."
    }
}
```

### Integration with Kubernetes and Prometheus

#### Kubernetes Integration

The following example shows how to integrate the Helidon {h1-prefix} application with Kubernetes.

*Stop the application and build the docker image:*

``` bash
docker build -t helidon-metrics-{flavor-lc} .
```

*Create the Kubernetes YAML specification, named `metrics.yaml`, with the following content:*

``` yaml
kind: Service
apiVersion: v1
metadata:
  name: helidon-metrics 
  labels:
    app: helidon-metrics
  annotations:
    prometheus.io/scrape: "true" 
spec:
  type: NodePort
  selector:
    app: helidon-metrics
  ports:
    - port: 8080
      targetPort: 8080
      name: http
---
kind: Deployment
apiVersion: apps/v1
metadata:
  name: helidon-metrics
spec:
  replicas: 1 
  selector:
    matchLabels:
      app: helidon-metrics
  template:
    metadata:
      labels:
        app: helidon-metrics
        version: v1
    spec:
      containers:
        - name: helidon-metrics
          image: helidon-metrics-{flavor-lc}
          imagePullPolicy: IfNotPresent
          ports:
            - containerPort: 8080
```

- A service of type `NodePort` that serves the default routes on port `8080`.

- An annotation that will allow Prometheus to discover and scrape the application pod.

- A deployment with one replica of a pod.

*Create and deploy the application into Kubernetes:*

``` bash
kubectl apply -f ./metrics.yaml
```

*Get the service information:*

``` bash
kubectl get service/helidon-metrics
```

``` bash
NAME             TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
helidon-metrics   NodePort   10.99.159.2   <none>        8080:31143/TCP   8s 
```

- A service of type `NodePort` that serves the default routes on port `31143`.

*Verify the metrics endpoint using port `30116`, your port will likely be different:*

``` bash
curl http://localhost:31143/metrics
```

> [!NOTE]
> Leave the application running in Kubernetes since it will be used for Prometheus integration.

#### Prometheus Integration

The metrics service that you just deployed into Kubernetes is already annotated with `prometheus.io/scrape:`. This will allow Prometheus to discover the service and scrape the metrics. This example shows how to install Prometheus into Kubernetes, then verify that it discovered the Helidon metrics in your application.

*Install Prometheus and wait until the pod is ready:*

``` bash
helm install stable/prometheus --name metrics
export POD_NAME=$(kubectl get pods --namespace default -l "app=prometheus,component=server" -o jsonpath="{.items[0].metadata.name}")
kubectl get pod $POD_NAME
```

You will see output similar to the following. Repeat the `kubectl get pod` command until you see `2/2` and `Running`. This may take up to one minute.

``` bash
metrics-prometheus-server-5fc5dc86cb-79lk4   2/2     Running   0          46s
```

*Create a port-forward, so you can access the server URL:*

``` bash
kubectl --namespace default port-forward $POD_NAME 7090:9090
```

Now open your browser and navigate to `http://localhost:7090/targets`. Search for helidon on the page, and you will see your Helidon application as one of the Prometheus targets.

#### Final Cleanup

You can now delete the Kubernetes resources that were just created during this example.

*Delete the Prometheus Kubernetes resources:*

``` bash
helm delete --purge metrics
```

*Delete the application Kubernetes resources:*

``` bash
kubectl delete -f ./metrics.yaml
```
