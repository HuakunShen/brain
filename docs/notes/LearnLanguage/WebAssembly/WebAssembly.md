---
title: WebAssembly
---

## Readings

- [Embedding Python in Rust with WebAssembly](https://wasmlabs.dev/articles/python-wasm-rust/)
- [Wasmer](https://wasmer.io/)
- [RustPython (Wasmer)](https://wasmer.io/rustpython/rustpython)
  - Embedding RustPython into your Rust Applications
  - Online demo (Python interpreter runs in browser): https://rustpython.github.io/demo/
- [wasmtime runtime](https://github.com/bytecodealliance/wasmtime): a standalone runtime for WebAssembly
  - Read the [docs](https://docs.wasmtime.dev/)
  - It can be used to run `.wasm` file in CLI.
  - It provides language support for multiple languages (C, C++, Python, .NET, Go, Ruby) so that wasm module can run within these languages
  - [wasmtime crate](https://crates.io/crates/wasmtime)
    - Rust embedding API for the Wasmtime project: a cross-platform engine for running WebAssembly programs.
    - Run wasm modules from Rust program
  - [WASI Tutorial](https://github.com/bytecodealliance/wasmtime/blob/main/docs/WASI-tutorial.md)
- [wasmer crate](https://crates.io/crates/wasmer)
- [WebAssembly Official Website](https://webassembly.org/)
  - [List of things you can do, such as comple wasm from Rust](https://webassembly.org/getting-started/developers-guide/)
- [Wasmer takes WebAssembly libraries mainstream with WAI](https://wasmer.io/posts/wasmer-takes-webassembly-libraries-manistream-with-wai)
  - Build library to wasm and use it in any langauge


## Practice

- [Frontend Library (`alert()`) Tutorial](https://rustwasm.github.io/book/game-of-life/hello-world.html)
- [Cargo wasi command](https://github.com/bytecodealliance/cargo-wasi)