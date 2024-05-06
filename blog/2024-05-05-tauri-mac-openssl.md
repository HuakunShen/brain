---
title: Tauri Universal Build for Mac (Solve SSL Problem)
authors: huakun
tags: [tauri]
---

I had problem building a universal Tauri app for Mac (M1 pro).

```bash
rustup target add x86_64-apple-darwin
rustup target add aarch64-apple-darwin

npm run tauri build -- --target universal-apple-darwin
```

The problem was with OpenSSL. The error message was:

```
    Finished `release` profile [optimized] target(s) in 4.50s
   Compiling openssl-sys v0.9.102
   Compiling cssparser v0.27.2
   Compiling walkdir v2.5.0
   Compiling alloc-stdlib v0.2.2
   Compiling markup5ever v0.11.0
   Compiling uuid v1.8.0
   Compiling fxhash v0.2.1
   Compiling crossbeam-epoch v0.9.18
   Compiling selectors v0.22.0
   Compiling html5ever v0.26.0
   Compiling indexmap v1.9.3
   Compiling tracing-core v0.1.32
error: failed to run custom build command for `openssl-sys v0.9.102`

Caused by:
  process didn't exit successfully: `/Users/hacker/Dev/projects/devclean/devclean-ui/src-tauri/target/release/build/openssl-sys-2efafcc1e9e30675/build-script-main` (exit status: 101)
  --- stdout
  cargo:rerun-if-env-changed=X86_64_APPLE_DARWIN_OPENSSL_LIB_DIR
  X86_64_APPLE_DARWIN_OPENSSL_LIB_DIR unset
  cargo:rerun-if-env-changed=OPENSSL_LIB_DIR
  OPENSSL_LIB_DIR unset
  cargo:rerun-if-env-changed=X86_64_APPLE_DARWIN_OPENSSL_INCLUDE_DIR
  X86_64_APPLE_DARWIN_OPENSSL_INCLUDE_DIR unset
  cargo:rerun-if-env-changed=OPENSSL_INCLUDE_DIR
  OPENSSL_INCLUDE_DIR unset
  cargo:rerun-if-env-changed=X86_64_APPLE_DARWIN_OPENSSL_DIR
  X86_64_APPLE_DARWIN_OPENSSL_DIR unset
  cargo:rerun-if-env-changed=OPENSSL_DIR
  OPENSSL_DIR unset
  cargo:rerun-if-env-changed=OPENSSL_NO_PKG_CONFIG
  cargo:rerun-if-env-changed=PKG_CONFIG_ALLOW_CROSS_x86_64-apple-darwin
  cargo:rerun-if-env-changed=PKG_CONFIG_ALLOW_CROSS_x86_64_apple_darwin
  cargo:rerun-if-env-changed=TARGET_PKG_CONFIG_ALLOW_CROSS
  cargo:rerun-if-env-changed=PKG_CONFIG_ALLOW_CROSS
  cargo:rerun-if-env-changed=PKG_CONFIG_x86_64-apple-darwin
  cargo:rerun-if-env-changed=PKG_CONFIG_x86_64_apple_darwin
  cargo:rerun-if-env-changed=TARGET_PKG_CONFIG
  cargo:rerun-if-env-changed=PKG_CONFIG
  cargo:rerun-if-env-changed=PKG_CONFIG_SYSROOT_DIR_x86_64-apple-darwin
  cargo:rerun-if-env-changed=PKG_CONFIG_SYSROOT_DIR_x86_64_apple_darwin
  cargo:rerun-if-env-changed=TARGET_PKG_CONFIG_SYSROOT_DIR
  cargo:rerun-if-env-changed=PKG_CONFIG_SYSROOT_DIR
  run pkg_config fail: pkg-config has not been configured to support cross-compilation.

  Install a sysroot for the target platform and configure it via
  PKG_CONFIG_SYSROOT_DIR and PKG_CONFIG_PATH, or install a
  cross-compiling wrapper for pkg-config and set it via
  PKG_CONFIG environment variable.

  --- stderr
  thread 'main' panicked at /Users/hacker/.cargo/registry/src/index.crates.io-6f17d22bba15001f/openssl-sys-0.9.102/build/find_normal.rs:190:5:


  Could not find directory of OpenSSL installation, and this `-sys` crate cannot
  proceed without this knowledge. If OpenSSL is installed and this crate had
  trouble finding it,  you can set the `OPENSSL_DIR` environment variable for the
  compilation process.

  Make sure you also have the development packages of openssl installed.
  For example, `libssl-dev` on Ubuntu or `openssl-devel` on Fedora.

  If you're in a situation where you think the directory *should* be found
  automatically, please open a bug at https://github.com/sfackler/rust-openssl
  and include information about your system as well as this message.

  $HOST = aarch64-apple-darwin
  $TARGET = x86_64-apple-darwin
  openssl-sys = 0.9.102


  note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
warning: build failed, waiting for other jobs to finish...
       Error failed to build x86_64-apple-darwin binary: failed to build app
```

## Solution

Install OpenSSL with `brew`

```bash
brew install openssl
export export OPENSSL_DIR=$(brew --prefix openssl) 
```
