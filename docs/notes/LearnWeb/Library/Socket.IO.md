# Socket.IO

https://socket.io/

> Bidirectional and low-latency communication for every platform

It's like a wrapper of WebSocket, making WebSocket and realtime communication much easier.

# Supported Languages

Many languages are supported for both server and client, as of the date of writing, here is a list of supported languages.

## Client Implementations

There are also several client implementation in other languages, which are maintained by the community:

- Java: https://github.com/socketio/socket.io-client-java
- C++: https://github.com/socketio/socket.io-client-cpp
- Swift: https://github.com/socketio/socket.io-client-swift
- Dart: https://github.com/rikulo/socket.io-client-dart
- Python: https://github.com/miguelgrinberg/python-socketio
- .Net: https://github.com/doghappy/socket.io-client-csharp
- Rust: https://github.com/1c3t3a/rust-socketio

## Server Implementations

- Golang: https://github.com/googollee/go-socket.io
- Golang: https://github.com/ambelovsky/gosf
- Java: https://github.com/mrniko/netty-socketio
- Java: https://github.com/trinopoty/socket.io-server-java
- Python: https://github.com/miguelgrinberg/python-socketio

Socket.io is designed for Nodejs natively, so only Nodejs has official server implementation,

Java, C++ and Swift clients are also officially supported to accomodate Android, Desktop and Apple apps.

# Important Notes and Docs

- [TypeScript Support](https://socket.io/docs/v4/typescript/)
- [Unit Testing](https://socket.io/docs/v4/testing/)
- [Adapters](https://socket.io/docs/v4/adapter/) for distributed systems
  - Replace in-memory adapter with database adapters when scaling to multiple Socket.IO servers
  - I've personally used [Redis Adapter](https://socket.io/docs/v4/redis-adapter/) and it works fine
- [Socket.IO Cheatsheet](https://socket.io/docs/v3/emit-cheatsheet/)
- [Concept of Room](https://socket.io/docs/v3/rooms/)
  - Room concept allows users to
    - communicate with each other in a many to many way
    - broadcast to a group of users
    - etc.
  - It's an essential concept to understand
- [Concept of Namespaces](https://socket.io/docs/v3/namespaces/)
  - > A Namespace is a communication channel that allows you to split the logic of your application over a single shared connection


## Admin UI

Socket.IO provides an admin UI for monitoring and debugging purposes. 

Docs: https://socket.io/blog/admin-ui-first-release/

Go to this website to get connected. https://admin.socket.io

### Note on CORS

Setting CORS to "*" may not work. you may have to set `origin: ["https://admin.socket.io"]`.



