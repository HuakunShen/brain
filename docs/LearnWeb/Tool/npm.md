---
title: npm
---

## Publish Package

Modify the version in `package.json`.

Use [npm version](https://docs.npmjs.com/cli/v9/commands/npm-version) to update package version.

```bash
npm version minor
npm publish
```

## Unpublish

[npm-unpublish](https://docs.npmjs.com/cli/v9/commands/npm-unpublish)

If you published a version and realized a problem with it, then you can unpublish it with the following command.

```bash
npm unpublish <package name>@<version>
npm unpublish crosscopy@0.0.14
```