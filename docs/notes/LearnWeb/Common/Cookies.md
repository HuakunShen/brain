# Cookies

[MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)

> An HTTP cookie (web cookie, browser cookie) is a small piece of data that a server sends to the user's web browser. The browser may store it and send it back with later requests to the same server. Typically, it's used to tell if two requests came from the same browser — keeping a user logged-in, for example. It remembers stateful information for the [stateless](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview#HTTP_is_stateless_but_not_sessionless) HTTP protocol.

### Purposes

1. **Session Management**

   Anything the server should remember. Since HTTP is stateless, we need a way to keep track of state if required.

2. **Personalization**

   User preferences, themes, and other settings.

3. **Tracking**

   Recording and analyzing user behavior.

Cookies (of the same domain) are sent to server every time a request is made, that's why it's small comparing to the other 2.

### Set Cookies

The [`Set-Cookie`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie) HTTP response header sends cookies from the server to the user agent.

```js
Set-Cookie: <cookie-name>=<cookie-value>

// example
HTTP/2.0 200 OK
Content-Type: text/html
Set-Cookie: yummy_cookie=choco
Set-Cookie: tasty_cookie=strawberry

[page content]
```

Then, with every subsequent request to the server, the browser sends back all previously stored cookies to the server using the [`Cookie`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cookie) header.

```js
GET /sample_page.html HTTP/2.0
Host: www.example.org
Cookie: yummy_cookie=choco; tasty_cookie=strawberry
```

`cookies` can be set by `document.cookie=...` with JavaScript, when new cookies are added, the old ones are not overriden.

```javascript
document.cookie = "name=xxx; expires=" + new Date(2020, 0, 1).toUTCString(); // expires on 2020/1/1
document.cookie = "name=yyy; expires=" + new Date(9999, 0, 1).toUTCString(); // never expires with a large date
```

To view cookies, we can only see all cookies and parse the string manually (use a packge to do this).

```javascript
document.cookie; // viewing current website's cookie (not all)
```

### Lifetime of a cookie

> The lifetime of a cookie can be defined in two ways:
>
> - _Session_ cookies are deleted when the current session ends. The browser defines when the "current session" ends, and some browsers use _session restoring_ when restarting, which can cause session cookies to last indefinitely long.
> - _Permanent_ cookies are deleted at a date specified by the `Expires` attribute, or after a period of time specified by the `Max-Age` attribute.

```js
// Example
Set-Cookie: id=a3fWa; Expires=Wed, 31 Oct 2021 07:28:00 GMT;
// Note: When an Expires date is set, the time and date set is relative to the client the cookie is being set on, not the server.
```

### Restrict access to cookies

#### Secure Attribute

> A cookie with the `Secure` attribute is sent to the server only with an encrypted request over the HTTPS protocol, never with unsecured HTTP, and therefore can't easily be accessed by a [man-in-the-middle](https://developer.mozilla.org/en-US/docs/Glossary/MitM) attacker.
>
> It can still be read from client's hard disk.

#### HttpOnly Attribute

> A cookie with the `HttpOnly` attribute is inaccessible to the JavaScript [`Document.cookie`](https://developer.mozilla.org/en-US/docs/Web/API/Document/cookie) API; it is sent only to the server. For example, cookies that persist server-side sessions don't need to be available to JavaScript, and should have the `HttpOnly` attribute.
>
> This precaution helps mitigate cross-site scripting ([XSS](<https://developer.mozilla.org/en-US/docs/Web/Security/Types_of_attacks#Cross-site_scripting_(XSS)>)) attacks.

```js
// Example
Set-Cookie: id=a3fWa; Expires=Wed, 21 Oct 2021 07:28:00 GMT; Secure; HttpOnly
```

### Define where cookies are sent

#### Domain attribute

> The `Domain` attribute specifies which hosts are allowed to receive the cookie. If unspecified, it defaults to the same [origin](https://developer.mozilla.org/en-US/docs/Glossary/origin) that set the cookie, _excluding subdomains_. If `Domain` _is_ specified, then subdomains are always included. Therefore, specifying `Domain` is less restrictive than omitting it. However, it can be helpful when subdomains need to share information about a user.

#### Path attribute

> The `Path` attribute indicates a URL path that must exist in the requested URL in order to send the `Cookie` header.

#### SameSite attribute

> The `SameSite` attribute lets servers require that a cookie shouldn't be sent with cross-origin requests (where [Site](https://developer.mozilla.org/en-US/docs/Glossary/Site) is defined by the registrable domain), which provides some protection against cross-site request forgery attacks ([CSRF](https://developer.mozilla.org/en-US/docs/Glossary/CSRF)).

##### Possible Values:

- **Strict:** cookie is sent only to the same site as the one that originated it (website that sends the request is the same as the one that receives it)

- **Lax:** similar, with an exception for when the user navigates to a URL from an external site, such as by following a link.

  With **Strict**, when a client navigate to your website from the URL of an external site, the Cookie wouldn't be sent.

- **None:** no restrictions on cross-site requests

`Lax` is a good choice for cookies affecting the display of the site, Strict` being useful for cookies related to actions your user is taking.

**Default:** `SameSite=Lax`

`None` must be used with `Secure` attribute when cookie is to be sent cross-origin.

```
Set-Cookie: mykey=myvalue; SameSite=Strict
```
