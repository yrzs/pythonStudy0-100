from math import sqrt

class Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    # 静态方法
    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        # 海伦公式
        p = self.perimeter() / 2
        return sqrt(p * (p - self._a) * (p - self._b) * (p - self._c))


def main():
    a, b, c = 3, 4, 5
    if Triangle.is_valid(a, b, c):
        print("构成三角形")
        t = Triangle(a, b, c)
        print(t.perimeter())
        print(t.area())

    else:
        raise Exception("不构成三角形")


if __name__ == '__main__':
    main()
