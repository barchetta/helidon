# Model Context Protocol (MCP) Server

Helidon provides support for building Model Context Protocol (MCP)
servers through a dedicated extension. The MCP Server feature is not
part of the core Helidon Framework – it is delivered as a separate
project hosted in the [helidon-mcp GitHub
repository](https://github.com/helidon-io/helidon-mcp).

## What is MCP?

The [Model Context Protocol (MCP)](https://modelcontextprotocol.io) is
an open protocol designed to connect AI models with external tools,
resources, and data sources in a standardized way. An MCP server exposes
resources, prompts, and tools that AI clients can discover and invoke
dynamically, enabling more powerful and context-aware applications.

## Helidon MCP Server Extension

The Helidon MCP Server extension allows you to build and run MCP servers
with Helidon.

Key points:

- Separate repository:
  [helidon-mcp](https://github.com/helidon-io/helidon-mcp)

- Independent lifecycle: Requires Helidon but has its own versioning and
  release cadence

- Dedicated documentation: Full usage guides, configuration details, and
  examples are provided directly in the [helidon-mcp
  documentation](https://github.com/helidon-io/helidon-mcp#documentation)

## Next Steps

To get started:

1.  Visit the [helidon-mcp GitHub
    repository](https://github.com/helidon-io/helidon-mcp).

2.  Follow the setup and usage instructions in the repository’s
    documentation.

3.  Explore how to expose your Helidon resources as MCP tools, prompts,
    and data sources.

# MCP Client

Helidon includes support for an MCP client through its [integration with
LangChain4j](../../se/ai/langchain4j/langchain4j.xml#_mcp_client).
With this integration, you can set up the MCP client using Helidon
configuration and plug it directly into your LangChain4j AI services.
