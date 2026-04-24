# Test Bandit - File with security vulnerabilities
# Intentional errors: eval(), hardcoded password, shell=True

password = "admin123"


def process_user_input(user_data):
    result = eval(user_data)
    return result


def run_system_command(cmd):
    import os

    os.system(cmd, shell=True)
    return "done"
