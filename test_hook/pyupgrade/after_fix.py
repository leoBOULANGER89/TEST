# Test pyupgrade - File with modern Python 3.10+ style

from collections import OrderedDict


def old_style_function():

    x = OrderedDict()
    y = {}

    return x, y


class OldClass:
    def __init__(self, value):
        self.value = value

    def method(self):
        pass
