# Markdown Extension Examples

This page demonstrates some of the built-in markdown extensions provided by VitePress.

## Link To API Examples

1. Markdown: [api-examples.md](api-examples.md)
2. Markdown: [api-examples.html](api-examples.html)
3. Markdown: [api-examples](api-examples)
4. HTML: <a href="api-examples.md">api-examples.md</a>
5. HTML: <a href="api-examples.html">api-examples.html</a>
6. HTML: <a href="api-examples">api-examples</a>

## Syntax Highlighting

VitePress provides Syntax Highlighting powered by [Shiki](https://github.com/shikijs/shiki), with additional features like line-highlighting:

**Input**

````md
```js{4}
export default {
  data () {
    return {
      msg: 'Highlighted!'
    }
  }
}
```
````

**Output**

```js{4}
export default {
  data () {
    return {
      msg: 'Highlighted!'
    }
  }
}
```

## Custom Containers

**Input**

```md
::: info
This is an info box.
:::

::: tip
This is a tip.
:::

::: warning
This is a warning.
:::

::: danger
This is a dangerous warning.
:::

::: details
This is a details block.
:::
```

**Output**

::: info
This is an info box.
:::

::: tip
This is a tip.
:::

::: warning
This is a warning.
:::

::: danger
This is a dangerous warning.
:::

::: details
This is a details block.
:::

## More

Check out the documentation for the [full list of markdown extensions](https://vitepress.dev/guide/markdown).
