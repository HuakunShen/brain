# NMAP Stage Scanning

```bash
# TCP Scan
sudo nmap -vv -Pn -A -sS -T4 -p- -oN ~/Desktop/tcpscan.txt 10.0.2.15

# UDP Scan
sudo nmap -vv -Pn -A -sU -T4 --top-ports 200 -oN ~/Desktop/udpscan.txt huakunshen.com
sudo nmap -Pn -sU --top-ports 1000 --stats-every 3m --max-retries 1 -T3 -oN ~/Desktop/udpscan.txt huakunshen.com
```

## NMAP scripts

Scripts are in `/usr/share/nmap/scripts`

## Scan Open Ports/Services

```bash
nmap <ip>
```

## Scan Live Hosts in a subnet

```bash
nmap -sP 192.168.1.0/24
```

## Scan Live Hosts and Open Ports/Services in subnet

```bash
nmap 192.168.1.0/24
```

## Tips

- ttl can be used to identify the OS of the target, linux ttl is 64, windows ttl is 128
- When scanning "filtered" port (not sure open or close) with TCP SYN packet, we can get info from duration
  - Shorter duration like 0.05 sec could mean firewall rejects the packet
- To get hostname, the -sV is helpful. It scans for service versions and takes longer.

## UDP Scan

- UDP protocol doesn't have handshake, requires a longer timeout, scanning it requires more time
- UDP service may to respond to the scan


## Saving Results

- Normal output: `-oN`, `.nmap`
- Grepable output: `-oG`, `.gnmap`
- XML output: `-oX`, `.xml`
- All formats: `-oA`, `.nmap`, `.gnmap`, `.xml`




## References

- https://nmap.org/book/man-port-scanning-techniques.html
