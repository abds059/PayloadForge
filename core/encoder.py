# core/encoder.py

import base64
import urllib.parse


def apply_encoding(payloads, encoding_type):
    """
    Apply encoding to the 'payload' field only.
    Supported encodings:
    - url
    - base64
    - hex
    """

    for payload in payloads:
        original = payload.get("payload", "")

        if encoding_type == "url":
            encoded = urllib.parse.quote(original)

        elif encoding_type == "base64":
            encoded = base64.b64encode(original.encode()).decode()

        elif encoding_type == "hex":
            encoded = original.encode().hex()

        else:
            encoded = original

        payload["original_payload"] = original
        payload["payload"] = encoded
        payload["encoding_applied"] = encoding_type

    return payloads
