---
title: Raycast Analysis
tags: [react, macos, software design]
---

In this article I will discuss the design of raycast, a popular macOS utility that allows users to run scripts and commands with a few keystrokes. I will anlayze the software design of raycast.

- [Blog: How the Raycast API and Extensions work](#blog-how-the-raycast-api-and-extensions-work)
  - [Goals](#goals)
  - [Tech](#tech)
    - [First Attempt: TypeScript + JSC](#first-attempt-typescript--jsc)
      - [UI Rendering](#ui-rendering)
    - [Second Attempt](#second-attempt)
      - [Goal](#goal)
      - [Concerns](#concerns)
    - [Sandboxing Runtime](#sandboxing-runtime)
      - [Option 1: Sandbox at Process Level](#option-1-sandbox-at-process-level)
      - [Option 2: Sandbox at JavaScript Engine Level](#option-2-sandbox-at-javascript-engine-level)
    - [Open Source Extensions](#open-source-extensions)
      - [Benefits](#benefits)
    - [Process for Extensions](#process-for-extensions)
    - [IPC](#ipc)
    - [Order and Speed](#order-and-speed)
    - [Reconciling and Creating the Render Tree](#reconciling-and-creating-the-render-tree)
      - [Solution](#solution)
  - [Developer Experience](#developer-experience)
    - [CLI](#cli)
    - [Versioning](#versioning)
      - [API Evolution](#api-evolution)
      - [Dev Cycle](#dev-cycle)
  - [Publish Package](#publish-package)
- [Analysis and Discussion](#analysis-and-discussion)
  - [API](#api)
  - [Compare with Alfred and uTools](#compare-with-alfred-and-utools)


## Blog: How the Raycast API and Extensions work

[Blog: How the Raycast API and extensions work](https://www.raycast.com/blog/how-raycast-api-extensions-work)

### Goals

1. Let developers have the freedom to customize Raycast and create shareable extensions that other users could install
2. "Avoid a second-class mini-app that shows in some frame in Raycast". Avoid webview.
   1. This is because Raycast is a fully native macOS app and wish to render a native user interface. So users don't feel like using an extension, but a single app.
   2. This is opposed to the design of uTools which uses webview to show extensions and every extension have completely different UI.

### Tech

#### First Attempt: TypeScript + JSC

VSCode is a successful example.

JSC: JavaScript Core

Run each extension with an instance of a JSC process and communicate with main Raycast process with XPC (apple's IPC)

##### UI Rendering

Defined components using JSON with a tree structure, then translate the tree to native view models using AppKit. Worked.

Developers feedback:

- Couldn't use npm packages in extensions
- UI and state management not easy

#### Second Attempt

Exposed API to developers in JS/TS, but developers were limited in which libraries they could use.

Need to run React on Node.js and make it interact with Raycast.

##### Goal

1. Use JS/TS
2. not spending too much time polyfilling OS-level APIs
3. Enable easy access to entire JS ecosystem (rpm)

##### Concerns

1. How to get Node runtime to users?
2. How to make sure extensions are not running evil code when they have full access to Node's APIs?

Chose to use external runtime but "manage" it through Raycast.

1. Auto-download and install the right Node runtime, without user noticing it before the first extension gets opened. Do integrity checking on the binary.
2. Benefit: the node process acn crash without crashing Raycast.

#### Sandboxing Runtime

Sandboxing the runtime is one option to limit what extension can do. 

They rejected this, since not satisfying.

##### Option 1: Sandbox at Process Level

Run one node process per extension. -> Expensive.

Apple’s sandboxing tools like sandbox-exec, that ship with macOS, aren’t supported for third-party development. Need to write our own tool to act as a security proxy for the Node process. 

##### Option 2: Sandbox at JavaScript Engine Level

Run all JS code through an additional virtual layer. Will degrade performance. 

#### Open Source Extensions

VSCode maintains a "kill list" of flagged extensions, who will be auto uninstalled for users.

Raycast chose to make all extensions open source and reviewed. 

##### Benefits

- High UX quality
- Sharing Solutions
- Complete transparency

#### Process for Extensions

Use one process for Raycast and one for all extensions.

Node supports "worker threads" in V12. V8 isolates the worker threads. This can be used to isolate each extension. 

Set up memory limits for extensions's heap. 

If a worker crashes or run out of memory, an error will be shown. 

#### IPC

> How do Node workers communicate with Raycast main process?

Use streams on standard file descriptors (in Swift via DispatchIO framework) to enable 2-way communication. 

JSON-RPC protocol is used because

- simple and lightweight
- fast enough
- easy to debug (since it's plain text)

Extensions only send registered messages ("render", "setClipboard", etc.) to Raycast. Arbitrary calling to Raycast code isn't possible. 

A temporary session id is generated for an extension when loaded, used to identify extensions in Raycast and this allows running multiple extensions in parallel.

#### Order and Speed

> How to make sure IPC message has right ordering and avoid concurrency issues? Node is single-threaded.

Serial queues and buffered streams are used (in Swift) to make sure messages arrive and leave in order. 

#### Reconciling and Creating the Render Tree

Extensions are written with React (which is a web framework). State management can be done with React hooks, and re-rendering can be triggered to update Raycast native UI. This is achieved with a customizable part of React called "reconciler". https://legacy.reactjs.org/docs/reconciliation.html

React uses virtual DOM to control the real DOM. In Raycast the browser DOM is replaced by AppKit. 

##### Solution

- Create a JSON representation for each component
- Composing in the reconciler to "render tree"
- After getting a complete description of the UI, compare to previous render using a standard called **JSON Patch**. 
  - If there is no patches -> no changes
- Compress the data if necessary and send to native rendering
- Construct lightweight Swift view models and translate patches to native UI

### Developer Experience

#### CLI

A CLI (ray CLI) is provided. Used to develop and build the API. Developers use it to create extensions, debug and see changes in Raycast.

The CLI is a Go app compiled both for Darwin and Linux (to run CI with GitHub actions). 

No server running in Raycast to detect changes from source files during development (files may change and need to be hot reloaded). Communication done over app schemes (I believe this [doc](https://developer.apple.com/documentation/xcode/defining-a-custom-url-scheme-for-your-app) is what app scheme means. Calling a url `raycast://reload`) and a ood old pid file. The CLI basically talks to Raycast via URLs and Raycast talks to the CLI (for example, to stop a development session) via the process ID file that the CLI creates.

#### Versioning

Dependency verison mismatch is a big problem. App could fail if node, raycast, API, extensions versions aren't compatible. 

In extensions store, only publish one latest version. Developers don't need to specify a version.

Raycast auto-update Raycast and extensions, only install extension when it's compatible with that Raycast version depending on the API version used. Raycast app version >= API version. 

Raycast, API and CLI version numbers are synchronized (same).

##### API Evolution

Backwards-compatible as much as possible. 

New features can be added but not removed. 

##### Dev Cycle

1. Learn from feedback
2. Create internal API ecolution proposal, sketch the API and discuss
3. Implement, review, dogfood it internally, release it

If some API need to be deprecated, try to create auto migration through code mods. Update docs with each release. 

### Publish Package

Developers send PR to https://github.com/raycast/extensions.git, an open source monorepo.

Automated checks run to do manifest checking, listing. Review, test and give feedback.

Once published, send auto notifications to slack. 



## Analysis and Discussion

The installed extensions are installed at `~/.config/raycast/extensions`.

Extensions source code can be downloaded from https://github.com/raycast/extensions.git

API Documentation: https://developers.raycast.com/

Raycast app itself is closed sourced, so I can only guess what they are doing.



Building an extension is simple. Raycast can auto generate a template starter code. It's basically a regular react app. However, rather than displaying in browser, `ray` cli takes over and display extensions in Raycast.

```json
  "scripts": {
    "build": "ray build -e dist",
    "dev": "ray develop",
    "fix-lint": "ray lint --fix",
    "lint": "ray lint",
    "publish": "npx @raycast/api@latest publish"
  }
```

As mentioned above, Raycast gives extensions full access to the OS. For example you can access the file system. But my `@crosscopy/clipboard` package doesn't work. Node bindings doesn't seem to work. 

https://developers.raycast.com/information/security states that encrypted local storage is provided. Only the plugin can access the stuff in it.

The Node.js runtime is stored in `/Users/User/Library/Application Support/com.raycast.macos/NodeJS/runtime` ~90MB.

I also found these sqlite files.

- `raycast-activities-enc.sqlite`

- `raycast-activities-enc.sqlite-shm`

- `raycast-activities-enc.sqlite-wal`

There are a few more files like this. `shm` should mean shared memory. `wal` may mean write ahead log.

These files are all encrypted. 

There is a folder called `posthog.queueFolder` containing some queued message to send to posthog.

Here is a sample message

```json
{
    "event": "Quick Action Performed",
    "properties": {
        "$locale": "en",
        "$app_version": "1.72.1",
        "$network_cellular": false,
        "$device_name": "User’s MacBook Pro",
        "$screen_width": 3440,
        "category": "apiExtension",
        "$app_namespace": "com.raycast.macos",
        "$network_wifi": true,
        "$device_manufacturer": "Apple",
        "$device_type": "Desktop",
        "$device_model": "arm64",
        "$os_name": "macOS Version 14.5 (Build 23F5074a)",
        "$app_name": "Raycast",
        "$timezone": "America\/Toronto",
        "$os_version": "14.5.0",
        "quickActionId": "_local\/qrcode-reader\/read-qrcode-from-screenshot_quickAction",
        "$lib": "posthog-ios",
        "packageName": "_local\/qrcode-reader",
        "isViaShortcut": "false",
        "$app_build": "0",
        "$screen_height": 1415,
        "$lib_version": "3.1.4"
    },
    "timestamp": "2024-05-08T01:45:05.838Z",
    "uuid": "68015C2C-0975-4AD3-A041-FB56CF2BBF16",
    "distinct_id": "BBBE9F5F-1BBB-4559-9F2A-C09E0A77DDF4"
}
```

### API

Although full OS access is granted with NodeJS runtime, Raycast provides some convenient APIs.

For example a `runAppleScript` API to control other apps. 

```ts
import { runAppleScript } from "run-applescript";

export default async function Command() {
  await runAppleScript('tell application "Spotify" to playpause');
}
```

The extension's react code isn't separated from the code that can access native APIs, which is very cool. This is like server side rendering. e.g. PHP, Flask template. Compute the data, plug them into a template and display in native app.


### Compare with Alfred and uTools

Alfred has something called workflows. Similar to Raycast extensions. 

Alfred has a GUI for creating workflows using blocks and connections. While Raycast uses React.

Each workflow block has some function. You can also run native scripts like AppleScript, shell script, etc.

These two apps are similar in how they display results. Both render extension output in a native window rather than something like a webview.

This is cleaner. This requires the extension to return UI specification in a specific format that the app understand how to render. 

uTools is different. It uses a webview to display extensions. This is more flexible. You can use any web technology to build the extension. The UI can be however you like. But this is also a downside. The UI can be inconsistent.

All three apps exposed full OS access to extensions.





























