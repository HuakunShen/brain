---
title: Service Scanning
---

# nmap

Nmap: Network Mapper

`nmap <ip address>` scans the 1000 most common ports (TCP only).

## Options

- `-sV` is for scanning service version
- `-sC` is for specify nmap scripts to use
- `-p` tells namp to scan all 65545 TCP ports

## Nmap Scripts

`-sC` runs many default scripts, `--script` can be used to run a specific script.

Scripts are under `/usr/share/nmap/scripts/*`.

# Banner Grabbing

> Find the fingerprint of a service

Services usually display a banner once a connection is initiated. `namp` grabs the banners with `nmap -sV --script=banner <target>`.

## Netcat

Netcat can be used to grab banner.

```bash
nc -nv <ip address> <port>

# e.g.
nc -nv 10.0.0.1 21
nmap -sV --script=banner -p21 10.10.10.0/24 # scan a subnet with nmap
```

# Examples

## FTP

```bash
nmap -sC -sV -p21 10.0.0.10
# see if anonymous login is permitted
ftp -p 10.0.0.10 # attempt to connect
```

## SMB

```bash
nmap --script smb-os-discovery.nse -p445 10.10.10.40
# see if vulnerable to EternalBlue, Metasploit has several modules for EternalBlue

smbclient -N -L \\\\10.0.0.10 # list smb shares
smbclient \\\\10.0.0.10\\users # attempt to connect to smb
smbclient -U bob \\\\10.0.0.10\\users # connect as a user
```
