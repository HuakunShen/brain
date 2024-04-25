# Network

- [Network](#network)
  - [Get Listening Ports and Application Name](#get-listening-ports-and-application-name)
    - [Windows](#windows)
    - [Linux](#linux)
    - [MacOS](#macos)


## Get Listening Ports and Application Name

### Windows

```powershell
netstat -ano                    # List all network info, including PID and port        
tasklist /FI "PID eq 5932"      # Get application name by PID (here assume PID is 5932)
```

### Linux

```bash
netstat -anpe | grep "1234" | grep "LISTEN"
```

### MacOS

