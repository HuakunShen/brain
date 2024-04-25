# Bash Scripting

## ping router

```bash
ifconfig # finds your machine's ip
ping ip_address
ping -c 1 ip_address # ping once
ping -c 1 192.168.15.1 | grep "64 bytes" # see who is responding
ping -c 1 192.168.15.1 | grep "64 bytes" | cut -d " " -f 4 # extract ip
ping -c 1 192.168.15.1 | grep "64 bytes" | cut -d " " -f 4 | sed 's/.$//' # remove ':'
```



