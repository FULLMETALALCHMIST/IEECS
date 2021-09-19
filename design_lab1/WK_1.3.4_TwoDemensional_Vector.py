import operator


class V2(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'V2[{self.x},{self.y}]'

    def getx(self):
        print(self.x)

    def gety(self):
        print(self.y)

    def __add__(self, other):
        return V2(self.x + other.x, self.y + other.y)

    def __mul__(self, con):
        return V2(self.x * con, self.y * con)


v = V2(1, 2)
a = V2(3, 4)
b = V2(5, 6)

print(v)

v.getx()
v.gety()

print(operator.add(a, b))
print(operator.mul(a, -1))

print(a + b)
print(a * -1)

print(V2(1.1, 2.2) + V2(3.3, 4.4))
