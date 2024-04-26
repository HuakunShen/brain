---
title: Clion
---

Clion is an IDE for c/c++ programming by JetBrians.

## Resources

- [Configuring Clion on Windows](https://www.jetbrains.com/help/clion/quick-tutorial-on-configuring-clion-on-windows.html#clang-cl)
- [Configuring Clion on Windows](https://www.jetbrains.com/help/clion/quick-tutorial-on-configuring-clion-on-macos.html)
- [Compilers: Configure Clion to use gcc and gdb](https://www.jetbrains.com/help/clion/how-to-switch-compilers-in-clion.html)
- [Remote Development](https://www.jetbrains.com/help/clion/remote-development.html#system-level)
  - [Clion Remote Toolchain (remote dev)](https://www.jetbrains.com/help/clion/remote-projects-support.html#remote-toolchain)
- [WSL](https://www.jetbrains.com/help/clion/how-to-use-wsl-development-environment-in-product.html#wsl-tooclhain)

## gcc in Clion

Read [Compilers: Configure Clion to use gcc and gdb](https://www.jetbrains.com/help/clion/how-to-switch-compilers-in-clion.html)

- Run `which gcc` to locate gcc command and enter that into the setting
    ![](https://hacker-storage.s3.us-east-2.amazonaws.com/2023/1/17/391bbff6-182f-41ee-9ce2-f474957d99c6.png)
- gdb isn't awailable on Mac with Arm CPU
    ![](https://hacker-storage.s3.us-east-2.amazonaws.com/2023/1/17/88bbb9a4-dbea-40c3-945f-37b15939042e.png)
- If you can see the green arrow, then you can run it
    <img src="https://hacker-storage.s3.us-east-2.amazonaws.com/2023/1/17/1766feeb-9d8b-4f4c-ba64-3a1f4a867f96.png" width="200" />
- Otherwise, edit or add a new configuration
  <img src="https://hacker-storage.s3.us-east-2.amazonaws.com/2023/1/17/e63a9697-60f1-447d-a1b2-f43670eb4e8a.png" width="300" />
- Choose the `C/C++ File` (if you don't see it, restart Clion or computer)
  <img src="https://hacker-storage.s3.us-east-2.amazonaws.com/2023/1/17/2633fca8-f66a-47b3-91b1-0587f95b05e0.png" />
- Then choose the gcc toolchain configured previously and choose the right source file
<img src="https://hacker-storage.s3.us-east-2.amazonaws.com/2023/1/17/a8eb064b-7278-4ca5-9957-1469720854c6.png" />
