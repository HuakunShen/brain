---
title: Flutter
---

## Installation

https://docs.flutter.dev/get-started/install/macos

Installation on MacOS isn't straight forward.

You not only need Android Studio and XCode, but also need to create simulator for them.
Start a dummy project with them and make sure a simulator can run.

If you get error about cocoa pods.

You need to run

```bash
gem which cocoapods
# find the path to ruby and add its bin to PATH
export PATH=/Users/hacker/.local/share/gem/ruby/3.2.0/bin/:$PATH
```

If you have problem with android sdk command line tool,
Go to Android Studio Android SDK setting, and install the command line tool.

<img src="https://hacker-storage.s3.us-east-2.amazonaws.com/2023/11/22/a87a3d53-2184-4ea3-8e22-febc75e09922.png" width="100%" />

`ANDROID_HOME` android home can be found in Android Stdudio by searching for Android SDK.

```bash
export ANDROID_HOME=/Users/hacker/Library/Android/sdk
export PATH=$ANDROID_HOME/tools:$PATH
export PATH=$ANDROID_HOME/tools/bin:$PATH
export PATH=$ANDROID_HOME/platform-tools:$PATH
```

Why is it so complicated? The documentation is not clear.