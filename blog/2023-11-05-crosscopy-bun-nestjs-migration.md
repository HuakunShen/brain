---
title: CrossCopy Migration to Bun and Nestjs
authors: Huakun Shen
tags: [bun, nestjs, migration]
---

My project CrossCopy has been using the following tech stack
- npm for package management
- nodejs for JS runtime
- Server: expressjs + nodejs
- Web: Svelte + nodejs
- Monorepo: nx monorepo + turborepo + npm workspaces
- JS Module: CJS
- API: GraphQL
- Sync: GraphQL subscription

Recently I spend a few days migrating from this stack to the following stack
- pnpm + bun for package management
- bun for JS runtime
- Server: Nestjs + bun
- Web: Svelte + bun
- Monorepo: turborepo + (pnpm workspaces + bun workspaces)
  - bun and pnpm workspaces are pretty much the same
- JS Module: ESM
- API: GraphQL
- Sync: SocketIO
  - Bun currently doesn't work with Apollo GraphQL's subscription. https://github.com/oven-sh/bun/issues/6905

> This makes the project much easier to develop and maintain. This is a blog I copied from our dev docs and may be useful for people who are interested in using bun for their projects.

There are huge breaking changes in this migration to improve development experience and performance.

This blog is must read, there are many places to be aware of, otherwise you may not be able to run the project.

Here are the PRs in our two main monorepo repositories for server and clients:

- https://github.com/CrossCopy/crosscopy-clients/pull/16
- https://github.com/CrossCopy/crosscopy-dev/pull/98

Many changes was maade in the `@crosscopy/core` and `@crosscopy/graphql-schema` repo but they don't have a separate PR for simplicity. Check the associated commits in the 2 PRs above if you really want.

After tons of research and experiment, I decided to make this huge refactoring and toolchain migration.

- Migrate nodejs runtime to bun runtime (https://bun.sh/)
  - Bun is much mcuh faster than nodejs
  - For now I removed the [subpath exports](https://nodejs.org/api/packages.html#subpath-exports) in package.json for `@crosscopy/core` and `@crosscopy/graphql` which requires building TypeScript into JavaScript first, and then import them in another project. This is complicated during development, especially the 2 libraries are only used by ourselves. Bun allows us to import TypeScript directly using relative paths, we no longer need to build them. Before, after making any changes in `@crosscopy/core`, I have to manually compile it again before I can see the changes in server who imports it. Now, I can see the changes immediately. Dev servers with `bun --watch` will pick up the changes from it's dependencies automatically although it's in another package, there is no need to restart server, without feeling another separate package.
  - Bun runs TypeScript directly, no need to build TypeScript into JavaScript first, which is much faster.
  - Environment Variables
    - With nodejs and ts-node, we have to use a `dotenv` package to programmatically load environment variables from `.env` file.
    - Bun has a built-in support for `.env` file, we no longer need to use `dotenv` package. See https://bun.sh/guides/runtime/set-env and https://bun.sh/guides/runtime/read-env
    - When running and command with bun, `bun run <script>` or `bunx vitest`, bun will automatically load `.env` file in the current directory, making testing and development easier. This is why the `test` script in `package.json` for many packages are changed to things like `bunx vitest` or `bun run test`. Sometimes `npm run test` won't work because it doesn't load `.env` file.
- Migrate package manager to `pnpm`
  - `bun` is not only a runtime, but also a package manager. It's the fastest I've ever seen. Faster than `npm`, `yarn` and `pnpm`. During migration to `bun` runtime I always use bun to install packages and do package management. I changed my plan when I started migrating clients CICD to use bun, as bun currently only works on MacOS and Linux, not Windows. Our future Windows client will have to be built on Windows in CICD, and our development environment should support Windows although I personally use MacOS and Linux all the time.
  - Using `npm` to do package management is no longer possible because [bun workspaces](https://bun.sh/docs/install/workspaces) uses slightly different syntax from [npm workspaces](https://docs.npmjs.com/cli/v7/using-npm/workspaces).
    - Using packages from the same monorepo as dependency requires adding the package name to `package.json`. npm workspaces uses `"@crosscopy/core": "*"` syntax, while bun workspaces uses `"@crosscopy/core": "workspace:*"`. The extra `workspace:` prefix is required and prevent npm workspaces to work with bun workspaces. i.e. npm package management and bun runtime simply won't work together in the same mono project.
  - `pnpm` comes to resecure. pnpm ranks first in 2022 stateofjs for monorepo tools (https://2022.stateofjs.com/en-US/libraries/monorepo-tools/). Turbo repo is second and we are using them together for our monorepo management. [pnpm workspaces](https://pnpm.io/workspaces) uses the same syntax as bun workspaces with a `workspace:*` prefix for within-monorepo dependencies. Making it possible to use `pnpm` for package management and `bun` for runtime in the same monorepo. Perfect! Problem solved.
- Migration to ESM from CJS.
  - CommonJS was a legacy module system of the JavaScript ecosystem. We used to use CJS for compatibility with most packages. Some packages migrate to only ESM recently, causing problems. ESM has more features and is easier to use, for example top-level await is only in ESM.
  - We now migrate every package to ESM except for the new server written with Nest.js, I will talk more about it.
- Migrate express to nestjs (https://nestjs.com/)
  - We used to use Express.js as our backend server framework. It's popular and undoubtedly the most popular framework in JS. However, it's not designed for large projects. It's hard to maintain and scale. Nest.js is a framework designed for large projects. It's based on Express.js, but it's much more powerful. It's also written in TypeScript, which is a big plus.
  - Express.js is a barebone framework, with no template, developers have to design and write everything from scratch. This is great, but bad initial design could lead to unmaintainable code in the future.
    - Our previous version server worked fine, but after the project get's bigger and a few refactor, I realized that the initial design was not good enough for this project as it grows bigger and bigger.
  - Nest.js has a lot of built-in features and templates. It organizes everything in the OOP way just like Spring Boot, many many files, but easier to read and maintain. With lots of built-in features that work out of the box, like Auth with JWT, rate limit throttler, GraphQL, Websocket with SocketIO, middleware and interceptor and much more. I don't need to set up everything from scratch, connecting components manually and making the code ugly and hard to maintain.
    - The testing framework is more mature, and it's easier to write tests. Everything is separated into modules, and it's easier to mock dependencies.
  - Problem with Nest.js.
    - I rewrite the server in Nest.js, fantastic experience and I can expect a better development and testing experience with it. However, a limitation of Nestjs is that it's completely in CommonJS, not possible to migrate to ESM. Our dependency packages (core and graphql-schema) has been migrated to the newer ESM standard, and to work with nest, they have to be compiled to CJS JavaScript first before they can be imported into Nest.js server, which gives up the freedom of importing TypeScript freely from any location.
    - Another problem with **Nest.js + bun** is that GraphQL subscription doesn't work with bun.
      - This is not a problem with Nest.js actually, but a problem with bun + Apollo server. bun's developer has worked so hard to make bun seamlessly integrate as a drop-in replacement for nodejs runtime by implementing most of the nodejs APIs. Most of the time I can use bun as a drop-in replacement for nodejs runtime. Bun works with nest.js websocket, but not with Apollo Server subscription. I don't know the reason either, but probably due to some missing APIs, there is no error shown. After hours of debugging, I found that bun simply won't work with Apollo Server, even without Nest.js. So it's not a Nest.js problem, but a problem between bun and Apollo Server.
      - Luckily, GraphQL Query and Mutation still work with bun runtime as they are simply HTTP requests under the hood. And since we have already decided to use SocketIO for realtime synchronization as it's more flexible and powerful than GraphQL subscription (SocketIO is two-way while subscription is only one-way), we don't need to use GraphQL subscription anymore. So this is not a problem for us. Later if Bun supports apollo server, we can use subscription again for some other simpler use cases that doesn't require two-way communication.
- Migrate `crosscopy-dev` repo from using nx monorepo to turborepo. I simply had more bugs and issues with nx repo. `crosscopy-clients` repo uses turborepo and has a better experience, so I decided to migrate `crosscopy-dev` repo to turborepo as well. turborepo also ranks higher than nx in 2022 stateofjs for monorepo tools (https://2022.stateofjs.com/en-US/libraries/monorepo-tools/), with 10% more retention rate, 14% more interest.

## Note

- Install bun and pnpm. bun work similar to nodejs, pnpm works similar to npm.
- In most packages, `bun dev` is used to start development server, `bun run test` is used to run tests, `bun run build` is used to build TypeScript into JavaScript. `bun run` is used to run any script in `package.json`.
- `pnpm run build` and `pnpm run test` in the root of a mono repo will use turborepo to build all packages in the monorepo. I've configured everything to work. If you need to run tests in subpackages, try to use `bun run test` or `bunx vitest` or `bunx jest` as I didn't write code to load `.env` file, using a bun command does that for us even if the test still uses nodejs under the hood. As long as bun is used as the initial command, `.env.` is loaded.
- If you are unsure about the command to use, look at `.github/workflows` to see what commands CI uses to build the repo. If CI works, then so should your local environment work if configured correctly.