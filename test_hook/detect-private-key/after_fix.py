# Test detect-private-key - Fixed file
# Key retrieved from environment variable

import os


def get_private_key_path():
    return os.getenv("PRIVATE_KEY_PATH")


def validate_key():
    key_path = get_private_key_path()
    if key_path and os.path.exists(key_path):
        with open(key_path) as f:
            return f.read()
    return None
