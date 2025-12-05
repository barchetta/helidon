# Introduction

Most of the Helidon documentation is Linux/Mac/Unix centric. This
document gives some tips for Windows users.

# Prerequisites

Windows 10 is required.

For general pre-requisites like Java and Maven see [Getting
Started](prerequisites.md). If you want to use the [Helidon
CLI](cli.md) you’ll also need to install the Visual C++ Redistributable
Runtime:

- [x64](https://aka.ms/vs/16/release/vc_redist.x64.exe)

- [x86](https://aka.ms/vs/16/release/vc_redist.x86.exe)

We also recommend installing the following from the Microsoft Store:

- PowerShell

- Windows Terminal

This document assumes you will be using PowerShell.

# Maven Quickstart Archetypes

## Helidon SE

``` bash
mvn "-U" "archetype:generate" "-DinteractiveMode=false" `
    "-DarchetypeGroupId=io.helidon.archetypes" `
    "-DarchetypeArtifactId=helidon-quickstart-se" `
    "-DarchetypeVersion=4.4.0-SNAPSHOT" `
    "-DgroupId=io.helidon.examples" `
    "-DartifactId=helidon-quickstart-se" `
    "-Dpackage=io.helidon.examples.quickstart.se"
```

You can then follow the instructions in the [Helidon SE
Quickstart](../se/guides/quickstart.md). If you do not have `curl`
installed you can use `Invoke-WebRequest`:

``` bash
Invoke-WebRequest -Uri "http://localhost:8080/greet"
```

## Helidon MP

``` bash
mvn "-U" "archetype:generate" "-DinteractiveMode=false" `
    "-DarchetypeGroupId=io.helidon.archetypes" `
    "-DarchetypeArtifactId=helidon-quickstart-mp" `
    "-DarchetypeVersion=4.4.0-SNAPSHOT" `
    "-DgroupId=io.helidon.examples" `
    "-DartifactId=helidon-quickstart-mp" `
    "-Dpackage=io.helidon.examples.quickstart.mp"
```

You can then follow the instructions in the [Helidon MP
Quickstart](../mp/guides/quickstart.md). If you do not have `curl`
installed you can use `Invoke-WebRequest`:

``` bash
Invoke-WebRequest -Uri "http://localhost:8080/greet"
```
