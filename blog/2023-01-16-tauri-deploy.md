---
title: Tauri Deployment (Auto Update and CICD)
authors: [huakun]
tags: [Tauri, Rust, Web, TypeScript, CICD, GitHub Action, Deployment]
---

## Docs

[Tauri Updater](https://tauri.app/zh-cn/v1/guides/distribution/updater/)

[Bundler Artifacts](https://tauri.app/v1/guides/distribution/updater/#bundler-artifacts) has sample CI and config script.

[Cross-Platform Compilation](https://tauri.app/v1/guides/building/cross-platform) has a sample GitHub Action CI script for cross-platform compilation (Windows, MacOS and Linux). Compiled files are stored as artifacts in a draft GitHub release. The release assets will be read by updater server for auto-update.

[Sample tauri.config.json](https://github.com/tauri-apps/tauri/blob/5b6c7bb6ee3661f5a42917ce04a89d94f905c949/examples/updater/src-tauri/tauri.conf.json#L52)

## Building

For [updater](https://tauri.app/zh-cn/v1/guides/distribution/updater/) to work, a public key is required. 

```json title="tauri.config.json"
"updater": {
    "active": true,
    "endpoints": [
        "https://releases.myapp.com/{{target}}/{{current_version}}"
    ],
    "dialog": true,
    "pubkey": "YOUR_UPDATER_SIGNATURE_PUBKEY_HERE"
}
```

A pair of keys can be generated with `tauri signer generate -w ~/.tauri/ezup.key`.

If update is configured, then private key and password environment variables must be set.

The following script can automatically load the private key as environment variable. Assuming password is an empty string. 

```bash
#!/usr/bin/env bash
PRIVATE_KEY_PATH="$HOME/.tauri/ezup.key";
if test -f "$PRIVATE_KEY_PATH"; then
    export TAURI_PRIVATE_KEY=$(cat ~/.tauri/ezup.key); # if the private key is stored on disk
    export TAURI_KEY_PASSWORD="";
else
    echo "Warning: Private Key File Not Found";
fi
```

## CICD (GitHub Action)

In GitHub Action, environment variables can be set like this in the top level of yml file.

```yml
env:
  TAURI_PRIVATE_KEY: ${{ secrets.TAURI_PRIVATE_KEY }}
  TAURI_KEY_PASSWORD: ${{ secrets.TAURI_KEY_PASSWORD }}
```
I encountered a error during compilation on Ubuntu platform. 

Error: `thread '<unnamed>' panicked at 'Can't detect any appindicator library', src/build.rs:326:17`

I found a solution in [this issue](https://github.com/tauri-apps/tauri/issues/5175).

Install `libayatana-appindicator3-1-dev` with apt for ubuntu.

## Updater Server

[vercel/hazel](https://github.com/vercel/hazel) is a updater server for electron, also compatible with tauri, can be deployed in a few clicks on vercel.

