---
title: Lecture 2
---

Proof of Work is for solving the voting problem in a decentralized system (sybil attack). By solving some hard problem. i.e. you cannot vote unless you do some heavy work. So that sybil attack isn't cheap.

The longest chain is the valid chain.

## Prevent Double Spend Attack

Someone has very low probability to revoke the transaction to do double-spend unless she can beat the whole network on proof-of-work.

## Assumptions

and what if not hold

- Block transmission between honest nodes are reasonably fast
  - Each bitcoin block is limited to 1MB
- Block generation should be comparably slow
  - 10 minutes each block

There are forks in the system. If transmission tooo slow, longest chain is smaller than other forks.The longest chain can be beaten. Only need to beat ~20% of entire network.

## Components in Blockchain Systems

- P2P network: Propagate transaction and block info
- Distributed Consensus: determine transaction order

## P2P Network in Blockchain

- Each node connects to a number of peers (~10,000 bitcoin nodes)
  - need 32 peers in Bitcoin
- Broadcast new transaction to every node
- To join a network, know at least one of the node.
- Defense against DoS Attack
  - DoS Attack is basically flooding a network with execessive amount of messages
  - Check validity of transactions
  - Drop peers that constantly send invalid/duplicate messages

## Network Adjusted Timestamp

### Problem

How to obtain a synchronized time in Blockchain?

- Timesteamp each block/transaction
- Sync time in P2P network
- Do not trust other internet time service

## Transaction Processing Layer

How info in blockchain is organized?

### (Authenticated Read)

Suppose transactions are stored in a Merkel tree. 

### Applications of Merkel Tree

- Transactions in a block
- Unspent transactions at block height
- Account state in Ethereum


## Questioin from Last Lecture

Can you withdraw a transaction? Already brwoadcasted. 

- Control 51% of the nodes.
- unplug router cable
- Transaction is slow, will wait in a queue (pending transaction pool)
  - Create a new transaction, same input, output send to some address you control. Conflict transaction. Payer higher transaction fee to miner. Only works if lucky (~10 minutes). 
