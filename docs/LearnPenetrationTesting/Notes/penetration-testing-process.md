---
title: Penetration Testing Process
---
# Stages

## Pre-Engagement

Planning with client, contract, all ncessary tests and components are stictly defined.

- Non-Disclosure Agreement
- Goals
- Scope
- Time Estimation
- Rules of Engagement

## Information Gathering

Obtain information of target in all kinds of ways. Including software and hardware used, to find potential vulnerabilities.

- OSINT (Open Source Intelligence): get information from public sources (open source)
- Infrastructure Enumeration
  - Create a map of client's servers and hosts with DNS and understand how it's structured
    - name servers
    - mail servers
    - web servers
    - cloud instances
  - Identifying the firewall tells us understanding of techniques used
    - also tells what methods can be used to avoid triggering alarm
- Service Enumeration
  - version of service
- Host Enumeration
  - Identify Operating System
  - Identify Services
  - Identify Service Version
- Pillaging
  - This happends in post-exploitation stage
  - Collect sensitive information on exploited host

## Vulnerability Assessment

- Analyze information gathered
- Look for known vulnerabilities in systems, applications, and various versions
- Evaluation of potential vulnerabilities (threat level)

## Exploitation

Execute attack.

## Post-Exploitation

At this stage, we already have access to exploited machine. 

- Try to escalate privileges
- Obtain sensitive data

## Lateral Movement

Access additional hosts at the same or higher privilege level. 

## Proof-of-Concept

Document the process.

## Post-Engagement

Provide detailed documentation, report.
