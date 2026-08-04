# Sentinel

A lightweight log analysis and threat detection tool built with Python.

Sentinel is a project I am building to better understand how Security Operations Centre (SOC) analysts work with authentication logs, event data, and security alerts.

The goal of Sentinel is to take raw Linux log files, process the data into a structured format, detect suspicious activity, and generate useful information for investigation.

This project is mainly focused on learning how SIEM systems work internally and applying cybersecurity concepts through practical development.

---

## Current Features

### Log Ingestion

- Accepts user-provided log files through the command line
- Reads and processes authentication logs
- Handles different log formats

### Log Parsing

Sentinel extracts important information from raw log entries:

- Timestamp
- Username
- Source IP address
- Port
- Service
- Event type
- Raw log data

### Data Storage

- Stores processed events using SQLite
- Converts raw logs into structured data
- Allows events to be searched and filtered using SQL queries

### Detection Logic

(Currently in development)

Planned detections include:

- SSH brute-force attempts
- Multiple failed authentication attempts from a single IP address
- Suspicious sudo activity
- Privilege escalation indicators

---

# How Sentinel Works

The current workflow:

```
User selects log file

        ↓

Sentinel reads the log

        ↓

Parser extracts important information

        ↓

Events are stored in SQLite

        ↓

Detection rules analyse events

        ↓

Security alerts are generated
```

---

# Project Structure

```
Sentinel/
│
├── sentinel.py              # Main application
│
├── modules/
│   ├── parser.py            # Extracts information from logs
│   ├── database.py          # Handles SQLite storage
│   ├── detections.py        # Detection rules
│   └── reporter.py          # Generates reports
│
├── sample_logs/             # Testing logs
│
├── sentinel.db              # Local event database
│
└── README.md
```

---

# Example Detection

One of the planned detections is SSH brute-force detection.

Example log entries:

```
Aug 04 10:12:01 server sshd[1521]:
Failed password for invalid user admin from 192.168.1.50 port 54122 ssh2

Aug 04 10:12:03 server sshd[1521]:
Failed password for invalid user admin from 192.168.1.50 port 54122 ssh2

Aug 04 10:12:05 server sshd[1523]:
Failed password for root from 192.168.1.50 port 54124 ssh2
```

If the same IP generates multiple failed authentication attempts within a short period, Sentinel will generate an alert for further investigation.

Example:

```
ALERT: Possible SSH brute-force attack detected

Source IP:
192.168.1.50

Failed attempts:
7

Severity:
High

Recommended action:
Investigate source IP and review authentication activity
```

---

# Technologies Used

- Python
- SQLite
- SQL
- Regular Expressions
- Linux authentication logs
- JSON
- Command-line interfaces

---

# Why I Built Sentinel

I created Sentinel to gain practical experience with defensive cybersecurity concepts.

While studying cybersecurity, I wanted a project that allowed me to apply topics such as:

- Log analysis
- Threat detection
- Security monitoring
- Incident investigation
- SIEM concepts

Instead of only learning how security tools are used, this project focuses on understanding how some of these systems work behind the scenes.

---

# Development Progress

## Completed

- [x] Basic command-line interface
- [x] User-selected log file input
- [x] Authentication log parsing
- [x] Event formatting
- [x] Structured event storage
- [x] SQLite database integration

## Currently Working On

- [ ] Detection engine
- [ ] Alert severity scoring
- [ ] SQL-based threat hunting queries
- [ ] Root-cause timeline analysis
- [ ] HTML incident reports

## Future Goals

- [ ] Support multiple log sources
- [ ] Continuous log monitoring
- [ ] Automated detection rules
- [ ] Event correlation
- [ ] Timeline reconstruction
- [ ] Analyst-focused dashboards

---

# Planned Architecture

The final Sentinel architecture will follow a similar workflow to professional SIEM systems:

```
Raw Logs

    ↓

Log Collection

    ↓

Parsing & Normalisation

    ↓

Database Storage

    ↓

Detection Engine

    ↓

Alert Generation

    ↓

Incident Report
```

---

# Example Use Cases

## SSH Brute-force Detection

Detect repeated failed SSH login attempts from the same source IP.

## Privilege Escalation Monitoring

Identify suspicious sudo activity, including:

- Unexpected root access attempts
- Failed sudo authentication
- Commands executed with elevated privileges

## Security Investigation

Allow analysts to search stored events and investigate:

- Specific IP addresses
- User activity
- Authentication failures
- Suspicious commands

---

# Current Development Status

Sentinel is currently under active development.

This project is being developed as a learning project to improve my understanding of:

- Python development
- Cybersecurity monitoring
- SIEM architecture
- Log analysis
- Defensive security operations

---

# Disclaimer

Sentinel is an educational project created to explore defensive cybersecurity concepts.

It is not intended to replace professional SIEM platforms or enterprise security monitoring solutions.

The purpose of this project is to understand the processes behind security monitoring tools and apply cybersecurity concepts in a practical environment.
