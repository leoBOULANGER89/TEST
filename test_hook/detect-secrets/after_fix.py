# Test detect-secrets - File without secrets
# Secrets retrieved from environment variables

import os


def get_api_key():
    return os.getenv("API_KEY")


def get_database_url():
    return os.getenv("DATABASE_URL")
