# Service

Start a service: `service apache2 start`

Stop a service: `service apache2 stop`

Permanent service: `systemctl enable apache2`

## ssh

```bash
service ssh start # systemctl enable ssh
netstat -antp | grep ssh # tells the port ssh is running on which must be 22
```

## For Metasploit

Start service **postgresql** for faster search.

**postgresql** is the database for `msfconsole`, stores info, making running faster.

```bash
msfconsole
search smb
# enable postgresql to search faster
service postgresql start
```

```shell
# enable service permanently
systemctl enable postgresql
```



