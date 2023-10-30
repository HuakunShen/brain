---
title: Cloudflare DDNS
---

> If you don't have a static IP, [DDNS](https://en.wikipedia.org/wiki/Dynamic_DNS) can save you by keeping a domain name pointing to your IP address even if IP address constantly updates.



## Methods

### TrueNAS Scale + Truecharts Cloudflare DDNS

Read

- https://truecharts.org/charts/stable/cloudflareddns/setup-guide/
- https://hotio.dev/containers/cloudflareddns/

The 2 documents should be enough to get it running, while there may be a little bit confusion on parameter naming.

Under Cloudflareddns Configuration,

- **CF API Key**: the **Global API Key** you can get from "Cloudflare -> My Profile -> API Tokens -> API Keys -> GLobal API Key"
    - You can also choose to create token on the same page following the [Charts](https://truecharts.org/charts/stable/cloudflareddns/setup-guide/) tutorial
- CF User: Cloudflare email
- CF API Token: See [Charts Doc](https://truecharts.org/charts/stable/cloudflareddns/setup-guide/), generate a zone-specific token
- CF API Token Zone: Go to the zone (base domain) Get the Zone ID from right hand side (API/Zone ID)
- In **Hosts, Zones and Record Types**, click **Add**
    - Domain is the the domain name you want to use
    - Zone is the base domain
        - If domain is `a.example.com` then Zone is `example.com`
    - Record Type: Use `A` if you have IPV4 and `AAAA` fpr IPV6
