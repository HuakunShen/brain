---
title: Magic Wormhole Source Code Analysis
authors: huakun
tags: [python, file transfer]
---

## Clients

1. Python: https://github.com/magic-wormhole/magic-wormhole (official, original)
2. Rust: https://github.com/magic-wormhole/magic-wormhole.rs (official)
3. Golang: https://github.com/psanford/wormhole-william.git (non-official)
4. Golang + Fyne GUI Client: https://github.com/Jacalz/rymdport
5. Rust + Tauri GUI Client: https://github.com/HuakunShen/wormhole-gui

## Documentation

- https://github.com/magic-wormhole/magic-wormhole-protocols
- https://magic-wormhole.readthedocs.io/en/latest/

## Performance

magic-wormhole can almost always eat the full bandwidth of the network. It's very fast. However, I have observed performance issue on Mac (M1 pro) during sending (not receiving).

See update on issue https://github.com/magic-wormhole/magic-wormhole.rs/issues/224

| Sender Computer  | Sender Client | Receiver Computer | Receiver Client | Speed   |
| ---------------- | ------------- | ----------------- | --------------- | ------- |
| M1 pro Mac       | python        | Ubuntu i7 13700K  | python          | 112MB/s |
| M1 pro Mac       | rust          | Ubuntu i7 13700K  | python          | 73MB/s  |
| M1 pro Mac       | golang        | Ubuntu i7 13700K  | python          | 117MB/s |
| Ubuntu i7 13700K | python        | M1 pro Mac        | python          | 115MB/s |
| Ubuntu i7 13700K | rust          | M1 pro Mac        | python          | 116MB/s |
| Ubuntu i7 13700K | golang        | M1 pro Mac        | python          | 117MB/s |
| Ubuntu i7 13700K | python        | Kali VM (on Mac)  | python          | 119MB/s |
| Kali VM (on Mac) | python        | Ubuntu i7 13700K  | python          | 30MB/s  |
| Ubuntu i7 11800H | rust          | Ubuntu i7 13700K  | python          | 116MB/s |
| Ubuntu i7 13700K | rust          | Ubuntu i7 11800H  | python          | 116MB/s |

It seems like there is some performance issue with the rust implementation on the sender side.

## Workflow

I read the client source code written in Python, Golang and Rust. The Python code is unreadable to me. Some packages like `automat` and `twisted` are used. I am not familiar with them and they make the code hard to read or follow. It even took me ~20-30 minutes to find the main function and get the debugger running. The code is not well-organized. It's hard to follow the workflow.

Rust is known for its complexity. It's `async` and `await` makes debugger jump everywhere. Variables allocated in heap are hard to track with debugger. Usually only a pointer address is shown.

The Golang version (although non-official) is the easiest to follow. Project structure is clear and simple. Goland's debugger works well. So let's follow the Golang version.

- After command arguments parsing, everything starts here [`sendFile(args[0])`](https://github.com/psanford/wormhole-william/blob/68dc3447a8585b060fb1e6836a23847700ab9207/cmd/send.go#L48)

- A `wormhole.Client` is created [`c := newClient()`](https://github.com/psanford/wormhole-william/blob/68dc3447a8585b060fb1e6836a23847700ab9207/cmd/send.go#L117)

- The `code` is retrieved from [`code, status, err := c.SendFile(ctx, filepath.Base(filename), f, args...)`](https://github.com/psanford/wormhole-william/blob/68dc3447a8585b060fb1e6836a23847700ab9207/cmd/send.go#L142)

  - `status` is a channel (`var status chan wormhole.SendResult`) that waits for the result of sending file.
  - ```go
        s := <-status

        if s.OK {
            fmt.Println("file sent")
        } else {
            bail("Send error: %s", s.Error)
        }

    ```

- Here is [Wormhole Client's `SendFile()` method](https://github.com/psanford/wormhole-william/blob/68dc3447a8585b060fb1e6836a23847700ab9207/wormhole/send.go#L445)

  - ```go
        func (c *Client) SendFile(ctx context.Context, fileName string, r io.ReadSeeker, opts ...SendOption) (string, chan SendResult, error) {
            if err := c.validateRelayAddr(); err != nil {
                return "", nil, fmt.Errorf("invalid TransitRelayAddress: %s", err)
            }

            size, err := readSeekerSize(r)
            if err != nil {
                return "", nil, err
            }

            offer := &offerMsg{
                File: &offerFile{
                    FileName: fileName,
                    FileSize: size,
                },
            }

            return c.sendFileDirectory(ctx, offer, r, opts...)
        }
    ```

  - `offer` contains the file name and size.

  -

- Let's go into `sendFileDirectory()` method [here](https://github.com/psanford/wormhole-william/blob/68dc3447a8585b060fb1e6836a23847700ab9207/wormhole/send.go#L187). Everything happens here.

  - `sideId`: RandSideID returns a string appropate for use as the Side ID for a client.

    > NewClient returns a Rendezvous client. URL is the websocket url of Rendezvous server. `SideID` is the id for the client to use to distinguish messages in a mailbox from the other client. AppID is the application identity string of the client.

    > Two clients can only communicate if they have the same AppID.

    ```go
    sideID := crypto.RandSideID()
    appID := c.appID()
    rc := rendezvous.NewClient(c.url(), sideID, appID)

    _, err := rc.Connect(ctx)
    ```

  - Then a nameplate is generated

    If users provides the code, the mailbox is attached to the code. Otherwise, a new mailbox is created. A mailbox is a channel for communication between two clients. The sender creates a mailbox and sends the code (address of mailbox + key) to the receiver. The receiver uses the code to open the mailbox.

    ```go
    if options.code == "" {
      // CreateMailbox allocates a nameplate, claims it, and then opens the associated mailbox. It returns the nameplate id string.
      // nameplate is a number string. e.g. 10
      nameplate, err := rc.CreateMailbox(ctx)
      if err != nil {
        return "", nil, err
      }

      // ChooseWords returns 2 words from the wordlist. (e.g. "correct-horse")
      pwStr = nameplate + "-" + wordlist.ChooseWords(c.wordCount())
    } else {
      pwStr = options.code
      nameplate, err := nameplateFromCode(pwStr)
      if err != nil {
        return "", nil, err
      }

      // AttachMailbox opens an existing mailbox and releases the associated nameplate.
      err = rc.AttachMailbox(ctx, nameplate)
      if err != nil {
        return "", nil, err
      }
    }
    ```

  - Then a `clientProto` is created

    ```go
      clientProto := newClientProtocol(ctx, rc, sideID, appID)
    ```

    `appID` is a constant string. `sideID` is a random string.

    `sideID := crypto.RandSideID()` RandSideID returns a string appropate for use as the Side ID for a client.

    Let's see how `newClientProtocol` works.

    ```go
      type clientProtocol struct {
        sharedKey    []byte
        phaseCounter int
        ch           <-chan rendezvous.MailboxEvent
        rc           *rendezvous.Client
        spake        *gospake2.SPAKE2
        sideID       string
        appID        string
      }

      func newClientProtocol(ctx context.Context, rc *rendezvous.Client, sideID, appID string) *clientProtocol {
        recvChan := rc.MsgChan(ctx)

        return &clientProtocol{
          ch:     recvChan,
          rc:     rc,
          sideID: sideID,
          appID:  appID,
        }
      }
    ```

  - Then enter a go routing (transfer happens here)

    - [`clinetProto.ReadPake(ctx)`](https://github.com/psanford/wormhole-william/blob/68dc3447a8585b060fb1e6836a23847700ab9207/wormhole/send.go#L260): block and waiting for receiver to connect (wait for receiver to enter the code)

      `ReadPake` calls `readPlainText` to read the event from the mailbox.

      ```go
      func (cc *clientProtocol) readPlaintext(ctx context.Context, phase string, v interface{}) error {
        var gotMsg rendezvous.MailboxEvent
        select {
        case gotMsg = <-cc.ch:
        case <-ctx.Done():
          return ctx.Err()
        }
        if gotMsg.Error != nil {
          return gotMsg.Error
        }

        if gotMsg.Phase != phase {
          return fmt.Errorf("got unexpected phase while waiting for %s: %s", phase, gotMsg.Phase)
        }

        err := jsonHexUnmarshal(gotMsg.Body, &v)
        if err != nil {
          return err
        }

        return nil
      }

      func (cc *clientProtocol) ReadPake(ctx context.Context) error {
        var pake pakeMsg
        err := cc.readPlaintext(ctx, "pake", &pake)
        if err != nil {
          return err
        }

        otherSidesMsg, err := hex.DecodeString(pake.Body)
        if err != nil {
          return err
        }

        sharedKey, err := cc.spake.Finish(otherSidesMsg)
        if err != nil {
          return err
        }

        cc.sharedKey = sharedKey

        return nil
      }

      ```

      `pake`'s body is a string of length 66. `otherSidesMsg` is `[]uint8` bytes of length 33.

      Then `sharedKey` is generated by calling `cc.spake.Finish(otherSidesMsg)`. `spake` is a SPAKE2 object.

      `sharedKey` is a 32-byte long byte array.

      So what is `pake` message read from the mailbox?

      TODO

    - [`err = collector.waitFor(&answer)`](https://github.com/psanford/wormhole-william/blob/68dc3447a8585b060fb1e6836a23847700ab9207/wormhole/send.go#L344): Wait for receiver to enter Y to confirm. The answer contains a OK message
    - A cryptor (type=`transportCryptor`) is created.

      ```go
        cryptor := newTransportCryptor(conn, transitKey, "transit_record_receiver_key", "transit_record_sender_key")

        recordSize := (1 << 14) // record size: 16384 byte (16kb)
        // chunk
        recordSlice := make([]byte, recordSize-secretbox.Overhead)
        hasher := sha256.New()
      ```

      `conn` is a `net.TCPConn` TCP connection.

      A `readKey` and `writeKey` are generated with hkdf (HMAC-based Extract-and-Expand Key Derivation Function) from `transitKey` and two strings in `newTransportCryptor`.

      `transitKey` is derived from `clientProto.sharedKey` and `appID`.

      ```go
      transitKey := deriveTransitKey(clientProto.sharedKey, appID)
      ```

      `sharedKey` is a 32-byte long key generated by `clientProto` (a `pake.Client`).

      ```go
      func newTransportCryptor(c net.Conn, transitKey []byte, readPurpose, writePurpose string) *transportCryptor {
        r := hkdf.New(sha256.New, transitKey, nil, []byte(readPurpose))
        var readKey [32]byte
        _, err := io.ReadFull(r, readKey[:])
        if err != nil {
          panic(err)
        }

        r = hkdf.New(sha256.New, transitKey, nil, []byte(writePurpose))
        var writeKey [32]byte
        _, err = io.ReadFull(r, writeKey[:])
        if err != nil {
          panic(err)
        }

        return &transportCryptor{
          conn:          c,
          prefixBuf:     make([]byte, 4+crypto.NonceSize),
          nextReadNonce: big.NewInt(0),
          readKey:       readKey,
          writeKey:      writeKey,
        }
      }
      ```

      `recordSize` is 16384 byte (16kb), used to read file in chunks.

      `hasher` is compute file hash while reading file.

    - In [the following loop](https://github.com/psanford/wormhole-william/blob/68dc3447a8585b060fb1e6836a23847700ab9207/wormhole/send.go#L387), file is read and sent in chunks.

      `r` has type `io.Reader`. Every time 16KB is read.

      `cryptor.writeRecord` encrypts the bytes and send the bytes.

      ```go
      for {
        n, err := r.Read(recordSlice)
        if n > 0 {
          hasher.Write(recordSlice[:n])
          err = cryptor.writeRecord(recordSlice[:n]) // send 16KB in each iteration
          if err != nil {
            sendErr(err)
            return
          }
          progress += int64(n)
          if options.progressFunc != nil {
            options.progressFunc(progress, totalSize)
          }
        }
        if err == io.EOF {
          break
        } else if err != nil {
          sendErr(err)
          return
        }
      }
      ```

      Let's see how `writeRecord` works.

      `package secretbox ("golang.org/x/crypto/nacl/secretbox")` is used to encrypt data.

      `d.conn.Write` sends the encrypted data out.

      ```go
      func (d *transportCryptor) writeRecord(msg []byte) error {
        var nonce [crypto.NonceSize]byte

        if d.nextWriteNonce == math.MaxUint64 {
          panic("Nonce exhaustion")
        }

        binary.BigEndian.PutUint64(nonce[crypto.NonceSize-8:], d.nextWriteNonce)
        d.nextWriteNonce++

        sealedMsg := secretbox.Seal(nil, msg, &nonce, &d.writeKey)

        nonceAndSealedMsg := append(nonce[:], sealedMsg...)

        // we do an explit cast to int64 to avoid compilation failures
        // for 32bit systems.
        nonceAndSealedMsgSize := int64(len(nonceAndSealedMsg))

        if nonceAndSealedMsgSize >= math.MaxUint32 {
          panic(fmt.Sprintf("writeRecord too large: %d", len(nonceAndSealedMsg)))
        }

        l := make([]byte, 4)
        binary.BigEndian.PutUint32(l, uint32(len(nonceAndSealedMsg)))

        lenNonceAndSealedMsg := append(l, nonceAndSealedMsg...)

        _, err := d.conn.Write(lenNonceAndSealedMsg)
        return err
      }
      ```
