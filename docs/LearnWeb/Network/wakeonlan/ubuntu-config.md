---
title: Ubuntu Config
---

Read the [official doc](https://help.ubuntu.com/community/WakeOnLan).

The config doesn't persist. To make it persist after each reboot, you have to edit configuration file `/etc/network/interfaces`.

However, latest ubuntu doesn't have this file. Instead you have to edit `/etc/netplan/01-network-manager-all.yaml`.

For example,

```yaml
# Let NetworkManager manage all devices on this system
network:
  version: 2
  renderer: NetworkManager
  ethernets:
    enp6s0:
      match:
        macaddress: 12:34:56:78:90:12
      dhcp4: true
      wakeonlan: true
```