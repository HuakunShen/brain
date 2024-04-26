---
title: Run WASM Module as Executable
---

## wasmtime

Doc: https://github.com/bytecodealliance/wasmtime

```rust
// hello.rs
fn main() {
    println!("Hello, world!");
}
```

```bash
rustup target add wasm32-wasi
rustc hello.rs --target wasm32-wasi
wasmtime hello.wasm
> Hello, world!
```

## Wasmer

[YouTube: WebAssembly On The Server??? Why?](https://youtu.be/OHmycSgFAUs)

## WASI

WASI provides some system APIs such as file system.

Tut: https://github.com/bytecodealliance/wasmtime/blob/main/docs/WASI-tutorial.md

```bash
rustup target add wasm32-wasi
cargo build --target wasm32-wasi    # build main.rs into wasm32-wasi
```

```bash
# run the program
echo "hello world!" > a.txt # construct a example file
wasmtime --dir=. target/wasm32-wasi/debug/wasm-tut.wasm a.txt b.txt  # run the wasm module, give cwd permission with --dir=.
wasmer --dir=. target/wasm32-wasi/debug/wasm-tut.wasm a.txt b.txt # wasmer can also be used to run the module
```
