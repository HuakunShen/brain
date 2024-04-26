---
title: Plugin/Extension System Design
---

VSCode and Chrome has a great extension ecosystem, allowing developers to enhance the functionality of them. How can we design such a system?

## Architecture Overview

For interpreted languages like Python and JavaScript, the main program can simply read the plugins' scripts. e.g. JavaScript library can be `import`/`require`. Python has `importlib`. The plugins can be run within the main programs process and thread.

For other compiled languages like Rust, it's more complicated. There are many options.

### Dynamic Library

#### Shared Object and DLL

Dynamic-link library (`.ddl`) is the shared library on Windows.

Shared Object (`.so`) is the shared library for Linux.

A library/plugin can be compiled into a shared library where an app can import dynamically. User just need to provide the library file. These libraries have to expose its functions in some specific standard, such as C API.

#### WebAssembly

Another similar (but different) concept is WebAssembly. WebAssembly runs in many languages. A program can import a WebAssembly module and import functions defined in it. This works similarly to shared libraries.

### Binary Sidecar

Compiling plugins into binaries as sidecars is another choice. The main difference is, the main program will have to run this as a separate process instead of importing as a library.

Pros: more flexible, don't have to deal with the interface between languages.

The problem with this is that the main program and plugins run in different processes and have to communicate. This is called IPC (Inter-Process Communication). Here are some options.

#### Pipe

Pipe can be used to communicate between the main and child process. More specifically stdin, stdout, stderr. Usually for parent-child process communication.

##### Named Pipe

Named pipes, also known as FIFOs (First-In-First-Out), are similar to pipes but can be used for communication between unrelated processes. They are created as special files in the file system, and processes can read from and write to them.

#### Message Queue

MQTT is an example, this requires a separate message queue server. 

#### Shared Memory

Multiple processes can access a common region of memory. This allows processes to share data directly, without the need for copying data between them. However, careful synchronization is required to avoid data corruption.

#### Sockets

Based on network. e.g. TCP connection between a client and server, sending raw bytes to each other.

#### HTTP Server

Similar to sockets, but a fully featured HTTP server with more functionalities, such as Web Soceket, GET/POST request. 