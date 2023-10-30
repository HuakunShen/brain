---
title: Read PNG to base64
---

```rust
use std::fs::File;
use std::io::Read;
use base64::{Engine as _, engine::general_purpose};

fn main() {
    let mut file = File::open("x.png").unwrap();
    let mut buffer = vec![];
    file.read_to_end(&mut buffer).unwrap();
    let base64_str = general_purpose::STANDARD_NO_PAD.encode(buffer);
    println!("{}",base64_str);
}
```