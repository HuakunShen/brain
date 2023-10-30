# Common


## Scanning
### Open Port

```bash
# Confirm Open Port
nc -v huakunshen.com 80
nc -nv 192.168.1.66 80
# Scan for Open Port
nmap 192.168.1.66
nmap 192.168.1.0/24
```

### Live Hosts

```bash
nmap -sP 192.168.1.0/24
```

See [nmap](./Tools/nmap.md) for more detalis

### Find Service/Ports
```bash
ss -antp
netstat -antp
ss -antp | grep ":80 "			# which service is listening on port 80
sudo netstat -antp | grep ssh	# which port ssh is running on
```

## Reference
- [netcat](./Tools/Netcat.md)
- [nmap](./Tools/nmap.md)


