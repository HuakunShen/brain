# Rust Concurrency

- [Rust Concurrency](#rust-concurrency)
  - [Example 1: Multi-Threading Counter](#example-1-multi-threading-counter)
    - [Naive Approach](#naive-approach)
    - [Arc + Mutex Approach](#arc--mutex-approach)
  - [Example 2: Fire and Forget Thread](#example-2-fire-and-forget-thread)
    - [A Tokio Example](#a-tokio-example)
    - [Fire and Forget Thread in a Struct](#fire-and-forget-thread-in-a-struct)
    - [Optional: Wait for Thread to Finish with thread](#optional-wait-for-thread-to-finish-with-thread)
    - [Optional: Wait for Thread to Finish with tokio async await](#optional-wait-for-thread-to-finish-with-tokio-async-await)
  - [Example 3: Loop](#example-3-loop)
    - [Provide `stop` method in System (tokio)](#provide-stop-method-in-system-tokio)
    - [The Thread Way to Stop (with a flag)](#the-thread-way-to-stop-with-a-flag)
  - [Example 4: Clipboard Watcher](#example-4-clipboard-watcher)

## Example 1: Multi-Threading Counter

### Naive Approach

Here is a multi-threading counter. count will be 0, because count is not shared between threads. The "move" keyword moves the ownership of count to the thread.

```rust
fn main() {
    let mut count = 0;
    let mut handles = vec![];
    for _ in 0..10 {
        let handle = std::thread::spawn(move || {
            for _ in 0..1000 {
                count += 1;
            }
        });
        handles.push(handle);
    }
    for handle in handles {
        handle.join().unwrap();
    }
    println!("count = {}", count);
}
```

### Arc + Mutex Approach

```rust
use std::sync::{Arc, Mutex};

fn main() {
    let count = Arc::new(Mutex::new(0));
    let mut handles = vec![];
    for _ in 0..10 {
        let count_clone = Arc::clone(&count);
        let handle = std::thread::spawn(move || {
            for _ in 0..1000 {
                let mut cnt = count_clone.lock().unwrap();
                *cnt += 1;
            }
        });
        handles.push(handle);
    }
    for handle in handles {
        handle.join().unwrap();
    }
    println!("count = {}", count.lock().unwrap());
}
```

## Example 2: Fire and Forget Thread

In JavaScript, promise can be fired and forgotten. In Rust, we can use thread::spawn to create a fire and forget thread.

```rust
// fire and forget thread
use std::{
    sync::{Arc, Mutex},
    thread,
    time::Duration,
};

fn increment(count: &Arc<Mutex<i32>>) {
    let count_clone = Arc::clone(count);

    thread::spawn(move || {
        thread::sleep(Duration::from_secs(2));
        let mut c = count_clone.lock().unwrap();
        *c += 1;
    });
}

fn main() {
    let count = Arc::new(Mutex::new(0));
    increment(&count);
    assert!(*count.lock().unwrap() == 0); // at this point the thread is still running in the background
    println!("Count: {}", *count.lock().unwrap());
    thread::sleep(Duration::from_secs(3));
    assert!(*count.lock().unwrap() == 1); // after 3 seconds the thread has finished
    println!("Count: {}", *count.lock().unwrap());
}
```

### A Tokio Example

```rust
#[tokio::main]
async fn main() {
    // Spawn a background task
    tokio::spawn(async {
        // Simulate some work in the background
        println!("Background task started");
        sleep(Duration::from_secs(2)).await;
        println!("Background task completed");
    });

    // Continue with the rest of your application
    println!("Main task continues");

    // For this example, we'll sleep the main task to ensure the background task has time to complete.
    // In a real application, you would likely have more async work being done or an event loop running.
    sleep(Duration::from_secs(3)).await;

    println!("Main task completed");
}
```

### Fire and Forget Thread in a Struct

```rust
// fire and forget thread
use std::{
    sync::{Arc, Mutex},
    thread,
    time::Duration,
};
use tokio::time::sleep;

struct System {
    apps: Arc<Mutex<Vec<String>>>,
}

impl System {
    fn new() -> Self {
        System {
            apps: Arc::new(Mutex::new(vec![])),
        }
    }

    fn refresh(&mut self) {
        let apps_clone = Arc::clone(&self.apps);
        thread::spawn(move || {
            thread::sleep(Duration::from_secs(2)); // intentionally slow down refresh for 2 seconds
            let mut apps = apps_clone.lock().unwrap();
            apps.push("app1".to_string());
        });
        // or use tokio
        // tokio::spawn(async move {
        //     sleep(Duration::from_secs(2)).await; // intentionally slow down refresh for 2 seconds
        //     let mut apps = apps_clone.lock().unwrap();
        //     apps.push("app1".to_string());
        // });
    }

    fn get_apps(&self) -> Vec<String> {
        self.apps.lock().unwrap().clone()
    }
}

fn main() {
    let mut system = System::new();
    system.refresh();
    assert!(system.get_apps().is_empty());
    println!("apps: {:?}", system.get_apps());
    thread::sleep(Duration::from_secs(3));
    assert_eq!(system.get_apps(), vec!["app1"]);
    println!("apps: {:?}", system.get_apps());
}
```

### Optional: Wait for Thread to Finish with thread

You may want to wait for the thread to finish in the main thread (while keeping the option to fire and forget), use the returned JoinHandle.

```rust
fn refresh(&mut self) -> std::thread::JoinHandle<()> {
    let apps_clone = Arc::clone(&self.apps);
    return thread::spawn(move || {
        thread::sleep(Duration::from_secs(2)); // intentionally slow down refresh for 2 seconds
        let mut apps = apps_clone.lock().unwrap();
        apps.push("app1".to_string());
    });
}

// in main thread
let handle = system.refresh();
handle.join().unwrap();
```

### Optional: Wait for Thread to Finish with tokio async await

```rust
fn refresh(&mut self) -> tokio::task::JoinHandle<()> {
    let apps_clone = Arc::clone(&self.apps);
    tokio::spawn(async move {
        sleep(Duration::from_secs(2)).await; // intentionally slow down refresh for 2 seconds
        let mut apps = apps_clone.lock().unwrap();
        apps.push("app1".to_string());
    })
}
```

Then in main thread you can choose to use or not use `.await`.

```rust
system.refresh();       // fire and forget
system.refresh().await; // wait for refresh to finish

let handle = system.refresh();
handle.await.unwrap();  // save the handle for later use, like .join() in thread
```

## Example 3: Loop

Now I want to run a loop in a separate thread to refresh the system every second.

```rust
fn refresh_in_background(&mut self) {
    let apps_clone = Arc::clone(&self.apps);
    tokio::spawn(async move {
        loop {
            sleep(Duration::from_secs(1)).await; // intentionally slow down refresh for 2 seconds
            let mut apps = apps_clone.lock().unwrap();
            println!("refreshing apps: {:?}", apps.clone());
            apps.push("app1".to_string());
        }
    });
}

// main thread
#[tokio::main]
async fn main() {
    let mut system = System::new();
    system.refresh_in_background();
    thread::sleep(Duration::from_secs(5));
}

// output
// refreshing apps: []
// refreshing apps: ["app1"]
// refreshing apps: ["app1", "app1"]
// refreshing apps: ["app1", "app1", "app1"]
```

What if I want to be able to stop the loop when I want to?

```rust
fn refresh_in_background(&mut self) -> tokio::task::JoinHandle<()> {
    let apps_clone = Arc::clone(&self.apps);
    tokio::spawn(async move {
        loop {
            sleep(Duration::from_secs(1)).await; // intentionally slow down refresh for 2 seconds
            let mut apps = apps_clone.lock().unwrap();
            println!("refreshing apps: {:?}", apps.clone());
            apps.push("app1".to_string());
        }
    })
}

// main thread

#[tokio::main]
async fn main() {
    let mut system = System::new();
    let handle = system.refresh_in_background();
    thread::sleep(Duration::from_secs(5));

    handle.abort(); // stop the refresh task
    println!("refresh aborted");
    thread::sleep(Duration::from_secs(7));
}
```

tokio's `JoinHandle` provides a method `abort` to stop the task at any time.

### Provide `stop` method in System (tokio)

Rather than calling `handle.abort()` in main thread, we can provide a `stop` method in `System` to stop the refresh task.

We can have an extra private field `refresh_handle` in `System` to store the `JoinHandle`.

This can also be used to check if the refresh task is already running. If None, then start the task, otherwise, print a message and return.

```rust

struct System {
    apps: Arc<Mutex<Vec<String>>>,
    refresh_handle: Option<tokio::task::JoinHandle<()>>,
}

impl System {
    fn new() -> Self {
        System {
            apps: Arc::new(Mutex::new(vec![])),
            refresh_handle: None,
        }
    }

    /// periodically refresh apps in the background
    fn refresh_in_background(&mut self) {
        let apps_clone = Arc::clone(&self.apps);
        if self.refresh_handle.is_some() {
            println!("refresh task already running");
            return;
        }
        self.refresh_handle = Some(tokio::spawn(async move {
            loop {
                tokio::time::sleep(Duration::from_millis(500)).await; // intentionally slow down refresh for 2 seconds
                let mut apps = apps_clone.lock().unwrap();
                println!("refreshing apps: {:?}", apps.clone());
                apps.push("app1".to_string());
            }
        }));
    }

    fn stop_refresh(&mut self) {
        if let Some(handle) = self.refresh_handle.take() {
            handle.abort();
        }
    }
}

#[tokio::main]
async fn main() {
    let mut system = System::new();
    system.refresh_in_background();
    thread::sleep(Duration::from_secs(3));
    system.refresh_in_background();
    system.stop_refresh();
    println!("refresh stopped");
}

// output
// refreshing apps: []
// refreshing apps: ["app1"]
// refreshing apps: ["app1", "app1"]
// refreshing apps: ["app1", "app1", "app1"]
// refreshing apps: ["app1", "app1", "app1", "app1"]
// refresh task already running
// refresh stopped
```

### The Thread Way to Stop (with a flag)

Unfortunately, thread does not have an `abort` method. We can use a `bool` flag to stop the loop.

`AtomicBool (std::sync::atomic::AtomicBool)`: Atomic types provide atomic operations without needing a lock. They allow safe concurrent access to shared data without the need for explicit locking. AtomicBool specifically provides atomic boolean operations like load, store, compare-and-swap (CAS), etc. It's useful for simple cases where you need to share a boolean flag among threads and want to perform atomic operations on it without the overhead of locking.

```rust

struct System {
    apps: Arc<Mutex<Vec<String>>>,
    running: Arc<AtomicBool>,
}

impl System {
    fn new() -> Self {
        System {
            apps: Arc::new(Mutex::new(vec![])),
            running: Arc::new(AtomicBool::new(false)), // Mutex could also be used
        }
    }

    /// periodically refresh apps in the background
    fn refresh_in_background(&mut self) {
        // get running and set it to true
        if self.running.load(std::sync::atomic::Ordering::Relaxed) {
            println!("refresh task already running");
            return;
        }
        self.running
            .store(true, std::sync::atomic::Ordering::Relaxed);

        let apps_clone = Arc::clone(&self.apps);
        let running_clone = Arc::clone(&self.running);
        thread::spawn(move || {
            loop {
                thread::sleep(Duration::from_millis(500)); // intentionally slow down refresh for 2 seconds
                let mut apps = apps_clone.lock().unwrap();
                println!("refreshing apps: {:?}", apps.clone());
                apps.push("app1".to_string());
                // get running and check if it is still running
                if !running_clone.load(std::sync::atomic::Ordering::Relaxed) {
                    println!("refresh task stopped");
                    break;
                }
            }
        });
    }

    fn stop_refresh(&mut self) {
        self.running
            .store(false, std::sync::atomic::Ordering::Relaxed);
    }
}

#[tokio::main]
async fn main() {
    let mut system = System::new();
    system.refresh_in_background();
    thread::sleep(Duration::from_secs(3));
    system.refresh_in_background();
    system.stop_refresh();
    println!("refresh stopped");
}

// output
// refreshing apps: []
// refreshing apps: ["app1"]
// refreshing apps: ["app1", "app1"]
// refreshing apps: ["app1", "app1", "app1"]
// refreshing apps: ["app1", "app1", "app1", "app1"]
// refresh task already running
// refresh stopped
```

## Example 4: Clipboard Watcher

This will be a larger example, go to [clipboard-watcher.md](./Samples/clipboard-watcher.md);

I discuss how to implement a clipboard watcher (or any other event listener) in Rust.

The following topics are covered

1. Creating callback functions
2. Using trait to define handlers
3. Using trait to handle multi-platform implementation of the watcher
4. Using Arc + Mutex to share data between threads
5. Rust generics
6. How to stop a watcher thread using
   1. Channel
   2. Flag (`AtomicBool`)
   3. `abort()` of tokio's `JoinHandle`
