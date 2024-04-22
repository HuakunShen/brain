# Clipboard Watcher Design (Rust Conccurency)

- [Clipboard Watcher Design (Rust Conccurency)](#clipboard-watcher-design-rust-conccurency)
  - [Level 0](#level-0)
  - [Level 1](#level-1)
    - [thread + channel](#thread--channel)
    - [tokio](#tokio)
  - [Level 1.1](#level-11)
  - [Level 1.2](#level-12)
  - [Level 1.3](#level-13)
  - [Level 2](#level-2)
  - [Level 2.1](#level-21)
    - [Problem 1](#problem-1)
  - [Level 2.2: Simplify with tokio](#level-22-simplify-with-tokio)
  - [Level 2.3: Generics](#level-23-generics)

In this article, I discuss how to implement a clipboard watcher (or any other event listener) in Rust.

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

This sample demonstrates some designs for a clipboard watcher, or any watcher/listener/monitor.

Here are some requirements:

1. The watcher should be able to start and stop.
2. The watcher can accept multiple callback functions, these functions will be called when the watcher detects a change.
3. The watcher should be able to detect changes in the clipboard.
4. The watcher shouldn't block the main thread.

First I let ChatGPT 4 write the code for me.

## Level 0

```rust
// use clipboard_win::{Clipboard, formats, Getter, Setter};
use std::sync::{Arc, Mutex};
use std::time::Duration;
use clipboard_rs::{Clipboard, ClipboardContext};
use tokio::time::interval;

// Define a type for handlers
type Handler = dyn Fn(String) + Send + Sync;

struct ClipboardWatcher {
    handlers: Vec<Box<Handler>>,
    last_content: Arc<Mutex<String>>,
}

impl ClipboardWatcher {
    fn new() -> Self {
        Self {
            handlers: Vec::new(),
            last_content: Arc::new(Mutex::new(String::new())),
        }
    }

    fn add_handler<F>(&mut self, handler: F)
    where
        F: Fn(String) + 'static + Send + Sync,
    {
        self.handlers.push(Box::new(handler));
    }

    async fn run(&self) {
        let mut interval = interval(Duration::from_secs(1));
        let last_content = self.last_content.clone();
        let ctx = ClipboardContext::new().unwrap();
        loop {
            interval.tick().await;
            let current_content = ctx.get_text().unwrap();
            // let current_content = get_clipboard(formats::Unicode).unwrap_or_default();
            let mut last = last_content.lock().unwrap();
            if *last != current_content {
                *last = current_content.clone();
                for handler in &self.handlers {
                    handler(current_content.clone());
                }
            }
        }
    }
}

#[tokio::main]
async fn main() {
    let mut watcher = ClipboardWatcher::new();
    watcher.add_handler(|data| println!("Clipboard updated with: {}", data));
    watcher.run().await;
}
```

The example above is the simplest design, without the ability to stop the watcher.

## Level 1

### thread + channel

Here is the next design by ChatGPT 4.

```rust

// use clipboard::{ClipboardContext, ClipboardProvider};
use clipboard_rs::{Clipboard, ClipboardContext};
use crossbeam_channel::{unbounded, Sender};
use std::sync::{Arc, Mutex};
use std::thread;
use std::time::Duration;

type Callback = Box<dyn Fn(String) + Send + Sync>;

struct ClipboardWatcher {
    running: bool,
    callbacks: Arc<Mutex<Vec<Callback>>>,
    sender: Option<Sender<()>>,
}

impl ClipboardWatcher {
    pub fn new() -> Self {
        ClipboardWatcher {
            running: false,
            callbacks: Arc::new(Mutex::new(Vec::new())),
            sender: None,
        }
    }

    pub fn add_callback<F>(&mut self, callback: F)
    where
        F: Fn(String) + 'static + Send + Sync,
    {
        self.callbacks.lock().unwrap().push(Box::new(callback));
    }

    pub fn start(&mut self) {
        if self.running {
            println!("Watcher is already running.");
            return;
        }
        self.running = true;
        let (s, r) = unbounded::<()>();
        self.sender = Some(s);

        let callbacks = self.callbacks.clone();
        thread::spawn(move || {
            let clipboard = ClipboardContext::new().unwrap();
            let mut last_clipboard_content = clipboard.get_text().unwrap_or_default();

            loop {
                if r.try_recv().is_ok() {
                    break;
                }

                let current_clipboard_content = clipboard.get_text().unwrap_or_default();
                if last_clipboard_content != current_clipboard_content {
                    let funcs = callbacks.lock().unwrap();
                    for callback in funcs.iter() {
                        callback(current_clipboard_content.clone());
                    }
                    last_clipboard_content = current_clipboard_content;
                }

                thread::sleep(Duration::from_millis(500)); // Polling interval
            }
        });
    }

    pub fn stop(&mut self) {
        if let Some(sender) = self.sender.take() {
            sender.send(()).unwrap();
            self.running = false;
        }
    }
}

fn main() {
    let mut watcher = ClipboardWatcher::new();
    watcher.add_callback(|data| println!("Clipboard updated with: {}", data));
    watcher.start();

    // Simulate running for some time
    thread::sleep(Duration::from_secs(10));

    watcher.stop();
}
```

Now the watcher can be stopped with the help of `crossbeam_channel`. `if r.try_recv().is_ok()` checks if the watcher should stop.

This is actually similar to using a `running` flag. I had examples discussing using a boolean `running` flag in the discussion on [Concurrency](../concurrency.md).

### tokio

I modified the previous design to use `tokio` instead of `thread` + `crossbeam_channel`, the resulting code is simpler as tokio tasks has an `.abort()` option.

For a simpler example like this, look at my discussion in [concurrency.md](../concurrency.md#provide-stop-method-in-system-tokio).

```rust
use clipboard_rs::{Clipboard, ClipboardContext};
use std::sync::{Arc, Mutex};
use std::time::Duration;

type Callback = Box<dyn Fn(String) + Send + Sync>;

struct ClipboardWatcher {
    callbacks: Arc<Mutex<Vec<Callback>>>,
    join_handle: Option<tokio::task::JoinHandle<()>>,
}

impl ClipboardWatcher {
    pub fn new() -> Self {
        ClipboardWatcher {
            callbacks: Arc::new(Mutex::new(Vec::new())),
            join_handle: None,
        }
    }

    pub fn add_callback<F>(&mut self, callback: F)
    where
        F: Fn(String) + 'static + Send + Sync,
    {
        self.callbacks.lock().unwrap().push(Box::new(callback));
    }

    pub fn start(&mut self) {
        if self.join_handle.is_some() {
            println!("Watcher is already running.");
            return;
        }
        if self.callbacks.lock().unwrap().is_empty() {
            println!("No callbacks added. Exiting.");
            return;
        }

        let callbacks = self.callbacks.clone();
        self.join_handle = Some(tokio::task::spawn(async move {
            let clipboard = ClipboardContext::new().unwrap();
            let mut last_clipboard_content = clipboard.get_text().unwrap_or_default();

            loop {
                let current_clipboard_content = clipboard.get_text().unwrap_or_default();
                if last_clipboard_content != current_clipboard_content {
                    let funcs = callbacks.lock().unwrap();
                    for callback in funcs.iter() {
                        callback(current_clipboard_content.clone());
                    }
                    last_clipboard_content = current_clipboard_content;
                }

                tokio::time::sleep(Duration::from_millis(500)).await;
            }
        }));
    }

    pub fn stop(&mut self) {
        if let Some(handle) = self.join_handle.take() {
            handle.abort();
        }
    }
}

#[tokio::main]
async fn main() {
    let mut watcher = ClipboardWatcher::new();
    watcher.add_callback(|data| println!("Clipboard updated with: {}", data));
    watcher.start();

    // Simulate running for some time
    tokio::time::sleep(Duration::from_secs(10)).await;

    watcher.stop();
    println!("Watcher stopped");
}
```

## Level 1.1

Then I tell ChatGPT 4 I want the callback function to be able to access some variable.

```rust
fn main() {
    let mut watcher = ClipboardWatcher::new();

    // Example of a callback with context
    let user_id = 42;
    watcher.add_callback(move |data| {
        println!("User {} got clipboard data: {}", user_id, data);
    });

    watcher.start();

    // Simulate running for some time
    thread::sleep(Duration::from_secs(10));

    watcher.stop();
}
```

## Level 1.2

Great, but I want the `user_id` to be able to be mutable.

ChatGPT gives me.

```rust
fn main() {
    let mut watcher = ClipboardWatcher::new();
    let user_id = Arc::new(Mutex::new(42));

    watcher.add_callback({
        let user_id = user_id.clone();
        move |data| {
            let mut id = user_id.lock().unwrap();
            println!("User {} got clipboard data: {}", id, data);
            *id += 1; // Increment the user_id each time the callback is called
        }
    });

    watcher.start();

    // Simulate running for some time
    thread::sleep(Duration::from_secs(10));

    watcher.stop();

    // Check the final value of user_id
    println!("Final user ID: {}", *user_id.lock().unwrap());
}
```

## Level 1.3

Rather than using `type Callback = Box<dyn Fn(String) + Send + Sync>;` type for callback, we can use a trait and a user-custom struct.

See the example below.

```rust
use clipboard::{ClipboardContext, ClipboardProvider};
use crossbeam_channel::{unbounded, Sender};
use std::sync::{Arc, Mutex};
use std::thread;
use std::time::Duration;

// Define the trait for handling clipboard changes
trait ClipboardObserver {
    fn on_change(&mut self, new_content: String);
}

// Implement the ClipboardWatcher
struct ClipboardWatcher {
    running: bool,
    observers: Arc<Mutex<Vec<Box<dyn ClipboardObserver + Send>>>>,
    sender: Option<Sender<()>>,
}

impl ClipboardWatcher {
    pub fn new() -> Self {
        ClipboardWatcher {
            running: false,
            observers: Arc::new(Mutex::new(Vec::new())),
            sender: None,
        }
    }

    pub fn add_observer<T>(&mut self, observer: T)
    where
        T: ClipboardObserver + 'static + Send,
    {
        self.observers.lock().unwrap().push(Box::new(observer));
    }

    pub fn start(&mut self) {
        if self.running {
            println!("Watcher is already running.");
            return;
        }
        self.running = true;
        let (s, r) = unbounded::<()>();
        self.sender = Some(s);

        let observers = self.observers.clone();
        thread::spawn(move || {
            let mut clipboard: ClipboardContext = ClipboardProvider::new().unwrap();
            let mut last_clipboard_content = clipboard.get_contents().unwrap_or_default();

            loop {
                if r.try_recv().is_ok() {
                    break;
                }

                let current_clipboard_content = clipboard.get_contents().unwrap_or_default();
                if last_clipboard_content != current_clipboard_content {
                    let mut obs = observers.lock().unwrap();
                    for observer in obs.iter_mut() {
                        observer.on_change(current_clipboard_content.clone());
                    }
                    last_clipboard_content = current_clipboard_content;
                }

                thread::sleep(Duration::from_millis(500));
            }
        });
    }

    pub fn stop(&mut self) {
        if let Some(sender) = self.sender.take() {
            sender.send(()).unwrap();
            self.running = false;
        }
    }
}

// Example implementation of the ClipboardObserver trait
struct Logger {
    count: u32,
}

impl Logger {
    fn new() -> Self {
        Logger { count: 0 }
    }
    fn increment(&mut self) {
        self.count += 1;
    }
}

impl ClipboardObserver for Logger {
    fn on_change(&mut self, new_content: String) {
        self.increment();
        println!("{}: {}", self.count, new_content);
    }
}

// Usage example
fn main() {
    let mut watcher = ClipboardWatcher::new();
    watcher.add_observer(Logger::new());

    watcher.start();

    // Simulate running for some time
    thread::sleep(Duration::from_secs(10));

    watcher.stop();
}

```

A struct gives us more flexibility and control over the callback function. We can implement custom methods and add more fields to the struct.

## Level 2

Here is a simplified version of how [`clipboard-rs`](https://crates.io/crates/clipboard-rs) crate implements the clipboard watcher.

<details>
<summary>Code</summary>

```rust
use clipboard_rs::{Clipboard, ClipboardContext};
use std::{
    sync::mpsc::{self, Receiver, Sender},
    thread,
    time::Duration,
};

pub trait ClipboardHandler {
    fn on_clipboard_change(&mut self);
}

pub struct ClipboardWatcherContext<T: ClipboardHandler> {
    clipboard: ClipboardContext,
    handlers: Vec<T>,
    stop_signal: Sender<()>,
    stop_receiver: Receiver<()>,
    running: bool,
}

unsafe impl<T: ClipboardHandler> Send for ClipboardWatcherContext<T> {}

impl<T: ClipboardHandler> ClipboardWatcherContext<T> {
    pub fn new() -> Self {
        let (tx, rx) = mpsc::channel();
        ClipboardWatcherContext {
            clipboard: ClipboardContext::new().unwrap(),
            handlers: Vec::new(),
            stop_signal: tx,
            stop_receiver: rx,
            running: false,
        }
    }
}

pub struct WatcherShutdown {
    stop_signal: Sender<()>,
}
impl Drop for WatcherShutdown {
    fn drop(&mut self) {
        let _ = self.stop_signal.send(());
    }
}

impl WatcherShutdown {
    pub fn stop(self) {
        drop(self);
    }
}

pub trait ClipboardWatcher<T: ClipboardHandler>: Send {
    fn add_handler(&mut self, handler: T) -> &mut Self;
    fn start_watch(&mut self);
    fn start_watch_block(&mut self);
    fn get_shutdown_channel(&self) -> WatcherShutdown;
}

impl<T: ClipboardHandler> ClipboardWatcher<T> for ClipboardWatcherContext<T> {
    fn add_handler(&mut self, handler: T) -> &mut Self {
        self.handlers.push(handler);
        self
    }

    fn start_watch_block(&mut self) {
        if self.running {
            println!("already start watch!");
            return;
        }
        if self.handlers.is_empty() {
            println!("no handler, no need to start watch!");
            return;
        }
        self.running = true;
        let mut last_text = self.clipboard.get_text().unwrap();
        loop {
            // if receive stop signal, break loop
            if self
                .stop_receiver
                .recv_timeout(std::time::Duration::from_millis(500))
                .is_ok()
            {
                break;
            }
            let text = self.clipboard.get_text().unwrap();
            if last_text != text {
                self.handlers
                    .iter_mut()
                    .for_each(|handler| handler.on_clipboard_change());
                last_text = text;
            }
        }

        self.running = false;
    }

    fn get_shutdown_channel(&self) -> WatcherShutdown {
        WatcherShutdown {
            stop_signal: self.stop_signal.clone(),
        }
    }

    fn start_watch(&mut self) {
        todo!()
    }
}

struct ClipboardHandlerImpl {
    ctx: ClipboardContext,
}

impl ClipboardHandlerImpl {
    pub fn new() -> Self {
        let ctx = ClipboardContext::new().unwrap();
        ClipboardHandlerImpl { ctx }
    }
}

impl ClipboardHandler for ClipboardHandlerImpl {
    fn on_clipboard_change(&mut self) {
        println!(
            "on_clipboard_change, txt = {}",
            self.ctx.get_text().unwrap()
        );
    }
}

fn main() {
    let mut watcher = ClipboardWatcherContext::new();
    watcher.add_handler(ClipboardHandlerImpl::new());
    let shutdown_channel = watcher.get_shutdown_channel();
    thread::spawn(move || {
        watcher.start_watch_block();
    });
    println!("watcher started, waiting for 5 seconds");
    thread::sleep(Duration::from_secs(5));
    shutdown_channel.stop();
    println!("watcher stopped");
}

```

</details>

It's much more complicated. Let's discuss the design.

1.  Channel is used to send a stop signal to the watcher.

    ```rust
    pub struct WatcherShutdown {
        stop_signal: Sender<()>,
    }
    impl Drop for WatcherShutdown {
        fn drop(&mut self) {
            let _ = self.stop_signal.send(());
        }
    }

    impl WatcherShutdown {
        pub fn stop(self) {
            drop(self);
        }
    }
    ```

    When `stop()` is called, drop is called, and the stop signal is sent.

    On the other side, in the loop, the receiver checks if the signal is received every 500ms. Once signal received, the loop breaks, and `start_watch_block()` returns.

    ```rust
        if self
            .stop_receiver
            .recv_timeout(std::time::Duration::from_millis(500))
            .is_ok()
    ```

2.  `ClipboardHandler` is designed as a schema for callback "functions". The watcher knows the handler must have a `on_clipboard_change` method.

    ```rust
    pub trait ClipboardHandler {
        fn on_clipboard_change(&mut self);
    }

    struct ClipboardHandlerImpl {
        ctx: ClipboardContext,
    }

    impl ClipboardHandlerImpl {
        pub fn new() -> Self {
            let ctx = ClipboardContext::new().unwrap();
            ClipboardHandlerImpl { ctx }
        }
    }

    impl ClipboardHandler for ClipboardHandlerImpl {
        fn on_clipboard_change(&mut self) {
            println!(
                "on_clipboard_change, txt = {}",
                self.ctx.get_text().unwrap()
            );
        }
    }

    let mut watcher = ClipboardWatcherContext::new();
    watcher.add_handler(ClipboardHandlerImpl::new());
    ```

3.  `ClipboardWatcher` declares the methods a watcher should have. The reason for this is that [`clipboard-rs`](https://crates.io/crates/clipboard-rs) crate has multiple implementations of the watcher. One for each platform (Mac, Windows, Linux). Each platform has their own `ClipboardWatcherContext` that could contain some platform-specific fields (in our simplified example there is no platform-specific code, but in [`clipboard-rs`](https://crates.io/crates/clipboard-rs)'s original code, the `clipboard` field in Mac's `ClipboardWatcherContext` has a `NSPasteboard` from `cocoa`, a Mac API binding crate. This field is not in Windows' `ClipboardWatcherContext`). So, depending on the real life scenario, this Trait may or may not be necessary.

    ```rust
    pub trait ClipboardWatcher<T: ClipboardHandler>: Send {
        fn add_handler(&mut self, handler: T) -> &mut Self;
        fn start_watch(&mut self);
        fn start_watch_block(&mut self);
        fn get_shutdown_channel(&self) -> WatcherShutdown;
    }

    pub struct ClipboardWatcherContext<T: ClipboardHandler> {
        clipboard: ClipboardContext,
        handlers: Vec<T>,
        stop_signal: Sender<()>,
        stop_receiver: Receiver<()>,
        running: bool,
    }

    ```

4.  TODO: explains the `unsafe impl` of `Send` trait on `ClipboardWatcherContext`
    ```rust
    unsafe impl<T: ClipboardHandler> Send for ClipboardWatcherContext<T> {}
    ```

## Level 2.1

In this level I implemented a similar design to the previous one, but with a fire and forget `start()` funciton.

It runs watcher in the background, without needing users to manually run `thread::spawn`, and there is a `watcher.stop()` function to stop the watcher thread at any time.

A `start_block()` function is also implemented, which run in the main thread and blocks the main thread.

```rust
use std::{
    sync::{atomic::AtomicBool, Arc, Mutex},
    thread,
    time::Duration,
};

use clipboard_rs::{Clipboard, ClipboardContext};

pub trait ClipboardHandler {
    fn on_clipboard_change(&mut self);
}

struct Watcher<T: ClipboardHandler> {
    clipboard: Arc<ClipboardContext>,
    running: Arc<AtomicBool>,
    handlers: Arc<Mutex<Vec<T>>>,
}

trait WatcherTrait<T: ClipboardHandler + Send + Sync> {
    fn new() -> Self;
    fn add_handler(&mut self, handler: T) -> &mut Self;
    fn start_block(&self);
    fn start(&self);
    fn stop(&self);
}

impl<T: ClipboardHandler + Sync + Send + 'static> WatcherTrait<T> for Watcher<T> {
    fn new() -> Self {
        Watcher {
            clipboard: Arc::new(ClipboardContext::new().unwrap()),
            running: Arc::new(AtomicBool::new(false)),
            handlers: Arc::new(Mutex::new(Vec::new())),
        }
    }

    fn add_handler(&mut self, handler: T) -> &mut Self {
        self.handlers.lock().unwrap().push(handler);
        self
    }

    fn start_block(&self) {
        self.running
            .store(true, std::sync::atomic::Ordering::Relaxed);
        let mut last_text = String::new();
        loop {
            if !self.running.load(std::sync::atomic::Ordering::Relaxed) {
                break;
            }
            let txt = self.clipboard.get_text().unwrap();
            if last_text != txt {
                let mut handlers = self.handlers.lock().unwrap();
                for handler in handlers.iter_mut() {
                    handler.on_clipboard_change();
                }
                last_text = txt;
            }
            thread::sleep(Duration::from_secs(1));
        }
    }

    fn start(&self) {
        if self.running.load(std::sync::atomic::Ordering::Relaxed) {
            println!("already start watch!");
            return;
        }
        self.running
            .store(true, std::sync::atomic::Ordering::Relaxed);
        if self.handlers.lock().unwrap().is_empty() {
            println!("no handler, no need to start watch!");
            return;
        }
        let running_clone = Arc::clone(&self.running);
        let clipboard_clone = Arc::clone(&self.clipboard);
        let handlers_clone = Arc::clone(&self.handlers);
        let mut last_text = String::new();
        thread::spawn(move || loop {
            if !running_clone.load(std::sync::atomic::Ordering::Relaxed) {
                break;
            }
            let txt = clipboard_clone.get_text().unwrap();
            if last_text != txt {
                let mut handlers = handlers_clone.lock().unwrap();
                for handler in handlers.iter_mut() {
                    handler.on_clipboard_change();
                }
                last_text = txt;
            }
            thread::sleep(Duration::from_secs(1));
        });
    }

    fn stop(&self) {
        self.running
            .store(false, std::sync::atomic::Ordering::Relaxed);
    }
}

struct ClipboardHandlerImpl {
    ctx: ClipboardContext,
}

impl ClipboardHandlerImpl {
    pub fn new() -> Self {
        let ctx = ClipboardContext::new().unwrap();
        ClipboardHandlerImpl { ctx }
    }
}

impl ClipboardHandler for ClipboardHandlerImpl {
    fn on_clipboard_change(&mut self) {
        println!("txt = {}", self.ctx.get_text().unwrap());
    }
}

fn main() {
    let mut watcher = Watcher::new();
    watcher.add_handler(ClipboardHandlerImpl::new());
    watcher.start();
    // watcher.start_block();
    thread::sleep(Duration::from_secs(6));
    watcher.stop();
}
```

However, there is a small problem with this design:

### Problem 1

> I have to manually spawn a new thread. Ideally I want to encapsulate the thread spawning inside the `Watcher` struct.

```rust
let mut watcher = Watcher::new();
watcher.add_handler(ClipboardHandlerImpl::new());
thread::spawn(move || {
    watcher.start_block();
});
thread::sleep(Duration::from_secs(5));
watcher.stop(); // borrow of moved value: `watcher` value borrowed here after move
```

If I want to run the watcher in a manually spawned thread, I can't use `watcher.stop()` to stop the watcher.

There could be multiple solutions to this problem:

1.  Use `Arc<Mutex<Watcher>>` to wrap the watcher, and clone the `Arc` before moving it to the thread.
2.  Use the `WatcherShutdown` design from Level 2.
    <details>
    <summary>Add these patch to fix the problem.</summary>
    
    ```rust
    impl<T: ClipboardHandler + Sync + Send + 'static> Watcher<T> {
        fn get_shutdown(&self) -> WatcherShutdown {
            WatcherShutdown {
                running: Arc::clone(&self.running),
            }
        }
    }

    pub struct WatcherShutdown {
        running: Arc<AtomicBool>,
    }

    impl WatcherShutdown {
        pub fn stop(self) {
            self.running.store(false, std::sync::atomic::Ordering::Relaxed);
        }
    }

    fn main() {
        let mut watcher = Watcher::new();
        let shutdown = watcher.add_handler(ClipboardHandlerImpl::new()).get_shutdown();
        thread::spawn(move || {
            watcher.start_block();
        });
        thread::sleep(Duration::from_secs(5));
        shutdown.stop();
    }

    ```

    </details>

## Level 2.2: Simplify with tokio

The previous design is good, but implementation gets complicated as we need to use a `running` flag to stop the thread. There is no way to stop a thread.

With `tokio`, we can use `tokio::task::JoinHandle` to stop the thread, who has an `.abort()` function.

Simply store the `JoinHandle` in the watcher, and call `.abort()` to stop the watcher. Same as the example in [concurrency.md](../concurrency.md#provide-stop-method-in-system-tokio).

<details>
<summary>Full Code</summary>

```rust
use clipboard_rs::{Clipboard, ClipboardContext};
use std::{
    sync::{Arc, Mutex},
    time::Duration,
};

pub trait ClipboardHandler {
    fn on_clipboard_change(&mut self);
}

struct Watcher<T: ClipboardHandler> {
    clipboard: Arc<ClipboardContext>,
    join_handle: Option<tokio::task::JoinHandle<()>>,
    handlers: Arc<Mutex<Vec<T>>>,
}

trait WatcherTrait<T: ClipboardHandler> {
    fn new() -> Self;
    fn add_handler(&mut self, handler: T) -> &mut Self;
    // fn start(&self);
    async fn start(&mut self);
    fn stop(&self);
}

impl<T: ClipboardHandler + Sync + Send + 'static> WatcherTrait<T> for Watcher<T> {
    fn new() -> Self {
        Watcher {
            clipboard: Arc::new(ClipboardContext::new().unwrap()),
            join_handle: None,
            handlers: Arc::new(Mutex::new(Vec::new())),
        }
    }

    fn add_handler(&mut self, handler: T) -> &mut Self {
        self.handlers.lock().unwrap().push(handler);
        self
    }

    async fn start(&mut self) {
        let clipboard_clone = Arc::clone(&self.clipboard);
        let handlers_clone = Arc::clone(&self.handlers);
        self.join_handle = Some(tokio::task::spawn(async move {
            let mut last_text = String::new();
            loop {
                let txt = clipboard_clone.get_text().unwrap();
                if last_text != txt {
                    for handler in handlers_clone.lock().unwrap().iter_mut() {
                        handler.on_clipboard_change();
                    }
                    last_text = txt;
                }
                tokio::time::sleep(Duration::from_secs(1)).await;
            }
        }));
    }

    fn stop(&self) {
        if let Some(handle) = self.join_handle.as_ref() {
            handle.abort();
        }
    }
}

struct ClipboardHandlerImpl {
    ctx: ClipboardContext,
}

impl ClipboardHandlerImpl {
    pub fn new() -> Self {
        let ctx = ClipboardContext::new().unwrap();
        ClipboardHandlerImpl { ctx }
    }
}

impl ClipboardHandler for ClipboardHandlerImpl {
    fn on_clipboard_change(&mut self) {
        println!("txt = {}", self.ctx.get_text().unwrap());
    }
}

#[tokio::main]
async fn main() {
    let mut watcher = Watcher::new();
    watcher.add_handler(ClipboardHandlerImpl::new());
    watcher.start().await;
    tokio::time::sleep(Duration::from_secs(5)).await;
    watcher.stop();
    println!("stop called");
    tokio::time::sleep(Duration::from_secs(5)).await;
}
```

</details>

`join_handle` is stored as a Option. When it's `None`, the watcher is not running. When it's `Some`, the watcher is running.

```rust
struct Watcher<T: ClipboardHandler> {
    clipboard: Arc<ClipboardContext>,
    handlers: Arc<Mutex<Vec<T>>>,
    join_handle: Option<tokio::task::JoinHandle<()>>,
}
```

The start function simply spawns a new task, and stores the `JoinHandle` in the watcher.

```rust
async fn start(&mut self) {
    let clipboard_clone = Arc::clone(&self.clipboard);
    let handlers_clone = Arc::clone(&self.handlers);
    self.join_handle = Some(tokio::task::spawn(async move {
        let mut last_text = String::new();
        loop {
            let txt = clipboard_clone.get_text().unwrap();
            if last_text != txt {
                for handler in handlers_clone.lock().unwrap().iter_mut() {
                    handler.on_clipboard_change();
                }
                last_text = txt;
            }
            tokio::time::sleep(Duration::from_secs(1)).await;
        }
    }));
}
```

In main function, we can start the watcher with `watcher.start().await`, and stop it with `watcher.stop()`.

```rust
#[tokio::main]
async fn main() {
    let mut watcher = Watcher::new();
    watcher.add_handler(ClipboardHandlerImpl::new());
    watcher.start().await;
    tokio::time::sleep(Duration::from_secs(5)).await;
    watcher.stop();
    tokio::time::sleep(Duration::from_secs(5)).await;
}
```

## Level 2.3: Generics

The generic is very complicated

```rust
impl<T: ClipboardHandler + Sync + Send + 'static> WatcherTrait<T> for Watcher<T> {...}
```

`Sync` and `Send` are necessary to make sure handlers can be used in threads. `'static` is used to make sure the handlers live a long enough time.

There is not really a good solution for this, but I want to discus the generics used here.

Let's forget about `Sync + Send + 'static` for a moment.

```rust
trait WatcherTrait {
    fn new() -> Self;
    fn add_handler(&mut self, handler: Box<dyn ClipboardHandler>);
    fn start(&mut self);
    fn stop(&self);
}

struct Watcher<T: ClipboardHandler> {
    clipboard: Arc<ClipboardContext>,
    handlers: Vec<T>,
}

struct Watcher2 {
    clipboard: Arc<ClipboardContext>,
    // Error: the size for values of type `(dyn ClipboardHandler + 'static)` cannot be known at compilation time the trait `Sized` is not implemented for `(dyn ClipboardHandler + 'static)`
    handlers: Vec<ClipboardHandler>,
}
```

The error message is clear, the size of the implementations of trait `ClipboardHandler` is unknown at compile time. This is because `ClipboardHandler` is a trait, and trait objects have a dynamic size. `handlers: Vec<Box<dyn ClipboardHandler>>`

Anyways, when `Box` and `dyn` are used, the code will get more and more complicated.

The resulting handlers will be `Box<dyn ClipboardHandler + Send + Sync + 'static>`, which is very complicated.

Thus, in previous implementation I used is `impl<T: ClipboardHandler> WatcherTrait<T> for Watcher<T> {...}`.

`T` has to be a struct that implements `ClipboardHandler`, which means the type of `T` is consistent, and size of `T` is known at compile time.

For example, in the following code, `T` is `ClipboardHandlerImpl`, which is a struct that implements `ClipboardHandler`. The size of `ClipboardHandlerImpl` is known at compile time.

```rust
struct ClipboardHandlerImpl {
    ctx: ClipboardContext,
}
fn main() {
    // ...
    watcher.add_handler(ClipboardHandlerImpl::new());
    // ...
}
```

If you want to use the `Box<dyn ClipboardHandler>` approach, here is the fully working code.

<details>
<summary>Full Code</summary>

```rust
use clipboard_rs::{Clipboard, ClipboardContext};
use std::{
    sync::{Arc, Mutex},
    time::Duration,
};

pub trait ClipboardHandler {
    fn on_clipboard_change(&mut self);
}

trait WatcherTrait {
    fn new() -> Self;
    fn add_handler(&mut self, handler: Box<dyn ClipboardHandler + Send + Sync + 'static>) -> &mut Self;
    fn start_block(&mut self);
    async fn start(&mut self);
    fn stop(&self);
}

struct Watcher {
    clipboard: Arc<ClipboardContext>,
    handlers: Arc<Mutex<Vec<Box<dyn ClipboardHandler + Send + Sync + 'static>>>>,
    join_handle: Option<tokio::task::JoinHandle<()>>,
}


impl WatcherTrait for Watcher {
    fn new() -> Self {
        Watcher {
            clipboard: Arc::new(ClipboardContext::new().unwrap()),
            handlers: Arc::new(Mutex::new(Vec::new())),
            join_handle: None,
        }
    }

    fn add_handler(&mut self, handler: Box<dyn ClipboardHandler + Send + Sync + 'static>) -> &mut Self {
        self.handlers.lock().unwrap().push(handler);
        self
    }

    fn start_block(&mut self) {
        let mut last_text = String::new();
        loop {
            let txt = self.clipboard.get_text().unwrap();
            if last_text != txt {
                // let mut handlers = self.handlers.lock().unwrap();
                for handler in self.handlers.lock().unwrap().iter_mut() {
                    handler.on_clipboard_change();
                }
                last_text = txt;
            }
            std::thread::sleep(Duration::from_secs(1));
        }
    }

    async fn start(&mut self) {
        let clipboard_clone = Arc::clone(&self.clipboard);
        let handlers_clone = Arc::clone(&self.handlers);
        self.join_handle = Some(tokio::task::spawn(async move {
            let mut last_text = String::new();
            loop {
                let txt = clipboard_clone.get_text().unwrap();
                if last_text != txt {
                    for handler in handlers_clone.lock().unwrap().iter_mut() {
                        handler.on_clipboard_change();
                    }
                    last_text = txt;
                }
                tokio::time::sleep(Duration::from_secs(1)).await;
            }
        }));
    }

    fn stop(&self) {
        if let Some(handle) = self.join_handle.as_ref() {
            handle.abort();
        }
    }
}

struct ClipboardHandlerImpl {
    ctx: ClipboardContext,
}

impl ClipboardHandlerImpl {
    pub fn new() -> Self {
        let ctx = ClipboardContext::new().unwrap();
        ClipboardHandlerImpl { ctx }
    }
}

impl ClipboardHandler for ClipboardHandlerImpl {
    fn on_clipboard_change(&mut self) {
        println!("txt = {}", self.ctx.get_text().unwrap());
    }
}

#[tokio::main]
async fn main() {
    let mut watcher = Watcher::new();
    watcher.add_handler(Box::new(ClipboardHandlerImpl::new()));
    watcher.start().await;
    tokio::time::sleep(Duration::from_secs(5)).await;
    watcher.stop();
    println!("stop called");
    tokio::time::sleep(Duration::from_secs(5)).await;
}
```

</details>

Using smart pointers `Box` and `dyn` keyword is a good way to handle trait objects, but it makes the code more complicated.

Here is an example, when adding handler, it has to be wrapped in a `Box`.

```rust
watcher.add_handler(Box::new(ClipboardHandlerImpl::new()));
```

Personally I believe [level 2.2](#level-22-simplify-with-tokio) is a better design, as it is simpler and more straightforward.
