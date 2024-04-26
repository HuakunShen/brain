# JavaScript

> JavaScript, often abbreviated JS, is a programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS. As of 2022, 98% of websites use JavaScript on the client side for web page behavior, often incorporating third-party libraries.

https://en.wikipedia.org/wiki/JavaScript

If HTML is noun, CSS is adjective, then JS is verb. It makes web pages iteractive.

Since TypeScript is kind of a wrapper or superset of JavaScript, many advnaced JS topics were coverered in [TypeScript Notes](./TypeScript/TypeScript.md).

TypeScript is also the current industry standard. So make sure to also learn TypeScript.

# Recommendation

Always use TypeScript for a serious project.

A TypeScript project is far more easier to develop and maintain than a JavaScript project.

It may be painful when you first start to learn TS, but once you are familiar with it, it will save you a ton of time and efforts.

# ESM vs CJS

A beginner will be confused by ESM and CJS. It's normal. Some features implemented in Nodejs are not implemented in TypeScript. 

ESM is the new standard and what I would prefer to use, but CJS is the old standard which many old packages use. Bundlers can build a ESM and a CJS version of the same code.

If you were to build a package, CJS would be the first to support, but it's always good to support ESM.

I found that some popular packages like `clipboardy` and `inquirer` no longer supports CommonJS in their latest version. You may have to use an older version when your package is in CJS.

This is where confusion comes in, when you install a new package, everything breaks. Error messages may be unclear or confusing especially if you don't know the story behind it.

Read the article below to learn more about the differences between ESM and CJS, and how to deal with them.

It's possible to mix them.

- [Node Modules at War: Why CommonJS and ES Modules Can’t Get Along](https://redfin.engineering/node-modules-at-war-why-commonjs-and-es-modules-cant-get-along-9617135eeca1)
  - This is a very good article about the problem of CommonJS and ES Modules.
  - Understanding this will solve most of your confusion about CJS and ESM
  - The part that's practical is the section that explains how CJS can import ESM modules and how ESM can import CJS modules.
  - ESM import CJS: no named import
    - ```js
      import _ from "lodash"; // will work
      import { reverse } from "lodash"; // won't work
      ```
  - CJS import ESM: dynamic import
    - ```js
      (async () => {
        const { foo } = await import("./foo.mjs");
      })();
      ```

# Workspace

Follow this example, https://docs.npmjs.com/cli/v9/using-npm/workspaces?v=true, it's very simple. 