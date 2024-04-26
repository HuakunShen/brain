---
title: ufw
---


> `ufw` stands for Uncomplicated Firewall. It's like a wrapper for `iptables`, making the interaction easier.

## Rules

- `allow`: allow traffic
- `deny`: silently discard traffic
- `reject`: reject traffic and send back an error packet to the sender
- `limit`: limit connections from a specific IP address that has attempted to initiate 6 or more connections in the last 30 seconds

## Syntax

```bash
ufw [rule] [target]
ufw [rule] in [target]
ufw [rule] out [target]


```


## Sample Commands

```bash
ufw status
ufw enable

ufw status numbered
ufw delete 4  # delete rule based on rule index

ufw allow ssh
ufw allow 2222
ufw delete allow 2222

ufw allow 4422/tcp

ufw deny from 192.168.100.20


ufw reset

ufw default allow incoming
ufw default deny outgoing

ufw app list
ufw allow [App name]
ufw allow in OpenSSH
ufw limit OpenSSH

# Target Network Interface
ufw allow in on eth0 from 192.168.100.255

```




## Reference

- [Linuxize: How to List and Delete UFW Firewall Rules](https://linuxize.com/post/how-to-list-and-delete-ufw-firewall-rules/)
- [How to Configure Ubuntu Firewall with UFW](https://www.cherryservers.com/blog/how-to-configure-ubuntu-firewall-with-ufw)