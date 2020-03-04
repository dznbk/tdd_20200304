class ClosedRange():
    def __init__(self, bottom, top):
        if bottom > top:
            raise ValueError
        self.bottom = bottom
        self.top = top

    def build_string(self):
        return f"[{self.bottom}, {self.top}]"

    def include_number(self, number):
        return self.bottom <= number <= self.top

    def is_same(self, another):
        return self.bottom == another.bottom and \
                self.top == another.top

    def include_range(self, another):
        return self.bottom <= another.bottom and \
                another.top <= self.top

