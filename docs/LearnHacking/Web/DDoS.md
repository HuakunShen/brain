# DDoS Attack

## DoS (Denial of Service)

DoS is a type of cyber attack to make service/device unavailable by overwhelming or flooding the target with massive requests until normal traffic is unable to be processed.

## DDoS (Distributed Denial of Service)

DoS uses a single computer, DDoS uses many, such as [botnet](https://www.cloudflare.com/en-ca/learning/ddos/what-is-a-ddos-botnet/).

The source of attack machines can come from infected computers or [IoT devices](https://www.cloudflare.com/en-ca/learning/ddos/glossary/internet-of-things-iot/).

![](https://www.cloudflare.com/img/learning/ddos/glossary/dos-attack/dos-vs-ddos-attack.png)

## Types of Attack

Network has 7 layers, aka [OSI model](https://www.cloudflare.com/en-ca/learning/ddos/glossary/open-systems-interconnection-model-osi/).

<img src="https://cloudflare.com/img/learning/ddos/what-is-a-ddos-attack/osi-model-7-layers.svg" width="70%" style={{'background-color': 'white', 'padding': '2em'}} />

### Application Layer

<img src="https://www.cloudflare.com/img/learning/ddos/what-is-a-ddos-attack/http-flood-ddos-attack.png" width="70%" />

This is HTTP flood.

### Protocol Attacks

Targets firewalls and load balancers.

This is **SYN flood**, taking advantage of TCP handshake.

<img src="https://cloudflare.com/img/learning/ddos/what-is-a-ddos-attack/syn-flood-ddos-attack.png" width="70%" />

### Volumetric Attacks

> This category of attacks attempts to create congestion by consuming all available bandwidth between the target and the larger Internet. Large amounts of data are sent to a target by using a form of amplification or another means of creating massive traffic, such as requests from a botnet.

<img src="https://cloudflare.com/img/learning/ddos/what-is-a-ddos-attack/ntp-amplification-botnet-ddos-attack.png" width="70%" />

## Solution

- [Blackhole Routing](https://www.cloudflare.com/en-ca/learning/ddos/glossary/ddos-blackhole-routing/)
  - Like `/dev/null`, route traffic to a blackhole.
- [Rate Limiting](https://www.cloudflare.com/en-ca/rate-limiting/)
  - Limit request frequency from a from a host within a time window.
- [WAF (Web Application Firewall)](https://www.cloudflare.com/en-ca/learning/ddos/glossary/web-application-firewall-waf/)
  - Firewall as reverse proxy, protect server from malicious traffic (on the 7 network layers), by filtering requests based on rules to identify DDoS tools.

## Reference

- [Cloudflare: What is a DDoS attack?](https://www.cloudflare.com/en-ca/learning/ddos/what-is-a-ddos-attack/)
- [Cloudflare: What is denial-of-service (DoS) attack?](https://www.cloudflare.com/en-ca/learning/ddos/glossary/denial-of-service/)
- [What is a DDoS botnet?](https://www.cloudflare.com/en-ca/learning/ddos/what-is-a-ddos-botnet/)
- [DNS amplification](https://www.cloudflare.com/en-ca/learning/ddos/dns-amplification-ddos-attack/)
