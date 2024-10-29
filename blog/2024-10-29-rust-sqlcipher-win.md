---
title: Rust Sqlite Cipher (Windows)
---

To use sqlite with encryption enabled, [rusqlite](https://crates.io/crates/rusqlite) is a popular option. Just enable `bundled-sqlcipher` feature.

It's super simple on Mac and Linux, on Windows, I have to configure OpenSSL library, it's a bit harder than Linux/Mac.

First download openssl from https://slproweb.com/products/Win32OpenSSL.html

OpenSSL is a very important library used everywhere. This website looks a bit old and I don't know if I can trust it. Why don't Microsoft include it in Windows or provide an official way to install it?

Download the latest, larger file, not the light installer.

The file I downloaded was `Win64OpenSSL-3_4_0.msi`, install it.

Before installing, here is the error

```
note: To improve backtraces for build dependencies, set the CARGO_PROFILE_DEV_BUILD_OVERRIDE_DEBUG=true environment variable to enable debug information generation.

Caused by:
  process didn't exit successfully: `C:\Users\shenh\Desktop\sqlcipher\target\debug\build\libsqlite3-sys-458bb895065b5297\build-script-build` (exit code: 101)
  --- stdout
  cargo:rerun-if-env-changed=LIBSQLITE3_SYS_USE_PKG_CONFIG
  cargo:include=C:\Users\shenh\.cargo\registry\src\index.crates.io-6f17d22bba15001f\libsqlite3-sys-0.30.1/sqlcipher
  cargo:rerun-if-changed=sqlcipher/sqlite3.c
  cargo:rerun-if-changed=sqlite3/wasm32-wasi-vfs.c

  --- stderr
  thread 'main' panicked at C:\Users\shenh\.cargo\registry\src\index.crates.io-6f17d22bba15001f\libsqlite3-sys-0.30.1\build.rs:164:29:
  Missing environment variable OPENSSL_DIR or OPENSSL_DIR is not set
```

`OPENSSL_DIR` is missing.

My install path is `C:\Program Files\OpenSSL-Win64`.

Set `OPENSSL_DIR` to `C:\Program Files\OpenSSL-Win64`.

Then remove `target` and build again. This time I get new errors

```
error: linking with `link.exe` failed: exit code: 1181
...
= note: LINK : fatal error LNK1181: cannot open input file 'libcrypto.lib'
```

`libcrypto.lib` is not found.

For my installation, I found the file under `C:\Program Files\OpenSSL-Win64\lib\VC\x64\MDd`

I need to add environment variable `OPENSSL_LIB_DIR` to `C:\Program Files\OpenSSL-Win64\lib\VC\x64\MDd`

Then it works. DB is encrypted. VSCode has sqlite viewer extension. Try open the encrypted db file, it won't open as it's encrypted.

From instructions online, I initially set `OPENSSL_LIB_DIR` to `C:\Program Files\OpenSSL-Win64\lib`, it doesn't work.

You may also want to set `OPENSSL_INCLUDE_DIR` to `C:\Program Files\OpenSSL-Win64\include\`

Also, you have to restart code editor everytime PATH is changed.

As a Mac user and Linux fan, Windows is too hard for developers. Even deleting files could be a big problem as it's used by some process. 
I rarely had these problems on Mac and Linux.

Also configuring environment variables on Mac and Linux is simply editing files. 
