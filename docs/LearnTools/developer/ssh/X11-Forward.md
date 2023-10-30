---
title: X11 Forward
---

X11 is a window system. [[Wikipedia: X Window System]](https://en.wikipedia.org/wiki/X_Window_System).

SSH has the option to forward UI from remote to local. Such as open server's firefox on localhost (although would be pretty slow). Forwarding terminal windows and editors, and simulation windows like ROS Viz may be practical examples.

```bash
ssh -X <user>@<server>
```

The `-X` flag enables X11 forward.

## Prerequisite

On the server side, it must also be enabled by setting `X11Forwarding yes` in `/etc/ssh/sshd_config`. Make sure you have the permission to edit the file and restart ssh service after modification.

Linux OS with X11 as the window system can run the command directly, on Mac and Windows whose window system isn't X11, extra softwares need to be installed.

- [Xming for Windows](https://sourceforge.net/projects/xming/)
- [Xquartz for MacOS](https://www.xquartz.org/)

## Usage

`ssh -X <user>@<server>` to establish connection.

Run `xclock`, `gedit` or any UI app that you know is installed on the server. A window should pop up on your local computer.

## Trusted X11 Forwarding

`-X` is untrusted. `-Y` is trusted.

In untrusted x11 forwarding, one extra step is performed before starting.

Read [What You Need to Know About X11 Forwarding](https://goteleport.com/blog/x11-forwarding/) for more details.

## Reference

- [Use X forwarding on a personal computer to securely run graphical applications installed on IU's research supercomputers](https://kb.iu.edu/d/bdnt)
- [What You Need to Know About X11 Forwarding](https://goteleport.com/blog/x11-forwarding/)
