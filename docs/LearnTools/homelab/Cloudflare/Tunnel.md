---
title: Cloudflare Tunnel
---

> Cloudflare Tunnel provides you with a secure way to connect your resources to Cloudflare without a publicly routable IP address.
>
> With Tunnel, you do not send traffic to an external IP — instead, a lightweight daemon in your infrastructure (cloudflared) creates outbound-only connections to Cloudflare’s edge. Cloudflare Tunnel can connect HTTP web servers, SSH servers, remote desktops, and other protocols safely to Cloudflare. This way, your origins can serve traffic through Cloudflare without being vulnerable to attacks that bypass Cloudflare.

[Cloudflare Tunnel Docs](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/)

## Introduction

This diagram explains how tunnels works. The logic is very simple, like a VPN, but without even need to expose a port.

![](https://developers.cloudflare.com/cloudflare-one/static/documentation/connections/connect-apps/handshake.jpg)

I usually use reverse proxy (nginx) to host services at home and expose to public internet with SSL certificate.

After trying Cloudflare Tunnel, it feels like it's on another dimension. It's so easy to set up. Simply run a docker container (one line) to run `Cloudflared`, and use Cloudflare web interface to add 2 urls.

![](https://i.imgur.com/opiGimH.png)

The first one is where you intend to expose to. The second one is the service how `Cloudflared` runner will connect to.

## Private Network
With Warp connected, you can access your private netork anywhere in the world. For example, a NAS service is hosted on 10.6.6.6, you will be able to to connect to it when connected to cloudflare with Warp.
One important thing to note: update Split Tunnels Setting [Split Tunnels · Cloudflare Zero Trust docs](https://developers.cloudflare.com/cloudflare-one/connections/connect-devices/warp/configure-warp/route-traffic/split-tunnels/#set-up-split-tunnels)
This may not be clear to understand. Basically, you need to select exclude mode, and deselect the CIDR range of your home. 
![](https://hacker-storage.s3.us-east-2.amazonaws.com/2023/3/20/c7f335ae-7e40-4de6-bc93-52d85d9fe5dd.png)

For example my I have 2 home networks, `192.168.1.0/24` and `10.6.6.0/24`. Then we have to remove `10.0.0.0/8` and `192.168.0.0/16` which are 2 supersets of my network. 
This is becasue "Exclude IPs and domains" means: "All traffic will be sent to Cloudflare Gateway except for the IPs and domains you specify."
I wasted lots of time on this, thanks to  [Securely access home network with Cloudflare Tunnel and WARP | Savjee.be](https://savjee.be/blog/securely-access-home-network-with-Cloudflare-Tunnel-and-WARP/) who gives the solution.

### Where to file the Split Tunnels Setting?
It's a little hard to find. 
Go to Cloudflare -> Zero Trust -> Settings -> WARP Client -> Device settings -> profile settings -> Configure the profile -> Split Tunnels -> Manage

## Benefit

- No need to port forward
- Traffic Analytics by Cloudflare
- Security Provided by Cloudflare
- Easy to deploy
- Work like a flexible VPN

## Reference

- https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/
- [Securely access home network with Cloudflare Tunnel and WARP | Savjee.be](https://savjee.be/blog/securely-access-home-network-with-Cloudflare-Tunnel-and-WARP/)

