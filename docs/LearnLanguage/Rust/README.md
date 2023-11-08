# Rust

## Arc

https://doc.rust-lang.org/rust-by-example/std/arc.html

Arc (Atommically Reference Counted) is used when you want to share ownership between multiple threads. 


```rust
use std::time::Duration;
use std::sync::Arc;
use std::thread;

fn main() {
    // This variable declaration is where its value is specified.
    let apple = Arc::new("the same apple");

    for _ in 0..10 {
        // Here there is no value specification as it is a pointer to a
        // reference in the memory heap.
        let apple = Arc::clone(&apple);

        thread::spawn(move || {
            // As Arc was used, threads can be spawned using the value allocated
            // in the Arc variable pointer's location.
            println!("{:?}", apple);
        });
    }

    // Make sure all Arc instances are printed from spawned threads.
    thread::sleep(Duration::from_secs(1));
}
```

## Box

Box is used when you want to allocate a value on the heap rather than the stack. 


