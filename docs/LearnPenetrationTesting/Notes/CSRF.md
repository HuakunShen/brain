# CSRF

[MDN](https://developer.mozilla.org/en-US/docs/Glossary/CSRF)

> **CSRF** (Cross-Site Request Forgery) is an attack that impersonates a trusted user and sends a website unwanted commands. This can be done, for example, by including malicious parameters in a [URL](https://developer.mozilla.org/en-US/docs/Glossary/URL) behind a link that purports to go somewhere else

```html
<img src="https://www.example.com/index.php?action=delete&id=123" />
```

For users who have modification permissions on `https://www.example.com`, the `<img>` element executes action on `https://www.example.com` without their noticing, even if the element is not at `https://www.example.com`.

There are many ways to prevent CSRF, such as implementing [RESTful API](https://developer.mozilla.org/en-US/docs/Glossary/REST), adding secure tokens, etc.