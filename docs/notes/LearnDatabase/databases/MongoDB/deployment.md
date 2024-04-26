---
title: MongoDB Deployment
---

# Replica Set

Doing transaction in MongoDB requires a replica.
Sometimes we may want to host the replica ourselves (doing CI or loacl deployment), but can be quite compilcated.

Some docker images made it easier to deploy a replica set.

Both of the 2 images below are provided by truth-worthy organizations, and are constantly updated.

## [prismagraphql/mongo-single-replica](https://hub.docker.com/r/prismagraphql/mongo-single-replica) (100k+ Pulls)

This is found in [prisma-examples/databases/mognodb/docker-compose.yml](https://github.com/prisma/prisma-examples/blob/latest/databases/mongodb/docker-compose.yml).

This tutorial is also very useful.

The docker image has no documentation, I guess it's just used for simpliest testing and CI. Don't use it in production.

## [bitnami/mongodb](https://hub.docker.com/r/bitnami/mongodb) (1B+ Pulls)

Search for **Setting up replication**.
Step by step instructions are provided, a `docker-compose.yml` file is also provided.
