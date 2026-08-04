import re
from datetime import datetime


def parse_auth_log(line):
    """
    Parses a Linux auth.log line and returns a structured event.

    Input:
        Raw log line (string)

    Output:
        Dictionary containing extracted event data
    """

    event = {
        "timestamp": None,
        "event_type": None,
        "username": None,
        "source_ip": None,
        "port": None,
        "service": None,
        "raw_log": line.strip()
    }

    timestamp_pattern = r"^(?P<timestamp>[A-Z][a-z]{2}\s+\d+\s\d{2}:\d{2}:\d{2})"
    timestamp_match = re.search(timestamp_pattern, line)

    if timestamp_match:
        event["timestamp"] = timestamp_match.group("timestamp")


    if "Failed password" in line:
        event["event_type"] = "failed_login"
        event["service"] = "sshd"


        username_pattern = r"(?:for invalid user|for)\s(\w+)"
        username_match = re.search(username_pattern, line)

        if username_match:
            event["username"] = username_match.group(1)


        ip_pattern = r"from\s(\d+\.\d+\.\d+\.\d+)"
        ip_match = re.search(ip_pattern, line)

        if ip_match:
            event["source_ip"] = ip_match.group(1)


        port_pattern = r"port\s(\d+)"
        port_match = re.search(port_pattern, line)

        if port_match:
            event["port"] = port_match.group(1)

    return event