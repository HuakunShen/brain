---
title: ssh
---

## Introduction

SSH is probably the most used tool that most developers need.

[SSH](https://en.wikipedia.org/wiki/Secure_Shell) means secure shell.
It's a cryptographic network protocol for operating network services.

It's used everywhere, here is a list of things it's capable of

- Remote control a computer with command line
- SSH tunnel to forward ports from remote server to `localhost` or vice versa
  - Gives user secure connection over unsecure network
- Forward UI with X11
  - e.g. display a GUI linux app on Mac or Windows.

:::tip
Search for ssh on this website, I have plenty of notes about SSH on all sorts of weird topics
:::

## TL;DR

```bash
ssh <username>@<server>  # most basic
# or
ssh -l <username> <server> # -l for username

# then enter password to login
```

### Key-Based Password-less Authentication

```bash
# on local computer
ssh-keygen # keep pressing enter
# id_rsa and id_rsa.pub are generated in ~/.ssh

# ssh-keygen -t ed25519 uses another algorithem, it's better
# id_ed25519 and id_ed25519.pub are generated instead

cat ~/.ssh/id_rsa.pub     # to get the content of public key, copy it to clipboard
# ========================================================================
# Mac and Linux ships with ssh-copy-id
# ========================================================================
ssh-copy-id -i ~/.ssh/id_rsa <username>@<server>

# ========================================================================
# Or you can do it manually if you don't have ssh-copy-ip (e.g. on windows)
# ========================================================================
ssh <username>@<server>   # login to server

mkdir ~/.ssh
echo <paste public key here> >> authorized_keys

# Ctrl + D to quit ssh session
ssh <username>@<server>   # ssh again, no password required
```

### Identity File

```bash
ssh <username>@<server> -i ~/.ssh/id_rsa
# or
ssh <username>@<server> -i ~/.ssh/id_ed25519
# or any custom identity file name
```

### SSH Config

Mac or Linux: `~/.ssh/config`

Windows: `C:\Users\<username>\.ssh\config`

Append the remote server config

```
Host custom_name
  HostName <server domain or IP>
  User my_username
  IdentityFile ~/.ssh/id_ed25519
```

Then

```bash
ssh custom_name
```

to connect (no password required).

### X11 Forward

```bash
ssh -X <username>@<server>  # untrusted
ssh -Y <username>@<server>  # trusted
```

### SSH Tunnel

> It's a tunnel for network traffic between 2 computers.

It's too complicated to explain without examples. See [SSH Tunnel](./SSH-Tunnel).

#### Remote Forward

```bash
ssh -R <remote port>:localhost:<localhost port> <REMOTE_USER>@<REMOTE_HOST>
```

#### Local Forward

```bash
ssh -L <remote port>:localhost:<localhost port> <REMOTE_USER>@<REMOTE_HOST>
```

## Remote Connection

The most common use case of `ssh` is remote connection. It allows you to remotely connect a computer using command line. The computer can have any operating system (Mac, Linux or Windows), as long as it has a [openssh-server](https://ubuntu.com/server/docs/service-openssh) running.

### Basic Usage

Mac, Linux and Windows (powershell) should all come with ssh client, no need to install.

```bash
ssh <username>@<host>  # most basic connection to control a computer
# then enter password
```

The host can be a domain (e.g. server.huakun.tech), or an IP address (i.e. 192.168.1.10).

### Passwordless Login

Login without password can be achieved with key-based authentication. Instead of using password, we use ssh key to login.

This method is also used for git cloning with ssh key. (git urls starts with `git@github.com/...`).

Read more at [ssh-keygen](https://www.ssh.com/academy/ssh/keygen) and [GitHub SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).

```bash
ssh-keygen -t ed25519 # then press enter multiple times until a key is created
# don't enter password if you want password-less auth
```

2 files are generated in `~/.ssh` folder. `id_ed25519` and `id_ed25519.pub`.

The one with `.pub` extension is a public key.

The overall idea is, add the public key to remote server (which you want to authenticate to), then use private key to authenticate. This is called [Asymmetric Encryption](https://cheapsslsecurity.com/blog/what-is-asymmetric-encryption-understand-with-simple-examples/). I will talk about this in another note. (TODO).

The public key can be exposed, but the private key must be kept private. Whoever with your private key can access the resource you can access without password.

Now you want to transfer the public key to remote server.

```bash
cat ~/.ssh/id_ed25519.pub # then copy the content
ssh <username>@<host>     # ssh into the server with password
cd $HOME                  # cd into home directory if you are not in it
mkdir .ssh                # make .ssh directory (by default it's doesn't exist)
echo '<the public key>' >> authorized_keys # append your public key to a file
```

`authorized_keys` is the key point. You can have multiple public key in this file (each on a new line). Each key represents a computer that can access the target.

:::caution
If the remote server is a Windows machine and the remote user is an administrator, `.ssh/authorized_keys` may not work. Instead, use `C:\ProgramData\ssh\administrators_authorized_keys`.

See https://superuser.com/questions/1342411/setting-ssh-keys-on-windows-10-openssh-server
:::

:::caution
Use `>>` to append to the file. Don't use `>` which could accidentally overwrite an existing `authorized_keys` file.

It's also fine to edit the file using editors like `vim` or `nano`.
:::

Then log out of the server and try again, you should not need to enter password.

#### Note

- `ssh-copy-id` is a command for automating the public key uploading process.
- Password Login can be completely disabled (use key auth only) for better security
  - `sudo vi /etc/ssh/sshd_config`
  - Set `PasswordAuthentication no`

https://www.ssh.com/academy/ssh/copy-id

### Identity File

The ssh keys are also called identity files, which can be used to identify an authorized client. You can have multiple identity file (ssh keys) in `~/.ssh`, or any folder, with custom names.

Then during ssh, your ssh client could use the wrong ssh key. Use `-i` to specify the identity file you want to use.

```bash
ssh -i ~/.ssh/custom_key <username>@<host>
```

Note that the identity file used should be the private key (not the one with `.pub`).

### ssh config file

It's possible to make things even simpler using a config file.

Example: `ssh server_name`. Without username, ip address or identity file.

Edit `~/.ssh/config` with any editor. On windows, it's `C:\Users\<username>\.ssh\config`.

```
Host any_name
  HostName server.huakun.tech
  User my_username
  IdentityFile ~/.ssh/id_ed25519
```

This is a simple sample config.

Then you can `ssh any_name` to ssh to the server, without needing to enter password or username or anything.

<details>
<summary>More Advanced Discussion</summary>

There are more options, like `ProxyCommand` allows you to use socks 5 VPN proxy, for VPNs that are not running in Network layer or Data Link Layer (layer 3 and 2 in [OSI model](https://www.imperva.com/learn/application-security/osi-model/)). This will be discussed in another note (TODO) where I will discuss networks and VPN in more details.

Basically, VPNs that operate in higher layers (e.g. [Shadowsocks](https://shadowsocks.org/) runs in [layer 5, session layer](https://baihuqian.github.io/2020-06-09-gfw-a-technical-analysis/#shadowsocks)) can only proxy traffic for higher-layer traffic like [HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) which runs in Application Layer (layer 7).

OpenVPN operates in Layer 3 (Network Layer) by default, and can be configured to operate on Layer 2 (Data Link Layer), and can automatically route ssh traffic.

SSH operates in layer 4 - 7 (transport to appliaction layer). VPNs in lower layers can proxy SSH traffic. [[SSH Wikipedia]](https://en.wikipedia.org/wiki/Secure_Shell)

Read more at [Some basic networking concepts simplified (Search for 'layer')](https://openvpn.net/vpn-server-resources/some-basic-networking-concepts-simplified/).

**Don't worry about the OSI and VPN related stuff for now, those are more advanced topics.**

</details>

Read more at [Linuxize: ssh config file](https://linuxize.com/post/using-the-ssh-config-file/).

## SSH Tunnel

Port binding/forwarding between 2 computers.

See [SSH Tunnel Notes](./SSH-Tunnel).

## SSH X11 Forward

Allows you Forward UI from remote to local computer.

See [SSH X11 Forward](./X11-Forward).

## Reference

- [Ubuntu: Service OpenSSH](https://ubuntu.com/server/docs/service-openssh)
- [My Video Talking about ssh and port forwarding with raspberry pi](../../../../videos/Other/ssh)
  - The videos talks about raspberry pi, but a pi is just like any regular computer. The process is exactly the same.
- [Known Host Issue](../../../../videos/HomeLab/ssh-known-host)
- [SSH with VSCode (fix permission)](../../../../videos/HomeLab/ssh-vscode-permission)
- [ssh-keygen](https://www.ssh.com/academy/ssh/keygen)
- [GitHub SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
- [Linuxize: ssh config file](https://linuxize.com/post/using-the-ssh-config-file/)
- [GFW, a Technical Analysis (osi layer 5)](https://baihuqian.github.io/2020-06-09-gfw-a-technical-analysis/#shadowsocks)
- [Some basic networking concepts simplified (Search for 'layer')](https://openvpn.net/vpn-server-resources/some-basic-networking-concepts-simplified/)
- [SSH Wikipedia](https://en.wikipedia.org/wiki/Secure_Shell)
- [The Art of SSH](https://medium.com/@aele54/the-art-of-ssh-57221226d64b)
- [SSH Tunneling](https://www.ssh.com/academy/ssh/tunneling)
  - [SSH Tunneling: Example](https://www.ssh.com/academy/ssh/tunneling-example)
