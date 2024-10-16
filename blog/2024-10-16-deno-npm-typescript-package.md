---
title: Problem with Deno + DOM + NPM Package
---

I get type error with TypeScript when I try to use Deno + DOM in an npm package.

Normally, a Deno package is a standalone Deno package with a `deno.json` file, without `package.json` or `tsconfig.json`.
That's the point of using Deno. 

However, I have a package with all kinds of code, divided into many subpackages, some runs in browser, some in Deno, some in Node.

Then there could be many type errors

## Missing Deno

When Deno VSCode extension disabled, `Deno` gloabal var is missing.

Create `deno.d.ts` in root

```bash
deno types > deno.d.ts
```

## Missing DOM

If you code contains dom operation, like using `document.` or `KeyboardEvent`, adding `deno.d.ts` will cause DOM and other types to be missing.

This is because the following lines are added to `deno.d.ts`

```ts
/// <reference no-default-lib="true" />
/// <reference lib="esnext" />
/// <reference lib="deno.net" />

```

Simply remove the first line containing `no-default-lib`.

Then other libs specified in `tsconfig.json` will be loaded.

This works for me, but may not be the best solution for other use cases. 

Deno and DOM packages should be separated into multiple packages when feasible.
