# nuxt/content

## Intro
See [Documentation](https://content.nuxtjs.org/) for a full list of features.
There are 2 highlights
- Git-based headless CMS (read from file system) + MongoDB-like Query
- Nice, pluginable Markdown rendering system

Here are the ones I found particularly useful:
- Full-text search
- Static Site Generation
- MongoDB-like Query API
- Table of Content
- Support for Markdown, CSV, YAML, JSON, XML
- Extensibility with plugins

This module acts as a git-based headless CMS allowing user to query files from file system and display them nicely (with code highlight and latex). External CMS is also supported, because query (git-based headless CMS) and rendering are 2 separate things. Using external (remote) CMS doesn't mean you can't render the content any more. 

There are a bunch of plugins you can choose from to improve the experience and functionalities. If all you want is standard documentation without too much customization, then this is perfect.

## Docs Theme
It contains a [theme](https://content.nuxtjs.org/themes/docs) for documentation which many nuxt documentations are built on. It's basically a starter template where user just need to write markdown files and the documentation is rendered nicely. Ths Docs theme is perfect for simple documentation that doesn't contain too many functionalities and pages. Nuxt has lots of functionalities and their documentations are divide into many separate modules.

## Customization and Configuration
If you don't use the [Docs Theme](https://content.nuxtjs.org/themes/docs), you can write your own layout like regular nuxt apps. The tag `<nuxt-content />` will render the markdown file you passed to it.

This means that in a vue file, all you do is fetching the document content and pass the content to `<nuxt-content document="page" />`. It's simple and clean to use, but you may have custom configurations you want to make, which can be done using plugins (local or external).

See [Configuration] for what can be customized. All configurations can be set in `nuxt.config.js`.

There are many configuration options, for example the `liveEdit` boolean attribute enables you to edit markdown within browser in development. The edited file will be saved to the file system which is convenient for small changes.

### Markdown
The [markdown](https://content.nuxtjs.org/configuration#markdown) configuration is definitely the most important option which let's you customize how you want your markdown file to be rendered using plugins, both external plugin and local plugin are supported.

#### Sample

`nuxt.config.js`

```js
export default {
  content: {
    markdown: {
      remarkPlugins: [
		['remark-emoji', { emoticon: true }],
        '~/plugins/my-custom-remark-plugin.js'    // local plugin
      ]
    }
  }
}
```
The following plugins enables math equation to be rendered.
```js
...
content: {
  markdown: {
    prism: {
      theme: false,
    },
    remarkPlugins: ['remark-math'],
    rehypePlugins: ['rehype-mathjax'],
  },
},
...
```

There are a list of [remark](https://github.com/remarkjs/remark/blob/main/doc/plugins.md#list-of-plugins) and [rehype](https://github.com/rehypejs/rehype/blob/main/doc/plugins.md#list-of-plugins) plugins.

#### [Code Highlight](https://content.nuxtjs.org/configuration#markdownprismtheme)
Code Highlight is a must for programmers and one of the reason I don't use [medium](https://medium.com/) to write blog.

[Prism](https://prismjs.com/) is supported by default.

[highlight.js](https://highlightjs.org/) is also [supported](https://content.nuxtjs.org/configuration#markdownhighlighter).


## [Hooks](https://content.nuxtjs.org/advanced#hooks)
They are like middlewares or setup and teardown functions, which are run in different stages or Markdown rendering. 
### `content:file:beforeParse`
e.g. you may change file content before parsing it.
### `content:file:beforeInsert`
After parsing, you many add attributes (e.g. reading time estimate) to the parsed document.
### `content:options`
Change options if necessary.

## [Handling Hot Reload](https://content.nuxtjs.org/advanced#handling-hot-reload)
Write plugins to do anything during hot reload during development.


## Usage
See [Snippets](https://content.nuxtjs.org/snippets) for sample usage.

## Sample Project

[Nuxt-Content-Blog-Starter](https://github.com/TannerGilbert/Nuxt-Content-Blog-Starter)
