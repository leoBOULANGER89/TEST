# Test Bandit - Fichier securise
# Aucune vulnerabilite

import os


def process_user_data(user_data):
    import ast

    ast.literal_eval(user_data)
    return user_data


def get_system_info():
    return {
        "os_name": os.name,
        "sep": os.sep,
        "linesep": os.linesep,
    }


def validate_input(value):
    if not isinstance(value, str):
        raise TypeError("Expected string")
    if len(value) > 1000:
        raise ValueError("Input too long")
    return True
