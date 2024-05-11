---
title: gRPC
---

RPC (Remote Procedure Call) is a protocol that one program can use to request a service from a program located in another computer in a network without having to understand the network's details. It's like calling a function in another program.

Proto files are used to define the service (like function declaration) and messages. The proto files are compiled into the language-specific code. The generated code is used to make RPC calls. It's kind of similar to GraphQL schema. Types are enforced.

gRPC is a high-performance, open-source universal RPC framework. It's developed by Google. It uses HTTP/2 for transport, Protocol Buffers as the interface description language, and provides features such as authentication, load balancing, bidirectional steaming and flow control.

gRPC is available in many languages. https://grpc.io/docs/languages/

These languages are officially supported by gRPC project by google.

While languages like Rust also have unofficial package: https://github.com/hyperium/tonic

gRPC, based on HTTP/2, uses binary payload which is more efficient than JSON. It's also faster than REST API.

## Reference

- [YouTube ByteByteGo: What is RPC? gRPC Introduction](https://youtu.be/gnchfOojMk4)
