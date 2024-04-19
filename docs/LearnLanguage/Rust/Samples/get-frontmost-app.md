# Get Frontmost Application

I found this in by searching for `frontmostApplication` in Rust code on GitHub.

https://github.com/search?q=frontmostApplication+language%3ARust+&type=code

Code found in https://github.com/huytd/goxkey/blob/3e21648951e28501327b6172c7a5c10832417ad0/src/platform/macos.rs#L324

```rust
extern crate objc;

use cocoa::base::id;
use objc::declare::ClassDecl;
use objc::runtime::{Class, Object};
use objc::{class, msg_send, sel, sel_impl};
use std::path::PathBuf;
use std::process::Command;
use std::str;

#[macro_export]
macro_rules! nsstring_to_string {
    ($ns_string:expr) => {{
        use objc::{sel, sel_impl};
        let utf8: id = objc::msg_send![$ns_string, UTF8String];
        let string = if !utf8.is_null() {
            Some({
                std::ffi::CStr::from_ptr(utf8 as *const std::ffi::c_char)
                    .to_string_lossy()
                    .into_owned()
            })
        } else {
            None
        };
        string
    }};
}

pub fn get_active_app_name() -> String {
    unsafe {
        let shared_workspace: id = msg_send![class!(NSWorkspace), sharedWorkspace];
        let front_most_app: id = msg_send![shared_workspace, frontmostApplication];
        let bundle_url: id = msg_send![front_most_app, bundleURL];
        let path: id = msg_send![bundle_url, path];
        nsstring_to_string!(path).unwrap_or("/Unknown.app".to_string())
    }
}


fn main() {
    std::thread::sleep(std::time::Duration::from_secs(5)); // so you have time to switch to another application before the app name is printed
    let app_name = get_active_app_name();
    println!("Active App: {}", app_name);
}
```
