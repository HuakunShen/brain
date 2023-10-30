# unifiedjs
> **unified** is an interface for processing text using syntax trees.

```
| ........................ process ........................... |
| .......... parse ... | ... run ... | ... stringify ..........|

          +--------+                     +----------+
Input ->- | Parser | ->- Syntax Tree ->- | Compiler | ->- Output
          +--------+          |          +----------+
                              X
                              |
                       +--------------+
                       | Transformers |
                       +--------------+
```

## Processors
The following projects process different [_syntax tree_](https://unifiedjs.com/explore/package/unified/#syntax-trees) formats.
-   [**rehype**](https://github.com/rehypejs/rehype) ([_hast_](https://github.com/syntax-tree/hast)) — HTML
-   [**remark**](https://github.com/remarkjs/remark) ([_mdast_](https://github.com/syntax-tree/mdast)) — Markdown
-   [**retext**](https://unifiedjs.com/explore/project/retextjs/retext/) ([_nlcst_](https://github.com/syntax-tree/nlcst)) — Natural language

There are many plugins available, you can also write your own.

## AST (Abstract Syntax Tree)
Use [AST Explorer ](https://astexplorer.net/#/gist/d9029a2e8827265fbb9b190083b59d4d/3384f3ce6a3084e50043d0c8ce34628ed7477603) to visualize