# Overview

Scheduling is an essential feature for the Enterprise. Helidon has its
own implementation of Scheduling functionality based on
[Cron-utils](https://github.com/jmrozanec/cron-utils).

# Maven Coordinates

To enable Scheduling, add the following dependency to your project’s
`pom.xml` (see [Managing
Dependencies](../about/managing-dependencies.md)).

``` xml
<dependency>
    <groupId>io.helidon.scheduling</groupId>
    <artifactId>helidon-scheduling</artifactId>
</dependency>
```

# Usage

For scheduling periodic tasks, it is possible to choose a fixed rate or
a Cron expression.

## Fixed rate

<div class="formalpara">

<div class="title">

Scheduling with fixed rate using `Scheduling.fixedRate()` builder.

</div>

``` java
FixedRate.builder()
        .delay(10)
        .initialDelay(5)
        .timeUnit(TimeUnit.MINUTES)
        .task(inv -> System.out.println("Every 10 minutes, first invocation 5 minutes after start"))
        .build();
```

</div>

Metadata like human-readable interval description or configured values
are available through FixedRateInvocation provided as task parameter.

<div class="formalpara">

<div class="title">

Invocation metadata

</div>

``` java
FixedRate.builder()
        .delay(10)
        .task(inv -> System.out.println("Method invoked " + inv.description()))
        .build();
```

</div>

Type:
[io.helidon.scheduling.FixedRate](/apidocs/io.helidon.scheduling/io/helidon/scheduling/FixedRate.html)

### Configuration options

<table style="width:100%;">
<caption>Required configuration options</caption>
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
<td style="text-align: left;"><p><span
class="line-through"><code>delay</code></span></p></td>
<td style="text-align: left;"><p>long</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p><strong>Deprecated</strong> Fixed rate
delay between each invocation. Time unit is by default
java.util.concurrent.TimeUnit.SECONDS, can be specified with
io.helidon.scheduling.FixedRateConfig.Builder.timeUnit(java.util.concurrent.TimeUnit).</p>
<p>@deprecated use io.helidon.scheduling.FixedRateConfig.interval()
instead</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><span
class="line-through"><code>initial-delay</code></span></p></td>
<td style="text-align: left;"><p>long</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p><strong>Deprecated</strong> Initial
delay of the first invocation. Time unit is by default
java.util.concurrent.TimeUnit.SECONDS, can be specified with
io.helidon.scheduling.FixedRateConfig.Builder.timeUnit(java.util.concurrent.TimeUnit)
timeUnit().</p>
<p>@deprecated use io.helidon.scheduling.FixedRateConfig.delayBy()
instead</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>interval</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Fixed interval between each
invocation.</p></td>
</tr>
</tbody>
</table>

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
<td style="text-align: left;"><p><code>delay-by</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p><code>PT0S</code></p></td>
<td style="text-align: left;"><p>Initial delay of the first
invocation.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>delay-type</code></p></td>
<td style="text-align: left;"><p>DelayType (SINCE_PREVIOUS_START,
SINCE_PREVIOUS_END)</p></td>
<td
style="text-align: left;"><p><code>DelayType.SINCE_PREVIOUS_START</code></p></td>
<td style="text-align: left;"><p>Configure whether the interval between
the invocations should be calculated from the time when previous task
started or ended. Delay type is by default
FixedRate.DelayType.SINCE_PREVIOUS_START.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>SINCE_PREVIOUS_START</code>: Next invocation start is
measured from the previous invocation task start.</p></li>
<li><p><code>SINCE_PREVIOUS_END</code>: Next invocation start is
measured from the previous invocation task end.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>id</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Identification of the started task.
This can be used to later look up the instance, for example to cancel
it.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><span
class="line-through"><code>time-unit</code></span></p></td>
<td style="text-align: left;"><p>TimeUnit (NANOSECONDS, MICROSECONDS,
MILLISECONDS, SECONDS, MINUTES, HOURS, DAYS)</p></td>
<td
style="text-align: left;"><p><code>TimeUnit.TimeUnit.SECONDS</code></p></td>
<td style="text-align: left;"><p><strong>Deprecated</strong>
java.util.concurrent.TimeUnit TimeUnit used for interpretation of values
provided with io.helidon.scheduling.FixedRateConfig.Builder.delay(long)
and
io.helidon.scheduling.FixedRateConfig.Builder.initialDelay(long).</p>
<p>@deprecated as duration is used for new options, this option is not
needed</p></td>
</tr>
</tbody>
</table>

## Cron

For more complicated interval definition, Cron expression can be
leveraged with `Scheduling.cron()` builder.

<div class="formalpara">

<div class="title">

Scheduling with Cron expression

</div>

``` java
Cron.builder()
        .expression("0 15 8 ? * *")
        .task(inv -> System.out.println("Executer every day at 8:15"))
        .build();
```

</div>

Type:
[io.helidon.scheduling.Cron](/apidocs/io.helidon.scheduling/io/helidon/scheduling/Cron.html)

### Configuration options

<table style="width:100%;">
<caption>Required configuration options</caption>
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
<td style="text-align: left;"><p><code>expression</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Cron expression for specifying period
of execution.</p>
<p><strong>Examples:</strong></p>
<ul>
<li><p><code>0/2 * * * * ? *</code> - Every 2 seconds</p></li>
<li><p><code>0 45 9 ? * *</code> - Every day at 9:45</p></li>
<li><p><code>0 15 8 ? * MON-FRI</code> - Every workday at 8:15</p></li>
</ul></td>
</tr>
</tbody>
</table>

| key | type | default value | description |
|----|----|----|----|
| `concurrent` | boolean | `true` | Allow concurrent execution if previous task didn’t finish before next execution. Default value is `true`. |
| `id` | string |   | Identification of the started task. This can be used to later look up the instance, for example to cancel it. |

Optional configuration options

## Cron expression syntax

Cron expressions should be configured as follows.

## Cron expression

<div class="formalpara">

<div class="title">

Cron expression format

</div>

    <seconds> <minutes> <hours> <day-of-month> <month> <day-of-week> <year>

</div>

| Order | Name | Supported values | Supported field format | Optional |
|----|----|----|----|----|
| 1 | seconds | 0-59 | CONST, LIST, RANGE, WILDCARD, INCREMENT | false |
| 2 | minutes | 0-59 | CONST, LIST, RANGE, WILDCARD, INCREMENT | false |
| 3 | hours | 0-23 | CONST, LIST, RANGE, WILDCARD, INCREMENT | false |
| 4 | day-of-month | 1-31 | CONST, LIST, RANGE, WILDCARD, INCREMENT, ANY, LAST, WEEKDAY | false |
| 5 | month | 1-12 or JAN-DEC | CONST, LIST, RANGE, WILDCARD, INCREMENT | false |
| 6 | day-of-week | 1-7 or SUN-SAT | CONST, LIST, RANGE, WILDCARD, INCREMENT, ANY, NTH, LAST | false |
| 7 | year | 1970-2099 | CONST, LIST, RANGE, WILDCARD, INCREMENT | true |

Cron expression fields

| Name | Regex format | Example | Description |
|----|----|----|----|
| CONST | \d+ | 12 | exact value |
| LIST | \d+,\d+(,\d+)\* | 1,2,3,4 | list of constants |
| RANGE | \d+-\d+ | 15-30 | range of values from-to |
| WILDCARD | \\ | \* | all values withing the field |
| INCREMENT | \d+\\\d+ | 0/5 | initial number / increments, 2/5 means 2,7,9,11,16,…​ |
| ANY | \\ | ? | any day(apply only to day-of-week and day-of-month) |
| NTH | \\ | 1#3 | nth day of the month, 2#3 means third monday of the month |
| LAST | \d\*L(+\d+\|\\\d+)? | 3L-3 | last day of the month in day-of-month or last nth day in the day-of-week |
| WEEKDAY | \\ | 1#3 | nearest weekday of the nth day of month, 1W is the first monday of the week |

Field formats

| Cron expression      | Description           |
|----------------------|-----------------------|
| \* \* \* \* \* ?     | Every second          |
| 0/2 \* \* \* \* ? \* | Every 2 seconds       |
| 0 45 9 ? \* \*       | Every day at 9:45     |
| 0 15 8 ? \* MON-FRI  | Every workday at 8:15 |

Examples

Metadata like human-readable interval description or configured values
are available through CronInvocation provided as task parameter.

# Configuration

Scheduling is configurable with [Helidon
Config](../se/config/introduction.md).

<div class="formalpara">

<div class="title">

Example of configuring

</div>

``` java
FixedRate.builder()
        .config(Config.create(() -> ConfigSources.create(
                """
                        delay: 4
                        delay-type: SINCE_PREVIOUS_END
                        initial-delay: 1
                        time-unit: SECONDS
                        """,
                MediaTypes.APPLICATION_X_YAML)))
        .task(inv -> System.out.println("Every 4 minutes, first invocation 1 minutes after start"))
        .build();
```

</div>

# Task Management

A `io.helidon.scheduling.TaskManager` can be used to manage tasks that
are started within Helidon. When using imperative programming model, you
can either provide a custom implementation of this interface to task
builder (method `taskManager`), or you can use the "default" one that
can be obtained by invoking
`io.helidon.service.registry.Services.get(TaskManager.class)`. When
using the default `TaskManager` from
`io.helidon.service.registry.Services`, there is no need to explicitly
register it with the task builders.

When using declarative programming model, the `TaskManager` can be
injected. It is a `Singleton` service that will be used by all scheduled
tasks in the current application.

# Examples

## Fixed Rate Example

For simple fixed rate invocation use .

<div class="formalpara">

<div class="title">

Example of scheduling with fixed rate using `FixedRate.builder()`
builder.

</div>

``` java
FixedRate.builder()
        .delay(10)
        .initialDelay(5)
        .timeUnit(TimeUnit.MINUTES)
        .task(inv -> System.out.println("Every 10 minutes, first invocation 5 minutes after start"))
        .build();
```

</div>

Metadata like human-readable interval description or configured values
are available through `FixedRateInvocation` provided as task parameter.

<div class="formalpara">

<div class="title">

Example with invocation metadata

</div>

``` java
FixedRate.builder()
        .delay(10)
        .task(inv -> System.out.println("Method invoked " + inv.description()))
        .build();
```

</div>

# Reference

- [Cron-utils GitHub page](https://github.com/jmrozanec/cron-utils)

- [Helidon Scheduling
  JavaDoc](/apidocs/io.helidon.microprofile.scheduling/io/helidon/microprofile/scheduling/package-summary.html)
