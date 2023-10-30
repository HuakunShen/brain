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