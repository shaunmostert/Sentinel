# Sentinel

A lightweight log analysis and threat detection tool built with Python.

Sentinel is a project I am building to better understand how Security Operations Centre (SOC) analysts work with authentication logs, event data, and security alerts.

The goal of Sentinel is to take raw Linux log files, process the data into a structured format, detect suspicious activity, and generate useful information for investigation.

This project is mainly focused on learning how SIEM systems work internally and applying cybersecurity concepts through practical development.

---

## Current Features

### Log ingestion
- Accepts user-provided log files through the command line
- Reads and processes authentication logs
- Handles different log formats

### Log parsing
- Extracts important fields from raw log entries:
  - Timestamp
  - Username
  - Source IP address
  - Port
  - Service
  - Event type
  - Raw log data

### Data storage
- Stores processed events using SQLite
- Allows structured searching and filtering of collected events

### Detection logic
(Currently in development)

Planned detections include:
- SSH brute-force attempts
- Multiple failed authentication attempts from a single IP address
- Suspicious sudo activity
- Privilege escalation indicators

---

## How Sentinel Works

The current workflow:
