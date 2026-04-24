# Test detect-secrets - File with exposed secrets
# Intentional errors: API keys, hardcoded passwords

API_KEY = "sk_live_1234567890abcdefghijklmnop"
DATABASE_URL = "postgresql://user:password123@localhost/db"
AWS_SECRET = "Example/OfAWS/Secret"


def get_api_key():
    return API_KEY
