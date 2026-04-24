# Test pyupgrade - File with old Python style
# Intentional errors: pre-Python 3.10 syntax that pyupgrade CANNOT auto-fix


def old_style_function():
    import collections

    x = collections.OrderedDict()
    y = dict()

    return x, y


class OldClass:
    def __init__(self, value):
        self.value = value

    def method(self):
        pass
