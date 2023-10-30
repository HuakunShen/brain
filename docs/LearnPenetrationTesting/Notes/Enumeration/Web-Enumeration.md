---
title: Web Enumeration
---

# Gobuster

After discovering a web app, use tools such as `ffuf` or `GoBuster` to uncover any hidden files or directories on the webserver.

```bash
# scanning
gobuster dir -u http://10.0.0.10/ -w /usr/share/dirb/wordlists/common.txt

# ===============================================================
# Gobuster v3.0.1
# by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
# ===============================================================
# [+] Url:            http://10.0.0.10/
# [+] Threads:        10
# [+] Wordlist:       /usr/share/dirb/wordlists/common.txt
# [+] Status codes:   200,204,301,302,307,401,403
# [+] User Agent:     gobuster/3.0.1
# [+] Timeout:        10s
# ===============================================================
# 2020/12/11 21:47:25 Starting gobuster
# ===============================================================
# /index.php (Status: 200)
# /server-status (Status: 403)
# /wordpress (Status: 301)
# ===============================================================
# 2020/12/11 21:47:46 Finished
# ===============================================================
```

# DNS Subdomain Enumeration

## Install SecLists

This has many useful lists for fuzzing.

```bash
git clone https://github.com/danielmiessler/SecLists
sudo apt install seclists -y
gobuster dns -d inlanefreight.com -w /usr/share/SecLists/Discovery/DNS/namelist.txt

# ===============================================================
# Gobuster v3.0.1
# by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
# ===============================================================
# [+] Domain:     inlanefreight.com
# [+] Threads:    10
# [+] Timeout:    1s
# [+] Wordlist:   /usr/share/SecLists/Discovery/DNS/namelist.txt
# ===============================================================
# 2022/9/17 23:08:55 Starting gobuster
# ===============================================================
# Found: blog.inlanefreight.com
# Found: customer.inlanefreight.com
# Found: my.inlanefreight.com
# Found: ns1.inlanefreight.com
# Found: ns2.inlanefreight.com
# Found: ns3.inlanefreight.com
# ===============================================================
# 2020/12/17 23:10:34 Finished
# ===============================================================
```

# Web Enumeration Tips

## Banner Grabbing / Web Server Headers

use `cURL` to retrieve server header information (response headers).

```bash
curl -IL https://www.inlanefreight.com
```

[EyeWitness](https://github.com/FortyNorthSecurity/EyeWitness) can be used to take screenshots of target web app, fingerprint them and identify possible default credentials.

## Whatweb

Extract

- web server version
- supporting frameworks
- applications

```bash
whatweb 10.0.0.10

# http://10.0.0.10 [200 OK] Apache[2.4.41], Country[RESERVED][ZZ], Email[license@php.net], HTTPServer[Ubuntu Linux][Apache/2.4.41 (Ubuntu)], IP[10.0.0.10], Title[PHP 7.4.3 - phpinfo()]


# scan a subnet
whatweb --no-errors 10.10.10.0/24

# http://10.10.10.11 [200 OK] Country[RESERVED][ZZ], HTTPServer[nginx/1.14.1], IP[10.10.10.11], PoweredBy[Red,nginx], Title[Test Page for the Nginx HTTP Server on Red Hat Enterprise Linux], nginx[1.14.1]
# http://10.10.10.100 [200 OK] Apache[2.4.41], Country[RESERVED][ZZ], HTTPServer[Ubuntu Linux][Apache/2.4.41 (Ubuntu)], IP[10.10.10.100], Title[File Sharing Service]
# http://10.0.0.10 [200 OK] Apache[2.4.41], Country[RESERVED][ZZ], Email[license@php.net], HTTPServer[Ubuntu Linux][Apache/2.4.41 (Ubuntu)], IP[10.0.0.10], Title[PHP 7.4.3 - phpinfo()]
# http://10.10.10.247 [200 OK] Bootstrap, Country[RESERVED][ZZ], Email[contact@cross-fit.htb], Frame, HTML5, HTTPServer[OpenBSD httpd], IP[10.10.10.247], JQuery[3.3.1], PHP[7.4.12], Script, Title[Fine Wines], X-Powered-By[PHP/7.4.12], X-UA-Compatible[ie=edge]
```

## Certificates

Go to `https://<ip>/` to find email address and company name. Could potentially be used to conduct a phishing attack.

## Robots.txt

This file is designed for bots like GoogleBot, it provides the location of web pages (maybe private).

## Source Code

`CTRL + U` to bring up the source code window. There could be sensitive information in comments and code.


