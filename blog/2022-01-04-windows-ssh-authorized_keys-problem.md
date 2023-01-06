---
title: Windows OpenSSH Server authorized_keys Failure on Administrative User Account
authors: [huakun]
tags: [network, hack, fix, windows, win11, OS, ssh]
---

## Problem

I run into a problem related to ssh and got stuck for a few days. On a fresh-intsalled win11 PC, I tried to configure OpenSSh server, which I have done a thousand times on Linux OS.

I could ssh into the windows PC, but only using password; Key-based auth (i.e. password-less) doesn't work no matter what I do.

I added the `authorized_keys` file to `C:\Users\username\.ssh`, checked the file permission and even created another user account to compare.

None of these fixed the problem, and I couldn't find a good solution from Google or Chat GPT. BTW, Chat GPT keeps giving me Linux-related solutions.

## Solution

The solution is actually quite simple. I read the official Doc by microsoft. [Key-based authentication (Administrative user)](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_keymanagement#administrative-user).

It turns out, Windows treat admin account differently. On Linux, regular accounts and sudoer accounts both use `$HOME/.ssh/authorized_keys` to stored trusted public keys.

The reason of my failure was because I was trying to ssh into an admin account.

On Windows, a `administrators_authorized_keys` should be placed under `C:\ProgramData\ssh\`. The content of `administrators_authorized_keys` is exactly the same.

**Solution verified to work.**

## Comment

- I can't blame Microsoft as this may be a more secure approach, and it's clearly documented in their documentation.
  - But maybe don't hide this at the bottom of the page. Highlight it in the beginning. It's easy to ignore it.
- However, I don't understand why I can't easily find solution for such a common topic online. One would not search with the "administrative" keyword for such problem. Maybe Windows should give more warning messages and hints when OpenSSH server is installed or when login failed.
- Furthermore, Chat GPT still has a long way to go.
- And Google Search, ... hope you don't get completely replaced by some tech like Chat GPT one day.

Good Luck Hacking!