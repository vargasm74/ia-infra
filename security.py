import re

SENSITIVE_PATTERNS = [
    r'password\s*:',
    r'token\s*:',
    r'api_key\s*:',
    r'client_secret\s*:',
    r'private_key\s*:'
]

def sanitize(text):

    for pattern in SENSITIVE_PATTERNS:
        text = re.sub(
            pattern + r'.*',
            pattern + ' <REDACTED>',
            text,
            flags=re.IGNORECASE
        )

    return text