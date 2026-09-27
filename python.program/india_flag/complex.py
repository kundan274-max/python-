"""class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def add(self, t):
        return Complex(self.r + t.r, self.i + t.i)

    def __str__(self):
        if self.i >= 0:
            return (f"{self.r}+{self.i}j")
        return (f"{self.r}{self.i}j")


c1 = Complex(2, 3)
c2 = Complex(4, 5)
result = c1.add(c2)

print("First complex number:", c1)
print("Second complex number:", c2)
print("Sum:", result)"""

"""class Complex:
    def __init__(self, a, b):
        self.__x = a
        self.__i = b

    def calculate(self, c2):
        t = Complex(0, 0)
        t.__x = self.__x + c2.__x
        t.__i = self.__i + c2.__i
        return t

    def display(self):
        print("Real:", self.__x)
        print("Imaginary:", self.__i)


c1 = Complex(2, 3)
c2 = Complex(4, 6)

c3 = c1.calculate(c2)

c3.display()"""



