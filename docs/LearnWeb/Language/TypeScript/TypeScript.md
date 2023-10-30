---
title: TypeScript
---

- [Overview of TypeScript](#overview-of-typescript)
- [Demo Sample Code](#demo-sample-code)
- [tsconfig](#tsconfig)
  - [module \& target](#module--target)
  - [moduleResolution](#moduleresolution)
  - [esModuleInterop](#esmoduleinterop)
  - [paths](#paths)
- [package.json](#packagejson)
  - [(Dev)Dependencies](#devdependencies)
  - [type](#type)
  - [exports](#exports)
    - [exports for TypeScript](#exports-for-typescript)
      - [Explanation](#explanation)
      - [Sample](#sample)
  - [Package Entrypoints](#package-entrypoints)
- [Features](#features)
  - [Top-Level Await](#top-level-await)
          - [Top-Level Await Sample Code](#top-level-await-sample-code)
- [Bootstrap a Project](#bootstrap-a-project)
- [Bundler](#bundler)
- [Resource](#resource)

# Overview of TypeScript

> TypeScript is JavaScript with syntax for types.
> TypeScript is a strongly typed programming language that builds on JavaScript, giving you better tooling at any scale.

[Official Website](https://www.typescriptlang.org/)

[Cheat Sheets](https://www.typescriptlang.org/cheatsheets)

`npm i -g typescript`: Install TypeScript globally into your OS.

Browsers only runs JavaScript which has lots of limitations and is not statically typed. TypeScript is like a wrapper for JavaScript, providing a layer of typing to facilitate development. In the end, TypeScript will be compiled to JavaScript.

Over the years, many versions and standards were created for JavaScript and TypeScript. You may feel OK when building a small project or coding with starter code such as vite, vue, react; but it could get super annoying when you need to build something from scratch.

TypeScript is a huge topic. It gets very complex when you want to build a complex project with it.

You need to understand many concepts before building a TypeScript project, otherwise you may be blocked for some weird errors and couldn't find a solution online. The best solution to this is to learn all the basics before coding.

# Demo Sample Code

- [ts-esm-cjs](https://github.com/HuakunShen/ts-esm-cjs)
  - Nodejs's module system (commonjs + ESM) is currently a mess to work with. Some libraries supports both, some libraries supports one of them. You need to know the difference to work with them. I built this [ts-esm-cjs](https://github.com/HuakunShen/ts-esm-cjs) repo to demonstrate how to work with these modules.

# tsconfig

`tsc --init` generates a TypeScript configuration template with most of the fields commented out and each field with a short description. The description may not be enough for you to understand everything. I will discuss some of the most important fields here.

## module & target

`module` in tsconfig.json tells the compiler what syntax to use for the modules in the emitted .js files. Frequently used values are "commonjs" (require/module.exports) or "ES2015" (import/export keywords), but there are other module systems.

`module` affects the **module syntax** of emitted code while `target` affects the rest.

[Read More](https://stackoverflow.com/questions/55471795/what-is-module-option-in-tsconfig-used-for/61215252#61215252)

The module syntax deplends on the requirements (i.e. where the compiled JS code will be used, Nodejs or Browser).

- If it's for a server-side project that uses Node.js then probably CJS (commonjs).
- If it's for a frontend application (React, Vue, etc.), use ESM.

Nowadays, all the modern browsers and Node 13.2.0+ support the ESM format, so maybe always use EMS if possible.

Setting `module` to commonjs doesn't mean the produced js has to be commonjs. If `target` is set to es2015, you can still use JS keywords like `const` and `let`.

`esnext` is for future features that has not been officially released.

## moduleResolution

[Module Resolution Strategies](https://www.typescriptlang.org/docs/handbook/module-resolution.html#module-resolution-strategies)

> There are two possible module resolution strategies: Node and Classic. You can use the moduleResolution option to specify the module resolution strategy. If not specified, the default is Node for --module commonjs, and Classic otherwise (including when module is set to amd, system, umd, es2015, esnext, etc.).

So, if you are writing a server-side app using ESM format, the default strategy is "Classic", and you may want to switch to "node" to prevent errors.

## esModuleInterop

## paths

`paths` option can be used to set shortcuts for long file paths.

For example, `import Button from '../../../components/Button.ts'` can be simplified to `import Button from @components/Button.ts`.

However there are 2 things to keep in mind.

1. The `baseUrl` has to be set for `paths` to work.

```json
"baseUrl": "src",
"paths": {
  "@components/*": ["components/*"]
}
```

2. `ts-node` doesn't work with `paths`. You have to compile first, then run the `.js` file.
   1. To get `ts-node` working with `paths`, use `tsconfig-paths`. See https://typestrong.org/ts-node/docs/paths/
   2. `npm i -D tsconfig-paths`
   3. `tsconfig.json`:
      ```json
      {
        "ts-node": {
          // Do not forget to `npm i -D tsconfig-paths`
          "require": ["tsconfig-paths/register"]
        },
        ...
      }
      ```

> Emit additional JavaScript to ease support for importing CommonJS modules. This enables 'allowSyntheticDefaultImports' for type compatibility.

[ES Module Interop - esModuleInterop](https://www.typescriptlang.org/tsconfig#esModuleInterop)

# package.json

Every JS project has a `package.json` specifying the dependencies and other configurations.

## (Dev)Dependencies

## type

https://nodejs.org/api/packages.html#type

One problem you may encounter is that the compiler asks you to set `type` to be `module` when you import some libraries.

> The "type" field defines the module format that Node.js uses for all .js files that have that package.json file as their nearest parent.
> Files ending with .js are loaded as ES modules when the nearest parent package.json file contains a top-level field "type" with a value of "module".

Default type is "commonjs".

Regardless of the value of the "type" field, `.mjs` files are always treated as ES modules and `.cjs` files are always treated as CommonJS.

## exports

https://nodejs.org/api/packages.html#exports

Type: `<Object> | <string> | <string[]>`

The "exports" field allows defining the [entry points](https://nodejs.org/api/packages.html#package-entry-points) of a package when imported by name loaded either via a node_modules lookup or a self-reference to its own name. It is supported in Node.js 12+ as an alternative to the "main" that can support defining subpath exports and conditional exports while encapsulating internal unexported modules.

[Conditional Exports](https://nodejs.org/api/packages.html#conditional-exports) can also be used within "exports" to define different package entry points per environment, including whether the package is referenced via require or via import.

### exports for TypeScript

`exports` works well with nodejs. See my sample code here [ts-esm-cjs](https://github.com/HuakunShen/ts-esm-cjs).

However, it doesn't work with TypeScript as of Dec 2022. I tried many things and discovered that it's not possible as of now.

The problem is, TypeScript cannot find the subpath although it's declared in `package.json`.

I've seen many packages supporting subpath exports such as `@apollo/server`, e.g. `import { expressMiddleware } from '@apollo/server/express4';`.

So I learnt how they do it their way. It's not as elegant as the original nodejs version, but it works.

#### Explanation

- This is `@apollo/server`'s main `package.json`. `https://github.com/apollographql/apollo-server/blob/main/packages/server/package.json`
  - It's normal, same as how we define nodejs `exports`in `package.json`
- The trick is to add a new folder with a `package.json` in it.
  - The folder needs to have the same name as the subpath you want, in this case, it's `express4`.
  - See https://github.com/apollographql/apollo-server/tree/main/packages/server/express4 for how they do it.
  - The module name would be `"name": "@apollo/server/express4"` with the subpath.
  - Use traditional `main`, `module` and `types` to export `.cjs` (compiled commonjs), `.mjs` (compiled ESM) and `.d.ts` types declaration.

#### Sample

Suppose we have a package `core`, and want to have subpath `plugin` to allow users to `import plugin from "core/plugin"`.

**Folder Structure with depth=2**

```
├── dist
│   ├── index.d.ts
│   ├── index.cjs
│   ├── index.mjs
│   ├── plugin.d.ts
│   ├── plugin.cjs
│   ├── plugin.mjs
├── src
│   └── plugin
├── plugin
│   └── package.json
└── package.json
```

**Main `package.json`**

```json
{
  ...
  "type": "module",
  "exports": {
    ".": {
      "require": "./dist/index.cjs",
      "import": "./dist/index.mjs",
      "types": "./dist/index.d.ts"
    },
    "./plugin": {
      "require": "./dist/plugin.cjs",
      "import": "./dist/plugin.mjs",
      "types": "./dist/plugin.d.ts"
    }
  },
  ...
}
```

**`plugin/package.json`**

```json
{
  "name": "@crosscopy/core/plugin",
  "type": "module",
  "main": "../dist/plugin.js",
  "module": "../dist/plugin.mjs",
  "types": "../dist/plugin.d.ts",
  "sideEffects": false
}
```

## Package Entrypoints

https://nodejs.org/api/packages.html#package-entry-points

In a package's `package.json` file, two fields can define entry points for a package: `"main"` and `"exports"`. Both fields apply to both ES module and CommonJS module entry points.

> The `"main"` field is supported in all versions of Node.js, but its capabilities are **limited**: it only defines the main entry point of the package.

> The `"exports"`` provides a modern alternative to "main" allowing multiple entry points to be defined, conditional entry resolution support between environments, and preventing any other entry points besides those defined in "exports". This encapsulation allows module authors to clearly define the public interface for their package.

# Features

## Top-Level Await

The following error messages are I got when trying to use top-level await, it tells us serveral things to do.

> Top-level 'await' expressions are only allowed when the 'module' option is set to 'es2022', 'esnext', 'system', 'node16', or 'nodenext', and the 'target' option is set to 'es2017' or higher.

> 'await' expressions are only allowed at the top level of a file when that file is a module, but this file has no imports or exports. Consider adding an empty 'export {}' to make this file a module.

There are a few things to do to activate top-level await

1. In `package.json`, set `"type": "module"` to make the package an ESM module
2. In `tsconfig`
   1. Set `"target": "es2017"` or above
   2. Set `"module": "esnext"` or other options
3. Add `export {}` to the end of the TypeScript file to execute to make it a module.
4. Since it's a ESM module, if you want to run the script with `ts-node`, use `ts-node-esm` instead.

###### Top-Level Await Sample Code

```ts
async function main() {
  console.log("name");
}
await main();
export {};
```

# Bootstrap a Project

Read [Start a New Project](https://www.typescriptlang.org/docs/bootstrap). There are planty of boilerplates.

Update (Aug 2023): Look at archive https://web.archive.org/web/20220609161653/https://www.typescriptlang.org/docs/bootstrap, https://www.typescriptlang.org/docs/bootstrap is missing.


# Bundler

TypeScript relies on compiler and bundler to transform into JavaScript and achieve features like tree shaking, code spliting, compatibility, etc.

- [Webpack](../compiler/webpack.md)
- [Parcel](../compiler/parcel.md)
- [Rollup](../compiler/rollup.md)
- [Babel](../compiler/Babel.md)

# Resource

- [Official Website](https://www.typescriptlang.org/)
- [Cheat Sheets](https://www.typescriptlang.org/cheatsheets)
- [Official Microsoft TypeScript Dev Blogs](https://devblogs.microsoft.com/typescript)
  - You can find the announcement of latest TS versions here, new features are listed
- [Stackoverflow: What is module option in tsconfig used for?](https://stackoverflow.com/questions/55471795/what-is-module-option-in-tsconfig-used-for/61215252#61215252)
- [TS: Code Generation for Modules](https://www.typescriptlang.org/docs/handbook/modules.html#code-generation-for-modules)
- [MDN: JavaScript Modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)
- [Dual CommonJS/ES module packages](https://nodejs.org/api/packages.html#dual-commonjses-module-packages)
