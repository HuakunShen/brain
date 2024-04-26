---
title: Oclif
---

https://oclif.io/

> The Open CLI Framework
> Create command line tools your users love

Oclif is for building console app, probably shouldn't be part of **LearnWeb**, but since it's using nodejs, I will include it in **LearnWeb**.

## features

https://oclif.io/docs/features

There are plenty of features, I will discuss some of the special features it has comparing to other packages.

- CLI Generator
  - Run a single command to scaffold out a fully functional CLI and get started quickly. See [Generator Commands](https://oclif.io/docs/generator_commands)
  - e.g. `oclif generate command login` to add login command
- Testing Helpers
  - Mockable stdout/stderr. Generator will automatically create [scaffolded tests](https://github.com/oclif/hello-world/blob/main/test/commands/hello/world.test.ts)
- Auto-documentation
  - `--help` automatically placed in README when npm package of CLI is published
- Plugins
  - Extend CLI with plugins
- Hooks
  - Lifecycle hooks, triggers on lifecycle events
- TypeScript
  - Run CLI with `ts-node`
- Auto-updating Installers
  - App can be packaged into
    - Standalone tarballs
    - Browser
    - Autoupdater
    - Windows Installer
    - MacOS Installer
    - Ubuntu/Debian Packages
    - Snapcraft
    - Autoupdate Channels
- Autocomplete
  - Autocompletion via [plugin-autocomplete](https://github.com/oclif/plugin-autocomplete)
