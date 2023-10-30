# markdown-link-check

## Intro

- [GitHub Repo](https://github.com/tcort/markdown-link-check)
- [npm package](https://www.npmjs.com/package/markdown-link-check)

You may install it globally or use it with npx.

```bash
npm i -g markdown-link-check

npx markdown-link-check filename.md
```

## Recursive Check

```bash
find . -name '*.md' -not -path "**/node_modules/*" -print0 | xargs -0 -n1 npx markdown-link-check --config ./md-link.json
```

For my note taking folders, I add a `Makefile` with the command above.

I also made an alias of it so I can easily execute it on CWD.

It's also a good practice to add it to GitHub action so that GitHub always run the check for you.

```yml
name: Markdown Link Check
on:
  push:
    branches:
      - master
      - develop
    paths:
      - '**.md'
      - '.github/workflows/*.yml'
  pull_request:
    paths:
      - '**.md'
      - '.github/workflows/*.yml'

jobs:
  markdown-link-check:
    name: Broken Links
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3
        with:
          submodules: recursive
      - name: Run link check
        run: |
          npm i -g markdown-link-check
          make check-markdown-link
```

Note that I added a `md-link.json` configuration file. It's not necessary. I added it because some websites with DDos protection (like cloudflare) will return status code 403 and will fail the check.

What I do is add 403 to the `aliveStatusCodes`.

```json
{
  "timeout": "20s",
  "retryOn429": true,
  "retryCount": 5,
  "fallbackRetryDelay": "30s",
  "aliveStatusCodes": [200, 206, 403]
}
```


