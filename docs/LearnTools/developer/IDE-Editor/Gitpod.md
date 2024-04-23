---
title: Gitpod
---

## Usage

- Prefix GitHub repo URL with `gitpod.io/#`
		- Sample: [https://gitpod.io/#https://github.com/HuakunShen/wol-web](https://gitpod.io/#https://github.com/HuakunShen/wol-web)
- There is a free option, see [Plans and Pricing](https://www.gitpod.io/pricing)
- Support [**Self-Hosted**](https://www.gitpod.io/docs/self-hosted/latest)
- Full access to terminal
- Support connecting to Gitpod with local IDE and editors such as VSCode with [Gitpod extension](https://www.gitpod.io/docs/ides-and-editors/vscode-extensions), and many JetBrains IDEs. See [IDEs & Editors](https://www.gitpod.io/docs/ides-and-editors#title)
	- Use gitpod's computing resource
	- Connect to gitpod's workspace via SSH
- Open preview browser within browser, See [Preview](https://www.gitpod.io/docs/command-line-interface#preview)
	- side by side with the code
	- or in a new browser tab/window
- Environment
	- Most languages are preinstalled, such as python, go, java, see [Custom Docker Image](https://www.gitpod.io/docs/config-docker#custom-docker-image)
	- Use `.gitpod.yml` to configure automation, Gitpod can run custom commands automatically or build environment on startup
	- You can customize your development environment with a `Dockerfile`, see [Configure a custom Dockerfile](https://www.gitpod.io/docs/config-docker#configure-a-custom-dockerfile)
	- Prebuild environment for every commit, see [An intro to prebuilds](https://www.gitpod.io/docs/getting-started#an-intro-to-prebuilds)


## Gitpod Badge to open GitHub repo in GitPod
Use `[![Gitpod ready-to-code](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/HuakunShen/LearnAlgorithm)` in Markdown file.

Or replace the badge image url either of the following.
- https://gitpod.io/button/open-in-gitpod.svg
- https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod

The resulting batch will look like [![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/HuakunShen/LearnTools) or [![Gitpod ready-to-code](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/HuakunShen/LearnTools).




