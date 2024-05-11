---
title: JWKS
---

# JSON Web Key Sets

[jwks](https://auth0.com/docs/secure/tokens/json-web-tokens/json-web-key-sets)

The JSON Web Key Set (JWKS) is a set of keys containing the public keys used to verify any JSON Web Token (JWT) issued by the Authorization Server and signed using the RS256 signing algorithm.

For example, if you use a auth service like Auth0 to allow users to log in with multiple identity providers, the service will sign the JWT with a private key. The public key is used to verify the JWT. The public key is available in the JWKS. Servers can use the JWKS to verify the JWT to ensure the token is valid.