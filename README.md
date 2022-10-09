# Web service for honey shop

Technologies:
- FastAPI
- PyTest

### Project architecture

![](resources/images/architecture.jpg)

### Tests

run `python -m pytest` in the root of project

### Databases

1. Redis
2. SQLite
3. PostreSQL

Let`s compare these variants. Here what I find on the websites:

#### 1. Pros of Redis:
- It’s super fast. Faster than any other cashing out there.
- Due to easy setup, Redis is Simple and easy to use.
- Redis has flexible data structures, it supports almost all data structures.
- Redis allows storing key and value pairs as large as 512 MB.
- Redis uses its own hashing mechanism called Redis Hashing.
- Zero downtime or performance impact while scaling up or down.
- Last and probably the very obvious point, it is open source and stable

####    Cons Of Redis:
- Since Data is sharded based on the hash-slots assigned to each Master. If Master holding some slots is down, data to be written to that slot will be lost.
- Clients connecting to the Redis cluster should be aware of the cluster topology, causing overhead configuration on Clients.
- Failover does not happen unless the master has at least one slave.
- It requires a huge ram because it is in-memory so are not supposed to use it on ram servers.

#### Summary: Redis is easy to use, fast and have all needed data structures but can skip some messages and require huge RAM memory on a servers.

4. Lite, good for web-application
3. Great SQL dialect
