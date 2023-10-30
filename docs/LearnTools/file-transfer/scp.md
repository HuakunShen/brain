# SCP (Secure Copy)

## Intro

`scp` (secure copy) lets you securely copy files to remote server.

It works similarly to `cp` command.

It's based on `ssh`.

## Usage

Here are the the most basic usage. 

```bash
scp file.txt user@10.0.0.1:Desktop/file.txt

scp -r folder user@10.0.0.1:Desktop/folder
```

For more options, read [How to Use SCP Command to Securely Transfer Files](https://linuxize.com/post/how-to-use-scp-command-to-securely-transfer-files/).

## Reference

- [How to Use SCP Command to Securely Transfer Files](https://linuxize.com/post/how-to-use-scp-command-to-securely-transfer-files/)
