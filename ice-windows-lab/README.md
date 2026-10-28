# TryHackMe: Ice — Windows Security Lab

## Project Overview

This project documents my hands-on experience completing the Ice Windows security lab on TryHackMe. I used Nmap for reconnaissance and studied how exposed network services and vulnerable applications can introduce security risks.

## Objectives

- Perform network reconnaissance using Nmap.
- Identify open ports and investigate running services.
- Understand the security risks associated with a vulnerable media server.
- Explore Windows security assessment concepts in an authorized lab.
- Identify defensive measures that can reduce security risks.

## Lab Environment

- **Platform:** TryHackMe
- **Room:** Ice
- **Target:** Windows lab machine provided by TryHackMe
- **Primary tool:** Nmap
- **Environment:** Authorized cybersecurity training lab

Room reference: 
https://tryhackme.com/room/ice?utm_campaign=social_share&utm_medium=social&utm_content=share-completed-room&utm_source=copy&sharerId=636d0507685afc0043217348

https://tryhackme.com/room/ice

## Tools and Technologies

- **Nmap:** Network scanning and service discovery.
- **Windows:** Operating system security concepts.
- **Networking:** TCP ports, exposed services, and remote access.
- **Vulnerability assessment:** Understanding weaknesses and potential impact.
- **Security documentation:** Recording observations and recommended mitigations.

## Methodology

### 1. Lab Setup

I accessed the TryHackMe Ice room and used its designated training environment. The assessment was conducted within the authorized lab.

### 2. Network Reconnaissance

I used Nmap to scan the assigned target and investigate accessible network ports.

The purpose was to identify exposed services and gather information that could support further security analysis.

### 3. Service Enumeration

I examined the services identified during reconnaissance to understand their purpose and potential security implications.

The Ice lab highlights the importance of investigating exposed remote-access services and the Icecast media server.

### 4. Security Analysis

I considered how outdated software, unnecessary network exposure, and weak system protections can increase the risk of compromise.

### 5. Defensive Review

I reviewed security measures that could help reduce the risks identified during the lab, including patching, restricting network access, and monitoring system activity.

## Nmap Reconnaissance

**Tool:** Nmap

**Purpose:** Identify accessible ports and investigate services on the authorized lab target.

**Scan command:** Record the exact command used during my session.

**Target:** The temporary IP address assigned by TryHackMe.

### Results

Document the verified results from my scan:

- Open ports: Add the ports shown in my scan output.
- Detected services: Add the service names reported by Nmap.
- Service versions: Include only versions actually identified.
- Hostname: Add the hostname if it appeared in my results.

### Analysis

Nmap reconnaissance helps establish which network services are accessible on a target. This information can help a security analyst identify unnecessary exposure and determine which services need further investigation.

## Security Findings

### Finding 1: Exposed Network Services

**Observation:** The lab involved identifying network services accessible on the target.

**Potential risk:** Unnecessary or poorly secured services may increase the attack surface.

**Recommended mitigation:** Restrict inbound connections to required services and allow access only from trusted networks where practical.

### Finding 2: Vulnerable Media Server

**Observation:** The TryHackMe Ice scenario focuses on a vulnerable Icecast service.

**Potential risk:** A vulnerable service may allow an attacker to execute unauthorized actions on the affected system.

**Recommended mitigation:** Upgrade to a supported, patched version, remove unnecessary services, and monitor service activity.

### Finding 3: Windows Security Configuration

**Observation:** The lab explores Windows security weaknesses and the consequences of inadequate system protections.

**Potential risk:** Weak security controls can make unauthorized access and further compromise easier.

**Recommended mitigation:** Maintain security updates, enable appropriate endpoint protection and firewall controls, apply least privilege, and monitor security logs.

*These findings describe the security themes of the training scenario. Add specific evidence from my own lab results before presenting any item as a confirmed observation.*

## Defensive Recommendations

- Keep Windows and applications patched.
- Restrict network access to necessary ports and services.
- Use host firewalls and endpoint protection.
- Apply least-privilege permissions.
- Monitor Windows logs and network activity.
- Review exposed services regularly.
- Document findings and verify remediation.

## Key Learning Outcomes

- Gained practical experience using Nmap during an authorized lab.
- Improved understanding of network reconnaissance and service enumeration.
- Learned why vulnerable applications require timely patching.
- Explored Windows security risks and defensive controls.
- Practiced documenting security observations and remediation recommendations.

## Conclusion

Completing the TryHackMe Ice lab strengthened my understanding of network reconnaissance, Windows security, and vulnerability assessment. The project demonstrates my commitment to practical cybersecurity learning and to identifying security risks and recommending appropriate defensive measures.

## Reference

TryHackMe — Ice:
https://tryhackme.com/room/ice?utm_campaign=social_share&utm_medium=social&utm_content=share-completed-room&utm_source=copy&sharerId=636d0507685afc0043217348

https://tryhackme.com/room/ice
