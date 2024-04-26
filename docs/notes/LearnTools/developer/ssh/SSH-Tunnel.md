---
title: SSH Tuneling
---

> It's a tunnel for network traffic between 2 computers.

Read `man ssh` for more details.

## Local Fowarding

> Forward a port from the client machine to the server machine
>
> Traffic to client to will redirected to server.

```bash
ssh -L <remote port>:localhost:<localhost port> <REMOTE_USER>@<REMOTE_HOST>

# sample
ssh -L 9090:localhost:8080 user@server
```

The command above forwards `localhost:9090` to `server:8080`.

Suppose I have a file server running on `http://server:8080`, I can now access the web page on `http://localhost:9090`.

### Jupyter Notebook Example

[Running Jupyter Notebook on a remote server](https://docs.anaconda.com/anaconda/user-guide/tasks/remote-jupyter-notebook/) is a perfect sample use case.

Suppose you are running a jupyter notebook server at home (on port 8080) and want to access it remotely from outside your home.

Let's say your home has a domain called `home.com`. If you do port forwarding and expose port 8080 for the jupyter notebook service. You can access it from outside home on `http://home.com:8080`.

Jupyter Notebook itself runs on http. This is dangerous as http traffic isn't encrypted. Your data can be seen by others easily.

To configure https for better security, you may need a reverse proxy server and setup SSL certificate, which is complicated.

Suppose you can ssh into your server with `ssh user@home.com` (assume port forwarding on router is already set up). Then

```bash
ssh -L 8080:localhost:9090 user@home.com
```

allows you to access the jupyter notebook web ui on `http://localhost:9090`. Although it's still http protocol. The traffic between you and your server is encrypted with SSH tunnel, http (unencrypted) traffic is only running on your local computer (localhost), it's secure.

### VNC Server Example

[How to Establish VNC Connection Over SSH tunnel in Ubuntu 20.04](https://serverspace.io/support/help/vnc-connection-ssh-tunnel-ubuntu-20-04/)

VNC is a protocol for remote desktop. Suppose the VNC server is running on port 5901.

Accessing VNC without encryption is dangerous. 

```bash
ssh -L 61000:localhost:5901 -N username@VNC_server_IP
```

Now you can remote control your VNC server with `vnc://localhost:61000` securely. Although there may be a warning telling you the traffic isn't encrypted, that's fine because you know the traffic is transmitted through SSH tunnel.

### RDP Example

Another example similar to VNC is RDP (remote desktop protocol). Mainly used by Microsoft, available on Windows, but also adopted by Ubuntu 22.04 as the main remote control protocol. It's better than VNC in my opinion, much smoother.

```bash
ssh -L 33389:localhost:3389 user@server
```

Then `rdesktop localhost:33389` to connect.

## Remote Fowarding

Forward server traffic to client.

Suppose client is localhost, in a private network. Server is remote host, exposed to public internet (where everyone can access).

```bash
ssh -R 9090:localhost:8080 user@server
```

The command above forwards traffic from `server:9090` to `localhost:8080`.

So, if I have a http server running on `localhost:8080`, people can access the service by accessing `http://server:9090`. This hides my `localhost` from public internet.

In other words, when someone access `http://server:9090` using a browser, the traffic is routed to `localhost:8080`, and the response back to server, and then back to the client (user who is accessing `http://server:9090`).

## Notes

- Use `-N` flag to **specifies to only forward ports, not execute the command**. Try it to see the difference.

## Reference

- [SSH Tunneling](https://www.ssh.com/academy/ssh/tunneling)
  - [SSH Tunneling: Example](https://www.ssh.com/academy/ssh/tunneling-example)
- [Running Jupyter Notebook on a remote server](https://docs.anaconda.com/anaconda/user-guide/tasks/remote-jupyter-notebook/)
- [How to Establish VNC Connection Over SSH tunnel in Ubuntu 20.04](https://serverspace.io/support/help/vnc-connection-ssh-tunnel-ubuntu-20-04/)


## Related Topics

- [Cloudflare Tunnel](../../../LearnTools/homelab/Cloudflare/Tunnel)
  - Makes tunneling much much simpler