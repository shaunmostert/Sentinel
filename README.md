# Sentinel

A Python-based Linux authentication log analysis platform designed to detect suspicious activity and generate investigation-ready security reports.

## Overview

Security teams rely on log analysis to identify malicious behaviour such as brute-force attacks, unauthorized access attempts, and privilege escalation.

Sentinel is a lightweight security analysis tool that processes Linux authentication logs (`auth.log`), extracts important security events, applies detection rules, and generates alerts for further investigation.

The goal of this project is to demonstrate practical understanding of:

- Security monitoring
- Log analysis
- Detection engineering
- Incident investigation
- Python automation
- Linux authentication systems

---

## Features

### Current Features

- Parse Linux authentication logs
- Extract authentication events
- Identify failed SSH login attempts
- Detect suspicious authentication patterns
- Generate security alerts

### Planned Features

- Multiple log source support
- MITRE ATT&CK technique mapping
- Investigation timelines
- HTML reporting
- Custom detection rules
- Live log monitoring

---

## How Sentinel Works

`Authentication Logs`
    ↓
`Log Parser`
    ↓
`Event Normalization`
    ↓
`Detection Engine`
    ↓
`Alert Generation`
    ↓
`Investigation Report Generation`

---

## Detection Rules

### SSH Brute Force Detection

Detects repeated failed SSH authentication attempts from the same source IP within a defined time window.

Example:
```bash
Multiple failed SSH logins detected

Source IP:
203.0.113.42

Target User:
root

Attempts:
7

Severity:
High
```


---

## Technology Used

- Python
- Linux
- Regular Expressions
- Log Analysis
- Git/GitHub

---

## Project Goals

This project was created to develop practical cybersecurity skills in:

- Security Operations Centre (SOC) workflows
- Detection logic development
- Incident investigation processes
- Defensive security engineering

---

## Installation

(Add later)

---

## Usage

(Add later)

---

## Roadmap

Version 1:
- [ ] Authentication log parsing
- [ ] SSH brute force detection
- [ ] Basic alert generation

Version 2:
- [ ] Timeline generation
- [ ] HTML reports
- [ ] Additional detection rules

Version 3:
- [ ] Live monitoring
- [ ] Custom rules
- [ ] Dashboard interface

---

## Disclaimer

***Sentinel is an educational cybersecurity project designed for analysing security logs and learning defensive security concepts.***
