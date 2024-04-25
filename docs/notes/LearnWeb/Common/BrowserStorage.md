# Browser Storage

## Overview

- Cookies
- Local Storage
- Session Storage
- IndexedDB
- Cache

All data are stored in client browser.

|                    | Cookies            | Local Storage | Session Storage |
| ------------------ | ------------------ | ------------- | --------------- |
| Capacity           | 4kb                | 10mb          | 5mb             |
| Browsers           | HTML4/HTML5        | HTML5         | HTML5           |
| Accessible From    | Any Window         | Any Window    | Same Tab        |
| Expires            | Manually Set       | Never         | On Tab Close    |
| Storage Location   | Browser and Server | Browser Only  | Browser Only    |
| Sent with Requests | Yes                | No            | No              |

These data can be found in **Application** tab of Dev Tools of Chrome.

[Sotrage Inspector](https://developer.mozilla.org/en-US/docs/Tools/Storage_Inspector)

## Cookies

[MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)

**Cookie** is a larger topic, see [Cookies.md](./Cookies.md) for details.

Cookies are usually used to interact with server.

### Purposes

1. **Session Management**

   Anything the server should remember. Since HTTP is stateless, we need a way to keep track of state if required.

2. **Personalization**

   User preferences, themes, and other settings.

3. **Tracking**

   Recording and analyzing user behavior.

Cookies (of the same domain) are sent to server every time a request is made (not all cookies, but the ones that belong to current website), that's why it's small comparing to the other 2.

## Local Storage

[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)

Stored as key value pairs where both key and value are string.

```js
localStorage.setItem(key, value);
localStorage.getItem(key);
localStorage.removeItem(key);
localStorage.clear();
```

Data persist when a tab is closed or browser restarts (no expiration time).

Data in a `localStorage` object created in a "private browsing" or "incognito" session is cleared when the last "private" tab is closed.

Note: `localStorage` is accessible only to the same domain (excluding sub-domains). So developer won't need to worry about using duplicate `localStorage` key name as other websites.

## Session Storage

[MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/sessions)

Works exactly the same as Local Storage.

```js
sessionStorage.setItem(key, value);
sessionStorage.getItem(key);
sessionStorage.removeItem(key);
```

Data lost after tab is closed or browser closed.

A page session lasts as long as the browser is open, and survives over page reloads and restores.

> Data stored in `sessionStorage` **is specific to the protocol of the page**. In particular, data stored by a script on a site accessed with HTTP (e.g., [http://example.com](http://example.com/)) is put in a different `sessionStorage` object from the same site accessed with HTTPS (e.g., [https://example.com](https://example.com/)).

## IndexedDB

## Cache

## Reference

### Video

[JavaScript Cookies vs Local Storage vs Session](https://youtu.be/GihQAC1I39Q)

### Documentation

[Cookies MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)

[Local Storage MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)

[Session Storage MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/sessions)
