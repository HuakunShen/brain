---
title: Tauri Plugin System Design
authors: [huakun]
tags: [Tauri, Rust, Web, Plugin]
---

In [Raycast Analysis](https://huakun.tech/notes/Analysis/LaunchApp/raycast) and [uTools Analysis](https://huakun.tech/notes/Analysis/LaunchApp/uTools) I discussed the two successful app launchers and their plugin system designs. But both of them have big limitations. Raycast is mac-only. uTools is cross-platform (almost perfect), but it is built with Electron, thus large bundle size and memory consumption.

Tauri is a new framework that can build cross-platform desktop apps with Rust and Web. With much smaller bundle size and memory consumption. It’s a good choice for building a cross-platform app launcher.

- [Requirements](#requirements)
- [Solution](#solution)
  - [API](#api)
  - [How to give plugin full access to OS and FS?](#how-to-give-plugin-full-access-to-os-and-fs)
- [Implementation Design](#implementation-design)
  - [User Interface](#user-interface)
    - [Option 1](#option-1)
    - [Option 2](#option-2)
  - [Script Command](#script-command)
- [Reference](#reference)


## Requirements

- Plugins can be built with JS frontend framework, so it’s easier for develop to build
- UI can be controlled by plugin
- Sandbox preferred, never trust plugins not developed by official team, community plugin could be malicious. Neither of Raycast, Alfred, uTools used sandbox. So we can discuss this as well.

## Solution

Plugins will be developed as regular single page application. They will be saved in a directory like the following.

```
plugins/
├── plugin-a/
│   └── dist/
│       ├── index.html
│       └── ...
└── plugin-b/
    └── dist/
        ├── index.html
        └── ...
```

Optionally use symbolic link to build the following structure (link `dist` of each plugin to the plugin name. You will see why this could be helpful later.

```
plugins-link/
├── plugin-a/
│   ├── index.html
│   └── ...
└── plugin-b/
    ├── index.html
    └── ...
```

When a plugin is triggered, the main Tauri core process will start a new process running a http server serving the entire `plugins` or `plugins-link` folder as static asset. The http server can be actix-web.

Then open a new WebView process 

```jsx
const w = new WebviewWindow('plugin-a', {
	url: 'http://localhost:8000/plugin-a'
});
```

If we didn’t do the `dist` folder symlink step, the url would be `http://localhost:8000/plugin-a/dist` 

Do the linking could avoid some problem.

One problem is **base url**. A single page application like react and vue does routing with url, but the base url is `/` by default. i.e. index page is loaded on `http://localhost:8000`. If the plugin redirects to `/login`, it should redirect to `http://localhost:8000/login` instead of `http://localhost:8000/plugin-a/login`

In this case, [https://vite-plugin-ssr.com/base-url](https://vite-plugin-ssr.com/base-url), [https://vitejs.dev/guide/build#public-base-path](https://vitejs.dev/guide/build#public-base-path) can be configured in vite config. 

Another solution is to use proxy in the http server. Like `proxy_pass` in nginx config.

### API

Now the plugin’s page can be loaded in a WebView window. 

However, a plugin not only needs to display a UI, but also need to interact with system API to implement more features, such as interacting with file system. Now IPC is involved. 

Tauri by default won’t allow WebView loaded from other sources to run commands or call Tauri APIs.

See this security config `dangerousRemoteDomainIpcAccess`

[https://tauri.app/v1/api/config/#securityconfig.dangerousremotedomainipcaccess](https://tauri.app/v1/api/config/#securityconfig.dangerousremotedomainipcaccess)

```jsx
"security": {
	"csp": null,
	"dangerousRemoteDomainIpcAccess": [
		{
			"domain": "localhost:8000",
			"enableTauriAPI": true,
			"windows": ["plugin-a"],
			"plugins": []
		}
	]
},
```

`enableTauriAPI` determines whether the plugin will have access to the Tauri APIs. If you don’t want the plugin to have the same level of permission as the main app, then set it to false.

This not only work with [localhost](http://localhost) hosted plugins. The plugin can also be hosted on public web (but you won’t be able to access it if there is no internet). This will be very dangerous, as compromised plugin on public web will affect all users. In addition, it’s unstable. Local plugin is always safer.

There is another `plugins` attribute used to control which **tauri plugin**’s (The plugin here means plugin in rust for Tauri framework, not our plugin) command the plugin can call.

[https://tauri.app/v1/api/config/#remotedomainaccessscope.plugins](https://tauri.app/v1/api/config/#remotedomainaccessscope.plugins)

> `plugins` is The list of plugins that are allowed in this scope. The names should be without the `tauri-plugin-` prefix, for example `"store"` for `tauri-plugin-store`.
> 

For example, Raycast has a list of APIs exposed to extensions ([https://developers.raycast.com/api-reference/clipboard](https://developers.raycast.com/api-reference/clipboard))

Raycast uses NodeJS runtime to run plugins, so plugins can access file system and more. This is dangerous. From their blog [https://www.raycast.com/blog/how-raycast-api-extensions-work](https://www.raycast.com/blog/how-raycast-api-extensions-work), their solution is to open source all plugins and let the community verify the plugins.

This gives plugins more freedom and introduces more risks. In our approach with Tauri, we can provide a Tauri plugin for app plugins with all APIs to expose to the extensions. For example, get list of all applications, access storage, clipboard, shell, and more. File system access can also be checked and limited to some folders (could be set by users with a whitelist/blacklist). Just don’t give plugin access to Tauri’s FS API, but our provided, limited, and censored API plugin. 

### How to give plugin full access to OS and FS?

Unlike Raycast where the plugin is run directly with NodeJS, and render the UI by turning React into Swift AppKit native components. The Tauri approach has its UI part in browser. There is no way to let the UI plugin access OS API (like FS) directly. The advantage of this approach is that the UI can be any shape, while Raycast’s UI is limited by its pre-defined UI components. 

If a plugin needs to run some binary like ffmpeg to convert/compress files, the previous sandbox API method with a custom Tauri plugin won’t work. In this scenario, this will be more complicated. Here are some immature thoughts

- The non-UI part of the plugin will need a JS runtime if written in JS, like NodeJS or bun.js
- Include plugin script written in python, Lua, JS… and UI plugin runs them using a shell API command (like calling a CLI command)
- If the plugin need a long running backend, a process must be run separately, but how can the UI plugin communicate with the backend plugin? The backend plugin will probably need to be an http server or TCP server.
    - And how to stop this long running process?

## Implementation Design

### User Interface

Raycast supports multiple user interfaces, such as list, detail, form. 

To implement this in Jarvis, there are 2 options. 

1. The extension returns a json list, and Jarvis render it as a list view.
2. Let the extension handles everything, including list rendering.

#### Option 1

Could be difficult in our case, as we need to call a JS function to get data, this requires importing JS from Tauri WebView or run the JS script with a JS runtime and get a json response. 

To do this, we need a common API contract in JSON format on how to render the response. 

1. Write a command script `cmd1.js`
2. Jarvis will call `bun cmd1.js` with argv, get response
   
    Example of a list view
    
    ```json
    {
        "view": "list",
        "data": [
            {
                "title": "Title 1",
                "description": "Description 1"
            },
            {
                "title": "Title 2",
                "description": "Description 2"
            },
            {
                "title": "Title 3",
                "description": "Description 3"
            }
        ]
    }
    ```
    

This method requires shipping the app with a bun runtime (or download the runtime when app is first launched).

After some thinking, I believe this is similar to script command. Any other language can support this. One difference is, “script command” relies on users’ local dependency, custom libraries must be installed for special tasks, e.g. `pandas` in python. It’s fine for script command because users are coders who know what they are doing. In a plugin, we don’t expect users to know programming, and install libraries. So shipping a built JS `dist` with all dependencies is a better idea. e.g. `bun build index.ts --target=node > index.js`, then `bun index.js` to run it without installing `node_modules`.

[https://bun.sh/docs/bundler](https://bun.sh/docs/bundler)

In the plugin’s package.json, list all commands available and their entrypoints (e.g. `dist/cmd1.js`, `dist/cmd2.js`).

```json
{
    "commands": [
        {
            "name": "list-translators",
            "title": "List all translators",
            "description": "List all available translators",
            "mode": "cmd"
        }
    ]
}
```

#### Option 2

If we let the extension handle everything, it’s more difficult to develop, but less UI to worry about. 

e.g. `translate input1` , press enter, open extension window, and pass the `input1` to the WebView. 

By default, load `dist/index.html` as the plugin’s UI. There is only one entrypoint to the plugin UI, but a single plugin can have multiple sub-commands with url path. e.g. `http://localhost:8080/plugin-a/command1`

i.e. Routes in single page app

All available sub-commands can be specified in `package.json`

```json
{
    "commands": [
        {
            "name": "list-translators",
            "title": "List all translators",
            "description": "List all available translators",
            "mode": "cmd"
        },
        {
            "name": "google-translate",
            "title": "Google Translate",
            "description": "Translate a text to another language with Google",
            "mode": "view"
        },
        {
            "name": "bing-translate",
            "title": "Bing Translate",
            "description": "Translate a text to another language with Bing",
            "mode": "view"
        }
    ]
}
```

If `mode` is `view`, render it. For example, `bing-translate` will try to load `http://localhost:8080/translate-plugin/bing-translate`

If `mode` is `cmd`, it will try to run `bun dist/list-translators` and render the response.

`mode cmd` can have an optional language field, to allow using Python or other languages.

### Script Command

Script Command from Raycast is a simple way to implement a plugin. A script file is created, and can be run when triggered. The stdout is sent back to the main app process.

Supported languages by Raycast script command are 

- Bash
- Apple Script
- Swift
- Python
- Ruby
- Node.js

In fact, let users specify an interpreter, any script can be run, even executable binaries. 

Alfred has a similar feature in workflow. The difference is, Raycast saves the code in a separate file, and Alfred saves the code within the workflow/plugin (in fact also in a file in some hidden folder).

## Reference

- [How the Raycast API and extensions work - Raycast Blog](https://www.raycast.com/blog/how-raycast-api-extensions-work)
- [Raycast Analysis](https://huakun.tech/notes/Analysis/LaunchApp/raycast)
- [uTools Analysis](https://huakun.tech/notes/Analysis/LaunchApp/uTools) 



