---
title: Use ufw to block outgoing traffic
authors: [huakun]
tags: [ufw, firewall]
---

Let's say you have a local network with subnet `192.168.0.0/24`, the router is on `192.168.0.1`, you have a VM running on `192.168.0.2` (Doesn't matter here).

I want to give a teammate access to the VM but doesn't allow the VM to access any other devices under the same subnet.

VLAN is a way to do it, but too complicated and require some hardwares and softwares.

The easiest way is to rely on the VM's firewall, simply don't give sudo access to the guest user.

```bash
sudo ufw enable
sudo ufw allow out to 192.168.0.1
sudo ufw deny out to 192.168.0.0/24
```

`ufw allow out to 192.168.0.1` is for allowing traffic to router, otherwise it will not be able to connect to external network.

The `ufw deny out to 192.168.0.0/24` must be run after `ufw allow out to 192.168.0.1`, as the rules are like a chain in `iptables`, if the `deny` rule comes first, traffic to router will be blocked and the `allow` rule won't even to reached.

The `prepend` keyword can be used to move a rule's priority `ufw prepend deny out to 192.168.0.0/24`.