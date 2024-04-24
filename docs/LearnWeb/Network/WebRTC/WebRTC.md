---
title: WebRTC
---

- [Terminology](#terminology)
- [Procedures](#procedures)
  - [Stage 1](#stage-1)
    - [Sender Side](#sender-side)
    - [Receiver Side](#receiver-side)
  - [Stage 2](#stage-2)
- [Data Channels](#data-channels)
- [Reference](#reference)

Peer to Peer connection. Connection established using a third party server but real data is only between 2 peers.

## Terminology

- **Peer Connection**: Connection between 2 peers.
- **ICE**: Interactive Connectivity Establishment. Protocol used to establish connection between 2 peers.
  - > In order to discover how two peers can connect, both clients need to provide an ICE Server configuration. This is either a STUN or a TURN-server, and their role is to provide ICE candidates to each client which is then transferred to the remote peer. This transferring of ICE candidates is commonly called signaling.
- **ICE candidates**: Information about how to connect to a peer.
- **STUN**: Session Traversal Utilities for NAT. Protocol used to find public IP address of a peer.
- **TURN**: Traversal Using Relays around NAT. Protocol used to relay data between 2 peers.
- **SDP Offer**: Session Description Protocol. Description of the media that a peer wants to send or receive.

## Procedures

Each peer connection is handled by a `RTCPeerConnection` object, which takes in a `RTCConfiguration` object. `RTCConfiguration` object contains the ICE servers that the peers will use to establish a connection.

### Stage 1

#### Sender Side

1. Create a `RTCPeerConnection` object.
2. Sender creates SDP offer
   1. Call `createOffer()` on the `RTCPeerConnection` object to create a `RTCSessionDescription` object, which is set as the **local description** using `setLocalDescription()`.
3. Set up a listener waiting for answer from the receiver

   ```js
   async function makeCall() {
     const configuration = {
       iceServers: [{ urls: "stun:stun.l.google.com:19302" }],
     }; // RTCConfiguration
     const peerConnection = new RTCPeerConnection(configuration);
     signalingChannel.addEventListener("message", async (message) => {
       // listen for answer from receiver
       if (message.answer) {
         const remoteDesc = new RTCSessionDescription(message.answer);
         await peerConnection.setRemoteDescription(remoteDesc);
       }
     });
     const offer = await peerConnection.createOffer(); // RTCSessionDescription
     await peerConnection.setLocalDescription(offer);
     signalingChannel.send({ offer: offer });
   }
   ```

4. Sender sends SDP offer to receiver (using a signaling server)

#### Receiver Side

1. Wait for an incoming offer **before** we create our `RTCPeerConnection` instance
2. Once offer received, use `setRemoteDescription()` to set the remote description
   1. This offer is the "local description" of the sender, but the "remote description" of the receiver
3. Call `createAnswer()` to create an answer to the offer
4. `setLocalDescription()` to set the local description
5. Send the answer to the sender through signaling server

   ```js
   const peerConnection = new RTCPeerConnection(configuration);
   signalingChannel.addEventListener("message", async (message) => {
     if (message.offer) {
       // received offer from sender
       peerConnection.setRemoteDescription(
         new RTCSessionDescription(message.offer)
       );
       const answer = await peerConnection.createAnswer();
       await peerConnection.setLocalDescription(answer);
       signalingChannel.send({ answer: answer });
     }
   });
   ```

### Stage 2

Stage 1 is not ready yet. We need to collect the ICE candidates at each peer and transfer (over the signaling channel) to the other peer. Without ICE candidates, the peers don't know how to connect to each other, they need to exchange connectivity information. ICE candidates are obtained from STUN or TURN servers.

Once a RTCPeerConnection object is created, the underlying framework uses the provided ICE servers to gather candidates for connectivity establishment (ICE candidates).

*This is automatic.*

State of ICE gathering: new, gathering or complete

Add a listener for `icecandidate` event on the `RTCPeerConnection` object

```js
// Listen for local ICE candidates on the local RTCPeerConnection
peerConnection.addEventListener('icecandidate', event => {
    if (event.candidate) {
        signalingChannel.send({'new-ice-candidate': event.candidate});
    }
});

// Listen for remote ICE candidates and add them to the local RTCPeerConnection
signalingChannel.addEventListener('message', async message => {
    if (message.iceCandidate) {
        try {
            await peerConnection.addIceCandidate(message.iceCandidate);
        } catch (e) {
            console.error('Error adding received ice candidate', e);
        }
    }
});
```

Once the ICE candidates are exchanged, the peers can establish a connection. The connection state can be checked using the `connectionState` property of the `RTCPeerConnection` object.

```js
// Listen for connectionstatechange on the local RTCPeerConnection
peerConnection.addEventListener('connectionstatechange', event => {
    if (peerConnection.connectionState === 'connected') {
        // Peers connected!
    }
});
```

## Data Channels

```js
const peerConnection = new RTCPeerConnection(configuration);
const dataChannel = peerConnection.createDataChannel();

// Enable textarea and button when opened
dataChannel.addEventListener('open', event => {
    // Do some UI update here such as enabling the textarea and send button
});

// Disable input when closed
dataChannel.addEventListener('close', event => {
    // Do some UI update here such as disabling the textarea and send button
});
```

To send data:

```js
dataChannel.send(message);

// Listen for messages from the remote peer
dataChannel.addEventListener('message', event => {
    const message = event.data;
});
```


## Reference

- [# WebRTC in 100 Seconds // Build a Video Chat app from Scratch](https://youtu.be/WmR9IMUD_CY)
- [MDN web docs RTCPeerConnection](https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection)
- [Guide: Getting Started](https://webrtc.org/getting-started/peer-connections)


