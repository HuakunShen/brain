---
title: Clap Struct-Style Arg Parsing
---

This is an example to support struct-style and subcommand arg parsing.

```rust
use clap::{Parser, Subcommand};

#[derive(Parser)]
#[command(author, version, about, long_about = None)]
struct Cli {
    #[command(subcommand)]
    command: Commands,
}

#[derive(Subcommand)]
enum Commands {
    Add {
        name: Option<String>,

        #[command(subcommand)]
        command: Commands2,
    },
}

#[derive(Debug, Parser)]
struct WriteArgs {
    /// The path to write to
    path: String,
    // a list of other write args
}

#[derive(Subcommand)]
enum Commands2 {
    Minus { name: Option<String> },
    Write(WriteArgs),
}

fn main() {
    let cli = Cli::parse();
}
```