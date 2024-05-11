---
title: Rubick
---

Rubick is an open source clone of uTools.

Here is the documentation for extension development:
https://rubickcenter.github.io/docs/dev/

- [Plugin Types](#plugin-types)
  - [ui (UI 插件)](#ui-ui-插件)
  - [system (系统插件)](#system-系统插件)
- [Publish Plugin](#publish-plugin)
- [Extension API](#extension-api)
  - [事件 Events](#事件-events)
  - [Window](#window)
  - [System](#system)
  - [Local Database](#local-database)
- [Source Code Implementation Details](#source-code-implementation-details)

## Plugin Types

### ui (UI 插件)

A `"main": "index.html",` is provided in `package.json` to specify the entry point of the plugin.

### system (系统插件)

`"entry": "index.js",` is provided in `package.json` to specify the entry point of the plugin.

Sample `index.js` for a system plugin:

```js
module.exports = () => {
  return {
    onReady(ctx) {
      const { Notification } = ctx;
      new Notification({
        title: "测试系统插件",
        body: "这是一个系统插件，在rubick运行时，立即被加载",
      }).show();
    },
  };
};
```

## Publish Plugin

Send a PR to https://gitcode.net/rubickcenter/rubick-database/-/blob/master/plugins/total-plugins.json

## Extension API

https://rubickcenter.github.io/docs/dev/api.html

### 事件 Events

- `onPluginReady(callback)` and `onPluginEnter(callback)`

  - Callback returns an object with plugin environment information

    - `code`: feature code in `package.json`
    - `type`: `feature.cmd.type` in `package.json`, could be `text`, `img`, `files`, `regex`, `over`, `window`
    - `payload: String | Object | Array`: `feature.cmd.type` 对应匹配的数据
    - ```js
      rubick.onPluginReady(({ code, type, payload }) => {
        console.log("插件装配完成，已准备好");
      });
      /* 
        type 为 "files" 时， payload 值示例
        [
            {
                "isFile": true,
                "isDirectory": false,
                "name": "demo.js",
                "path": "C:\\demo.js"
            }
        ]
      
        type 为 "img" 时， payload 值示例
        data:image/png;base64,...
      
        type 为 "text"、"regex"、 "over" 时， payload 值为进入插件时的主输入框文本
        */
      ```

- `onPluginOut(callback)`
  - Callback called with plugin goes to background

### Window

- `hideMainWindow()`
- `showMainWindow()`
- `setExpendHeight(height)`
- `setSubInput(onChange, placeholder)`
  - Subscribe to search bar input changes with `onChange` callback
- `setSubInputValue(value)`
  - 直接对子输入框的值进行设置

### System

- `showNotification(body)`
  - Show system notification
- `shellOpenPath(fullPath)`
  - Open file
- `shellOpenExternal(url)`
  - open url in browser
- `getPath(name)`
  - Electron API https://www.electronjs.org/docs/latest/api/app#appgetpathname
  - Used to get path of some system folders such as `home`, `appData`, `userData`, `temp`

### Local Database

Rubick's db is based on [https://github.com/pouchdb/pouchdb](pouchdb)

Read more examples in the [doc](https://rubickcenter.github.io/docs/dev/api#%E6%9C%AC%E5%9C%B0%E6%95%B0%E6%8D%AE%E5%BA%93)

It's basically a key-value store.

```js
rubick.db.put({
  _id: "demo",
  data: "demo"
})
// 更新请求
rubick.db.put({
  _id: "demo",
  data: "demo",
  _rev: "1-05c9b92e6f24287dc1f4ec79d9a34fa8"
})
rubick.db.get("demo")
rubick.db.remove("demo")
```


## Source Code Implementation Details

https://rubickcenter.github.io/docs/core/

