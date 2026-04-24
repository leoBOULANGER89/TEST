# Test Ruff - File with linting errors
# Intentional errors: unused imports, unused variables

import math
import os


def ma_fonction(a, b, c):
    x_unused = a + b
    if a == b:
        return True
    else:
        return False


y_unused = 5
