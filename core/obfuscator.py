# core/obfuscator.py

import random


def apply_obfuscation(payloads, method):
    """
    Apply basic educational obfuscation techniques.
    Supported:
    - comment
    - whitespace
    - mixed
    """

    for payload in payloads:
        original = payload["payload"]

        if method == "comment":
            obfuscated = insert_comments(original)

        elif method == "whitespace":
            obfuscated = insert_whitespace(original)

        elif method == "mixed":
            temp = insert_comments(original)
            obfuscated = insert_whitespace(temp)

        else:
            obfuscated = original

        payload["original_payload"] = original
        payload["payload"] = obfuscated
        payload["obfuscation_applied"] = method

    return payloads


# -----------------------------
# Obfuscation Techniques
# -----------------------------

def insert_comments(text):
    """
    Insert simple inline comments for educational bypass simulation.
    """
    if len(text) < 4:
        return text

    midpoint = len(text) // 2
    return text[:midpoint] + "/**/" + text[midpoint:]


def insert_whitespace(text):
    """
    Insert random whitespace between characters
    to simulate filter evasion.
    """
    result = ""
    for char in text:
        result += char
        if random.choice([True, False]):
            result += " "
    return result
