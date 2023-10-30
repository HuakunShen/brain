# Proxy

## Forward Proxy

### Purpose

- Enforce browsing restrictions (e.g. block websites)
- Block/Filter content
- Hide Identity

<img src="https://www.cloudflare.com/img/learning/cdn/glossary/reverse-proxy/forward-proxy-flow.svg" style={{'background-color': 'white', 'padding': '2em'}} />

## Reverse Proxy

> Reverse Proxy hides backend applications and forwards client requests to the applications.

### Benefits

> Increase scalability, performance, resilience and security

- Load Balancing
  - Direct traffic to difference servers behind the proxy to distribute traffic
- Aggregate backend services
  - There is a single entrypoint for accessing the backend, instead of exposing all microservices.
  - This is more secure, exposing only one service. Single point to defend against attacks suck as [DDoS attack](../../LearnHacking/Web/DDoS)
- [Global Server Load Balancing](https://www.cloudflare.com/learning/cdn/glossary/global-server-load-balancing-gslb/)
  - Load Balancing across the globe
- Caching
- SSL Encryption
  - Read [My Notes on Web App Deployment with Nginx as Reverse Proxy](../../LearnWeb/deployment)

<img src="https://www.cloudflare.com/img/learning/cdn/glossary/reverse-proxy/reverse-proxy-flow.svg" style={{'background-color': 'white', 'padding': '2em'}} />

## Reference

- [Cloudflare Reverse Proxy](https://www.cloudflare.com/en-ca/learning/cdn/glossary/reverse-proxy/)
