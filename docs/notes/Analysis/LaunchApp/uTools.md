# uTools

https://www.u.tools/

Dev Docs: https://www.u.tools/docs/developer/welcome.html

- [uTools](#utools)
  - [Questions](#questions)
  - [Manifest](#manifest)
  - [Dev](#dev)
  - [preload.js](#preloadjs)
  - [Use Third Party Packages](#use-third-party-packages)
  - [uTools API](#utools-api)
    - [uTools DB API](#utools-db-api)
    - [uTools Browser API](#utools-browser-api)
    - [uTools Server API](#utools-server-api)
  - [注意事项](#注意事项)
  - [App Storage](#app-storage)

## Questions

1. How does uTools render UI?
2. How does uTools allow plugins to access system API?

## Manifest

```json title="plugin.json"
{
  "main": "index.html",
  "logo": "logo.png",
  "features": [
    {
      "code": "hello",
      "explain": "hello world",
      "cmds": ["hello", "你好"]
    }
  ]
}
```

- `main` is the entry point.
- `features` is a list of features
  - `features.code` id code to distinguish features
  - `features.cmds`: command list to trigger the feature (中文会自动支持 拼音及拼音首字母，无须重复添加)
- `"platform": ["win32", "darwin", "linux"]` optional

## Dev

The dev tools provided by uTools can load plugin for testing and bundle into `.ups` file which can be installed and shared. Like Alfred's workflow file.

Example: https://github.com/uTools-Labs/utools-tutorials/tree/main/utools-helloworld-example

Doc: https://www.u.tools/docs/developer/debug.html

Set `main` to a local url for development to achieve hot reload.

```json
{
  "development": {
    "main": "http://127.0.0.1:8080/index.html"
  }
}
```

## preload.js

https://www.u.tools/docs/developer/preload.html

> 当你在 `plugin.json` 中配置了 `preload` 属性，将载入对应的预加载脚本。
>
> 在传统的 web 开发中，所有的 javascript 脚本都在浏览器沙盒中运行，权限被严格限制，所能实现的功能非常有限。
>
> 通过 `preload.js` 能够帮你突破沙盒限制，进入一个崭新的 JavaScript 世界。

`preload.js` is used to preload script and bypass sandbox limitation.

`preload.js` can access `nodejs`, `electron`, `uTools` API. APIs can be plugged into `window` object so that other JS code can access these APIs.

```js
// 开发者可以暴露自定义 API 供后加载脚本使用

// preload.js 中使用 nodejs
const { readFileSync } = require("fs");

window.readConfig = function () {
  const data = readFileSync("./config.json");
  return data;
};

// index.html 后加载的内容可以使用 window.readConfig() 方法，但不能使用 Node.js 特性
console.log(window.readConfig()); // 正常执行
console.log(readFileSync("./config.json")); // 报错
```

```js
function readFileAsync(filePath, encoding) {
  return new Promise((resolve, reject) => {
    require("fs").readFile(filePath, encoding, (error, data) => {
      if (error) {
        reject(error);
      } else {
        resolve(data);
      }
    });
  });
}

window.services = {
  readFile: (inputPath, encoding = "utf8") => {
    return readFileAsync(inputPath, encoding);
  },
};
```

`window.services.readFile` get's access to read files beyond the constraint by sandbox.

## Use Third Party Packages

> 通过源码方式使用第三方库
>
> Through source code

Download the library into `/public`

## uTools API

This is a wrapper for some common functions.

在插件应用初始化完成时，uTools 会自动在你的 window 对象上挂载 utools 对象。

```js
// 复制单个文件
utools.copyFile("/path/to/file");
// 复制多个文件
utools.copyFile(["/path/to/file1", "/path/to/file2"]);
// 路径
utools.copyImage("/path/to/img.png");
// base64
utools.copyImage("data:image/png;base64,xxxxxxxxx");
```

### uTools DB API

Data persistance.

```js
// 创建
utools.db.put({
  _id: "demo",
  data: "demo",
});
// 返回 {id: "demo", ok: true, rev: "1-05c9b92e6f24287dc1f4ec79d9a34fa8"}

// 更新
utools.db.put({
  _id: "demo",
  data: "demo",
  _rev: "1-05c9b92e6f24287dc1f4ec79d9a34fa8",
});

// 异步方式更新
utools.db.promises.put({
  _id: "demo",
  data: "demo",
  _rev: "1-05c9b92e6f24287dc1f4ec79d9a34fa8",
});

utools.db.get("demo");
// 返回 {_id: "demo", _rev: "3-9836c5c68af5aef618e17d615882942a", data: "demo"}

utools.db.remove("demo");
// 返回 {id: "demo", ok: true, rev: "2-effe5dbc23dffc180d8411b23f3108fb"}
```

### uTools Browser API

> uTools browser 简称 ubrowser，是根据 uTools 的特性，量身打造的一个可编程浏览器。利用 ubrowser 可以轻而易举连接一切互联网服务，且与 uTools 完美结合。

ubrowser 拥有优雅的链式调用接口，可以用口语化的数行代码，实现一系列匪夷所思的操作。例如：

1. RPA 自动化脚本

2. 网页魔改

3. 网页抓取

```js
// 打开"必应" 并搜索 "uTools"
utools.ubrowser
  .goto("https://cn.bing.com")
  .value("#sb_form_q", "uTools")
  .click("#sb_form_go")
  .run({ width: 1000, height: 600 });
```

This is interesting. This should be very simple. The browser window is loaded in a electron window, the API is just a wrapper around DOM APIs.

There is also `setCookies(cookies)` and `removeCookies(name)` API.

`evaluate(func, ...params)` allows developers to eval JS function.

```js
.evaluate((param1, param2) => {
  return document.querySelector('div').innerText
}, 'param1', 'param2')
```

### uTools Server API

> 通过 uTools 的服务端 API，可以将你的应用和 uTools 用户关联，实现帐号互通、接收支付通知、查询用户支付记录等，为保护密钥安全，请仅在服务端调用接口。

APIs for account and payment. Regular API wrapper for web requests, skip.

## 注意事项

1. uTools 插件应用中不受跨域影响，可以访问任意网址。
2. 无需网页考虑兼容性问题，基于（Chromium 91 和 Node 14）
3. 在插件应用开发模式中，可以使用 http 协议加载远程资源（ js、css ）。当打包成 uTools 插件应用后，所有的静态资源都应该在包内，否则会加载失败。
4. 在打包目录中，请勿包含 `.git` `.js.map` `.css.map` 文件。

## App Storage

On Mac, the app data is stored in `/Users/<user>/Library/Application Support/uTools`.

Clipboard data stored in `clipboard-data/1715136702505/data`. The number is the timestamp.

In the `data` file, there is encoded (and potentially encrypted clipboard data).

Here is the tree structure with 2 layers of folders.

```
.
├── Cache
│   └── Cache_Data
├── Code Cache
│   ├── js
│   └── wasm
├── Cookies
├── Cookies-journal
├── Local Storage
│   └── leveldb
├── Network Persistent State
├── Partitions
│   └── %3Cutools%3E
├── Preferences
├── SingletonCookie -> 11472625255256702255
├── SingletonLock -> f4d488789185-8643
├── SingletonSocket -> /var/folders/f7/7c6q0gh121vdyh86bv192wpc0000gn/T/scoped_dirCsNUE2/SingletonSocket
├── blob_storage
│   └── 37646b27-ee51-41e8-a51d-91b911b09c42
├── clipboard-data
│   └── 1715136702505
├── database
│   └── default
├── plugins
│   ├── 170c1ee16af97ded0bdde9e7eb60294b.asar
│   ├── 5522e367c63f3d5490807c01b442211d.asar
│   ├── 668b903f4bcdf240dd228aab904f3892.asar
│   ├── 6ee51b94a1ffd0d90edfc1f3c2460f06.asar
│   ├── 6ee51b94a1ffd0d90edfc1f3c2460f06.asar.unpacked
│   ├── 878f2055a6213f3e8f4c38a8109e077c.asar
│   ├── 878f2055a6213f3e8f4c38a8109e077c.asar.unpacked
│   ├── 9325e4f7566857c5e4633eb2b1b564fc.asar
│   ├── b5a1343f92233a09aa4499f1a3389a12.asar
│   ├── b5a1343f92233a09aa4499f1a3389a12.asar.unpacked
│   ├── d030e1e61e13bf54f1b393938e80242c.asar
│   ├── e332887c9a7b922489ee3dba816901b1.asar
│   └── installs
└── settings
```

WASM is used, node addons are used. The app is built on Electron.

