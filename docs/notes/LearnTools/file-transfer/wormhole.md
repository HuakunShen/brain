---
title: Wormhole
---

- https://magic-wormhole.readthedocs.io/en/latest/welcome.html
- https://github.com/magic-wormhole/magic-wormhole

Convenient app for sending files/folders, no need to sign in.

```bash
wormhole send <filename>
# will print wormhole receive xxx-xxx-xxx to stdout
wormhole receive xxx-xxx-xxx # receive file
```

Wormhole file transfer is based on p2p network. Data are transferred from point to point, thus could be super fast (especially if 2 computers are in the same local network).

File transfer through cloud drives has 2 steps, upload and download. Cloud is like a transfer station. In p2p network, data transfer is direct between 2 hosts.
Thus, theoretically, under exactly the same network bandwidth, p2p transfer could be at least 2x the speed of cloud drives, as cloud drives transfer data 2 times (upload and download).

In practice, things could be different, there are many factors

1. Congested network between 2 hosts in long distance transfer
   1. In long distance transfer/cross-country transfer, cloud drive companies may have more advantages as they may be using faster commercial networks. Network used by normal people may be congested.
   2. It's like the difference between local county road and highway. You upload files to local cloud drives, and cloud drives uses faster "highway" network to transfer your data to another data center.
2. Under local network or close-distance transfer, P2P is always faster. Data travels hundreds of miles to data centers and back, while local network is not usually not congested and runs at the max speed.
3. Wormhole transfers once and closes the connection, while cloud drives are "upload onces, infinite downloads". Depends on the use case, whether you need to store the data in cloud.

## Example

Under my home network (1Gb)
OneDrive runs at 25MBps, Google Drive runs at 40-80 MBps. While using wormhole to transfer files between my computers at home (ethernet cable connected) can reach 117MBps all time. Note that 125MBps is the theoretically upper limit of a 1Gbps network. My router at home operates at 1Gbps. It's at full speed. If I have a 5Gbps or 10Gbps network switch at home, I could potentially reach 1250MBps in local transfer, where it's impossible for cloud drives to reach in 2023.

## Installation

The official docs contains detailed installation instructions.

https://magic-wormhole.readthedocs.io/en/latest/welcome.html#installation

This install the original python version of wormhole.

There are also other implementations of wormhole, such as `wormhole-william`, which is a golang implementation of wormhole.
https://github.com/psanford/wormhole-william/

Also https://github.com/magic-wormhole/magic-wormhole.rs is a rust implementation of wormhole.

```bash
# install rust version
cargo install --git https://github.com/magic-wormhole/magic-wormhole.rs.git
wormhole-rs send <filename>

# install wormhole-william
go install github.com/psanford/wormhole-william@latest
wormhole-william send <filename>
```

## Conclusion

Overall, wormhole is a perfect tool for transferring files. The concept is very different from cloud drives, and are used in different scenarios.
