from math import floor

from tuple import x


class StripePattern:
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def color_at(self, pt):
        return self.a if floor(x(pt)) % 2 == 0 else self.b

