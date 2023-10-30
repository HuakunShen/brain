# Json Web Token

## Sturcture

A token contains 3 parts
1. Header
2. Payload
3. Verify Signature

### Parse Payload

To parse the payload without verifying with a library, just split and take the second part. The payload is in base64, just decode it. 

Here is an nodejs example

```js
const token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c";
const payloadBase64Str = token.split(".")[1];
const tokenBuf = Buffer.from(payloadBase64Str, 'base64');
const payloadUTF8 = tokenBuf.toString();
const tokenObject = JSON.parse(payloadUTF8);
```

The payload of a JWT can contain serveral non-mandatory fields such as `iat` and `exp`.

Here are 2 of the properties that's most likely existent.

- `iat` means **issued at**
- `exp` means **expiration time**

Both of them are integers in seconds from Jan 1, 1970 00:00am.

In JavaScript, to convert the 2 values to `Date`

```js
new Date(exp * 1000);
```

Check if expired in JavaScript

```ts
const expired = (exp: number) => Date.now() > exp * 1000;
```




## Revoke JWT Token

### Related Readings

- [How to Revoke JSON Web Tokens (JWTs)](https://devops.com/how-to-revoke-json-web-tokens-jwts)

## Reference

- [Json Web Token OpenId](https://openid.net/specs/draft-jones-json-web-token-07.html)
