
class FNumber:
    def __init__(self, ffield, value):
        self.f = ffield
        self.v = int(value) % self.f.p

    def __neg__(self):
        return FNumber(self.f, -self.v)
    
    def __add__(self, other):
        return FNumber(self.f, int(self) + int(other))

    def __sub__(self, other):
        return -other + self

    def __mul__(self, other):
        return FNumber(self.f, int(self) * int(other))

    def __int__(self):
        return self.v

    def __truediv__(self, other):
        return self.f.mod(self.f.find(int(self)) - self.f.find(int(other)))

    def __pow__(self, other):
        return self.f.mod(self.f.find(int(self)) * int(other))

    def __eq__(self, other):
        return int(self) == int(other)

    def __str__(self):
        return str(int(self))

class FField:
    def __init__(self, p, w):
        self.p = p
        self.w = w

    def mod(self, j):
        b = 1
        for _ in range(j % self.p - 1 if j < 0 else j):
            b = (b * self.w) % self.p
        return self.num(b)

    def find(self, b):
        for j in range(self.p):
            if int(b) == self.mod(j):
                return j
        return -1

    def num(self, value):
        return FNumber(self, value)