---
title: Redis
---

[Redis](https://redis.io/)
> The open source, in-memory data store used by millions of developers as a database, cache, streaming engine, and message broker.

## Use Cases

### 1. Cache
For frequently accessed data, store in redis to reduce load on persistant database and improve response time of application (e.g. web server).

### 2. Session Store
Share session data among stateless servers. 
Session-based authentication has a drawback. When a user connects to another server instance, the user will be asked to login again as the other server doesn't have login session data in memory, making servers non-stateless. JWT based token authentication doesn't have this issue as servers don't store any data; instead user sends a token with required information (payload) with cryptography to prove the credibility of the token.
Redis can be used as a global variable to contain all session data from all web server instances.

### 3. Distributed Lock
Like mutex. In a distributed syste, when multiple instances want to access a shared mutable resource, Redis can be used as a mutex lock. Instances need to acquire the lock before making changes, and release the lock once finished. 
There are many existing distributed lock libraries for redis. 

### 4. Rate Limiter
Limit how frequent user can send requests to server to prevent DoS attack and robots. 
For a time window (e.g. 1 minute), each request will increment a counter in redis by 1. If the number of request is below the allowed value, then keep going, reject request with [Status Code: 429 Too Many Requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) otherwise. 
The key has a TTL (time to live) of 1 minute. A counter is created if a counter for the user doesn't already exist. 
Implementation of this can be done in web server middleware, such as [express-rate-limit - npm (npmjs.com)](https://www.npmjs.com/package/express-rate-limit)

### 5. Leaderboard
Gaming Leaderboard. 

### 6. Publisher Subscriber for Distributed Syncing
[Example: Socketio Redis Adapter](https://socket.io/docs/v4/redis-adapter/)
SocketIO is a popular library to websocket (realtime syncing). For example it can be used to build a realtime message app. When a user sends a message, server broadcast to everyone else in the chat room. However, in a distributed system where users in the same room may connect to different servers, how to achieve syncing/broadcasting?
Redis has a [publisher subscriber mechanism](https://redis.io/docs/manual/pubsub/) that can be used to sync data across servers with socketio. When user A sends a message to room **R** to server A, server A will make a broadcast to room **R** while also publish this message to redis. Other SocketIO instances receive this message and broadcast to room **R** users connected to them. For example, user B connected to server B will also receive the message from user A.




## Reference
- [Top 5 Redis Use Cases](https://youtu.be/a4yX7RUgTxI)






