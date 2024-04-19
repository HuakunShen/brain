# How to Implement a native feature in Rust?

Rustlings is a collection of small exercises to get you used to writing and reading Rust code. It's a good way to learn Rust basics, but when it comes to real life projects, there are much more to learn apart from the standard syntax you learn from Rustlings.

In this article, I will share a few tips on how to learn to implement a feature in Rust.

One of the most difficult things in Rust is to write platform-specific code to access system-level API. If there is no existing crate/library for the feature you want to implement, you need to write the code yourself.

For example, if you want to get the frontmost application in macOS, you need to use Objective-C API.

You usually need to use [objc](https://crates.io/crates/objc) and [cocoa](https://crates.io/crates/cocoa) crates.

The syntax is very ugly and hard to understand. You need to use `unsafe` block and `msg_send!` macro to call Objective-C methods. You need to start from learning from other people's code.

The first step is to find a relative API documentation from Apple: https://developer.apple.com/documentation/appkit/nsworkspace/1532097-frontmostapplication

Once you know the API method name, you can search for the method name in `Rust` code on GitHub:
https://github.com/search?q=frontmostApplication+language%3ARust+&type=code

Working code snippet: https://github.com/huytd/goxkey/blob/3e21648951e28501327b6172c7a5c10832417ad0/src/platform/macos.rs#L324

**Make sure you set language filter to `Rust`.**

For example, if you want to get clipboard content in macOS, you can search for `pasteboardItems`:
https://github.com/search?q=pasteboardItems+language%3ARust+&type=code

Here is the working code found https://github.com/ChurchTao/clipboard-rs/blob/f2fbf7911eb6d6ee00b1a77393326ae6b8dabe36/src/platform/macos.rs#L115

After experimenting a few code samples, you will usually find a working code snippet. You can then modify the code to fit your needs.

If no Rust code is found, you could look at how native languages use the APIs (native languages must have code samples), like AppleScript for macOS, Objective-C, or Swift. Or you could see how other languages call this API, e.g. Python, Java, etc.
