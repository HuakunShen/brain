---
title: Read Safari Bookmark
---

On Mac, Safari bookmarks are stored in `~/Library/Safari/Bookmarks.plist`.

## Permission

It's not readable directly. To read the file, we need to open a dialog to let user select the folder `~/Library/Safari/`, then read the file.

This is only the first step, bypass permission.

Then we need to parse the plist file.

## Parse plist file

May need to copy the plist file to another folder first so other processes can read it.

The following crates can parse plist file:

- Rust plist crate: https://crates.io/crates/plist
- Python plistlib: https://docs.python.org/3/library/plistlib.html

But in my scenario, I can't directly use them.
I am in a browser environment (tauri).

On Mac, the built-in `/usr/bin/python3` comes with `plistlib`.

To get the full code in python, ask CharGPT, it could easily given you the parser code.

Another option is to use mac's built-in command `plutil`.

The available formats are `xml1`, `binary1`, `json`, `swift`, `objc`.

`json` format doesn't seem to work, `xml1` format works.

After converting to `xml1` format, it's easy to convert to json with any language.

```bash
plutil -convert xml1 -o - ./Bookmarks.plist
plutil -convert xml1 -o output.xml  ./Bookmarks.plist
```
