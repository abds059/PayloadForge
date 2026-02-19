# core/waf_notes.py

def attach_waf_notes(payloads):
    """
    Attach defensive / WAF detection notes
    explaining why payloads may be blocked.
    Educational purpose only.
    """

    for payload in payloads:

        notes = []

        content = payload.get("payload", "").lower()

        # -----------------------------
        # XSS Detection Patterns
        # -----------------------------
        if "<script" in content:
            notes.append("Likely blocked by signature-based WAF detecting <script> tags.")
            notes.append("Mitigation: Proper output encoding and Content Security Policy (CSP).")

        if "onerror" in content or "onload" in content:
            notes.append("Event handler usage may trigger WAF detection rules.")
            notes.append("Mitigation: Attribute sanitization and strict HTML validation.")

        if "javascript:" in content:
            notes.append("javascript: protocol often blocked by modern browsers and filters.")
            notes.append("Mitigation: URL validation and protocol allowlisting.")

        # -----------------------------
        # SQLi Detection Patterns
        # -----------------------------
        if "union" in content:
            notes.append("UNION keyword commonly detected by SQLi protection filters.")
            notes.append("Mitigation: Parameterized queries / prepared statements.")

        if " or " in content or " and " in content:
            notes.append("Boolean logic patterns may trigger SQLi detection.")
            notes.append("Mitigation: Strict input validation and ORM usage.")

        if "--" in content:
            notes.append("SQL comment sequences often flagged by WAF rules.")
            notes.append("Mitigation: Escaping input and query parameterization.")

        if "sleep" in content:
            notes.append("Time-delay functions may indicate blind SQLi attempts.")
            notes.append("Mitigation: Query time monitoring and anomaly detection.")

        # -----------------------------
        # Command Injection Detection
        # -----------------------------
        if ";" in content or "&&" in content or "||" in content or "|" in content:
            notes.append("Command chaining operators may indicate injection attempts.")
            notes.append("Mitigation: Avoid system shell calls or use safe execution APIs.")

        # -----------------------------
        # Default fallback
        # -----------------------------
        if not notes:
            notes.append("May bypass naive regex filters but should be blocked by secure coding practices.")

        payload["waf_detection_notes"] = notes

    return payloads
