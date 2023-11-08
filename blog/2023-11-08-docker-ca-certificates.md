---
title: Docker ca-certificates Dependency Required by Prisma
authors: huakun
tags: [docker]
---

When I tried to run prisma within a docker container, I got this error:

```
Error opening a TLS connection: error:1416F086:SSL routines:tls_process_server_certificate:certificate verify failed:../ssl/statem/statem_clnt.c:1919: (unable to get local issuer certificate)
```

The docker image I used was `oven/bun`, but I believe this error can happen to any docker image that doesn't install `ca-certificates`. 

The solution is simple, add the following to the `Dockerfile`

```Dockerfile
RUN apt update && apt install -y ca-certificates
```

## What is ca-certificates

https://packages.debian.org/sid/ca-certificates

Contains the certificate authorities shipped with Mozilla's browser to allow SSL-based applications to check for the authenticity of SSL connections.

Browsers like chrome or firefox have built-in trusted certificate authorities, which means they can communicate to verify the authenticity of SSL connections. When your prisma connect requires SSL connection, then you have to install `ca-certificates` to allow SSL-based applications to check for the authenticity of SSL connections.


