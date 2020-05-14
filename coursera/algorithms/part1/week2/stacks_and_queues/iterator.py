class Iterator:

    def __init__(self, l):
        self.i = l.copy()

    def next(self):
        try:
            item = self.i.pop()
        except IndexError:
            raise UnboundLocalError
        return item

    def remove(self):
        raise AttributeError

    def has_next(self):
        return self.i