# Mac Finder Selected Files

This is actually purely AppleScript, but it's a useful way to get the selected files in Finder in Rust.

I tried to find objc binding for Rust.

`FIFinderSyncController` is a class in `FinderSync` framework. It has a method `selectedItemURLs` which returns the selected items in Finder.

https://developer.apple.com/documentation/findersync/fifindersynccontroller/selecteditemurls()?language=objc

But I couldn't find a way to use this in Rust. `let finder_sync_controller = class!(FIFinderSyncController);` doesn't work.

Searching for `FIFinderSyncController` in Rust code on GitHub, I get nothing. https://github.com/search?q=FIFinderSyncController+language%3ARust+&type=code

```rust

fn get_finder_selected_files() -> Vec<PathBuf> {
    let applescript = r#"
        tell application "Finder"
            set selectedFiles to selection
            set filePaths to {}
            repeat with aFile in selectedFiles
                set end of filePaths to POSIX path of (aFile as alias)
            end repeat
            return filePaths
        end tell
    "#;

    let output = Command::new("osascript")
        .arg("-e")
        .arg(applescript)
        .output()
        .expect("Failed to execute command");

    if output.status.success() {
        let paths_str = str::from_utf8(&output.stdout).unwrap_or("");
        let paths_str = paths_str.trim();
        let paths: Vec<PathBuf> = paths_str
            .split(",")
            .map(|path| path.trim())
            .map(|path| PathBuf::from(path))
            .collect();
        paths
    } else {
        vec![]
    }
}

fn main() {
    let finder_selected = get_finder_selected_files();
    println!("Selected files: {:?}", finder_selected);
}

```
