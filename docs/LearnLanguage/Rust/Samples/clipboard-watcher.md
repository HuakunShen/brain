# Clipboard Watcher Design

- [Clipboard Watcher Design](#clipboard-watcher-design)
  - [Level 0](#level-0)
  - [Level 1](#level-1)
    - [thread + channel](#thread--channel)
    - [tokio](#tokio)
  - [Level 1.1](#level-11)
  - [Level 1.2](#level-12)
  - [Level 1.3](#level-13)
  - [Level 2](#level-2)

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

TODO: provide a fire and forget start method for the watcher.

TODO: provide a better design.
