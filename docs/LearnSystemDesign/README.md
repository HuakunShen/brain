# System Design

| Name                       | URL                                                 | Description                                                                                      |
| -------------------------- | --------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| System Design Primer       | https://github.com/donnemartin/system-design-primer | A 200k Stars repo with System Design Notes, not too detailed, but covers a lot of stuff          |
| Cloudflare Learning Center | https://www.cloudflare.com/en-ca/learning/          | Cloudflare is a perfect source to learn system design, they have so many free info in their docs |

## Topics

- Cache
  - [Cloudflare](https://www.cloudflare.com/en-ca/learning/cdn/what-is-caching/)
- CDN
- DNS
- Load Balancer
- Reverse Proxy
- Database
- Asynchronism
  - Message Queues
  - Task Queues
  - Back Pressure
- Security
- Protocols
- Deployment
  - Read [Web App Deployment](../LearnWeb/deployment.mdx) for web app deployment methods

## How to Approach a System Design Interview Question

1. Outline use cases, constraints, assumptions
   - Who is client?
   - How many client?
   - How are clients using it?
   - How much data?
   - How many requests per second?
   - Read/Write Ratio
2. Create the high-level design
   - Sketch the main components and connections
3. Design core components
4. Scale the design
   - Load Balancer
   - Horizontal Scaling
   - Caching
   - Database Sharding
