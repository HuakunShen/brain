## Assumptions
- only a small fraction of nodes are Byzantine
- Use votes to form quorums of supermajority to defend against Byzantine failures.

## Basic Idea
- Node Identity: Each node has private/public keys to sign messages
- Everyone knows others' public key and can verify
- Primary: the leader node that drives the consensus
- Normal Case: Primary forwards requests to all nodes. Each node collecte 2f+1 votes from others and process requests.
- Why 2f+1 quorum
	- 2f+1 quorums must have f+1 overlapping nodes
- If only wait for majority >50%?

## View Change
- View change commit point: when 2f+1 replicas initiate view change
- Handle malicious primary case
- $O(N^2)$ messages in a view change. 
- Each view change message collects up to $O(N)$ certificates
- $O(N^3)$ data to transmit in total.

## Normal Case
- All to all messages in each round, $O(N^2)$ messages.



## Comparison Between Consensus
### Nakamoto Consensus
- Tolerate up to 50% malicious
- Permission-less
- Strong against DDoS
- Not partition tolerant
- Slow ~10tx/s
- Scale 10-100k full nodes

### PBFT
- Tolerate 1/3 malicious nodes
- Permissioned (not open for everyone to join network)
- Partition tolerant
- Weak against DDoS
- Fast, thousands of tx/s
- Not Scalable, dozens of nodes







