---
title: Rust SocketIO Event Handling with Channel
authors: huakun
tags: [rust, socketio]
---

[rust-socketio](https://github.com/1c3t3a/rust-socketio) is an open source Rust client for socket.io

It has an async version, but the event handling is a bit tricky. All callback functions (closures) have to use `async move {}` to handle events. To use variables outside the closure, you have to make clones of the variables and pass them to the closure. The regular sync version also needs to do this, but the async version is more complicated because of the async nature. The variables have to be cloned and moved twice.

```rust
#[tokio::main]
async fn main() {
    let (tx, rx) = channel::<String>();
    let tx2 = tx.clone();
    let socket = ClientBuilder::new("http://localhost:9559")
        .on("evt1", move |payload, socket| {
            let tx = tx.clone();
            async move {
                tx.send(format!("identity: {:?}", payload)).unwrap();
            }
            .boxed()
        })
        // .on("evt1", callback2)
        .on_any(move |evt, payload, socket| {
            let tx = tx2.clone();
            async move {
                tx.send(format!("{:?}", payload)).unwrap();
            }
            .boxed()
        })
        .connect()
        .await
        .expect("Connection failed");
}
```

This makes things complicated and hard to read. I have to clone variables so many times. Rust's nature keeps me focusing on the language itself rather than the business logic. In JS I could finish this without even thinking about this problem.

See this issue https://github.com/1c3t3a/rust-socketio/issues/425

## Solution

What I ended up doing is use `on_any` and channel to transfer all event handling to another loop outside the closures to avoid variables moving. It's much simpler.

Here is how I did it.

```rust
#[derive(Debug)]
pub struct EventMessage {
    pub event: String,
    pub payload: Payload,
}

let (done_tx, mut done_rx) = tokio::sync::mpsc::channel::<()>(1);
let (evt_tx, mut evt_rx) = tokio::sync::mpsc::channel::<EventMessage>(1);

let socket = ClientBuilder::new(SERVER_URL)
    .on(Event::Connect, |_, _| async move {}.boxed())
    .on_any(move |evt, payload, _| {
        let evt_tx = evt_tx.clone();
        async move {
            evt_tx
                .send(EventMessage {
                    event: evt.to_string(),
                    payload,
                })
                .await
                .unwrap();
        }
        .boxed()
    })
    .on(Event::Error, |err, _: Client| {
        async move {
            eprintln!("Error: {:#?}", err);
        }
        .boxed()
    })
    .connect()
    .await
    .expect("Connection failed");


loop {
    tokio::select! {
        _ = done_rx.recv() => {
            break;
        }
        Some(evt) = evt_rx.recv() => {
            // Handle event received from evt_rx
            match evt.event.as_str() {
                "evt1" => {...}
                "evt2" => {...}
            }
        }
        _ = tokio::signal::ctrl_c() => {
            break;
        }
    };
}
```

All events are caught by `on_any` and sent to `evt_tx`. Then I can handle all events in the loop outside the closures. This way I don't have to clone variables so many times and move them. It's much simpler and easier to read.

Not sure about the performance difference. It shouldn't matter as this is dealing with network I/O. The performance bottleneck is the network, not the CPU. So I think this is a good solution.

Cloning variables, locking and unlocking mutexes, and moving variables from stack to heap all cost time, and are harder to read. Unsure about the cost of using channels, but I think it's a good trade-off.

I am thinking about a new design for `rust_socketio`. The `ClientBuilder` can simply return a channel to the user, and the user can handle all events in the loop with select outside the closures. This way the user can handle events in a more natural way.
