"""class Distance:
    def __init__(self, km, m):
        self.km = km
        self.m = m

    def sum(self, d2):
        d = Distance(0, 0)

        d.m = self.m + d2.m
        d.km = self.km + d2.km

        if d.m >= 1000:
            d.m = d.m - 1000
            d.km = d.km + 1

        return d

    def display(self):
        print("Distance:", self.km, "km", self.m, "m")


d1 = Distance(5, 750)
d2 = Distance(3, 500)

d3 = d1.sum(d2)

d3.display()"""

#Add two fraction

"""class Fraction:
    def __init__(self, n, d):
        self.n = n
        self.d = d

    def sum(self, f2):
        f = Fraction(0, 1)

        f.n = self.n * f2.d + f2.n * self.d
        f.d = self.d * f2.d

        return f

    def display(self):
        print("Fraction:", self.n, "/", self.d)


f1 = Fraction(2, 5)
f2 = Fraction(3, 5)

f3 = f1.sum(f2)

f3.display()"""

#Add two money amount

"""class Money:
    def __init__(self, rupees, paise):
        self.rupees = rupees
        self.paise = paise

    def sum(self, m2):
        m = Money(0, 0)

        m.paise = self.paise + m2.paise
        m.rupees = self.rupees + m2.rupees

        if m.paise >= 100:
            m.paise = m.paise - 100
            m.rupees = m.rupees + 1

        return m

    def display(self):
        print("Amount: ₹", self.rupees, ".", self.paise)


m1 = Money(2500, 50)
m2 = Money(1750, 75)

m3 = m1.sum(m2)

m3.display()"""

#Add two marks

"""class Marks:
    def __init__(self, theory, practical):
        self.theory = theory
        self.practical = practical

    def sum(self, m2):
        m = Marks(0, 0)

        m.theory = self.theory + m2.theory
        m.practical = self.practical + m2.practical

        return m

    def display(self):
        print("Theory:", self.theory)
        print("Practical:", self.practical)


m1 = Marks(70, 25)
m2 = Marks(65, 28)

m3 = m1.sum(m2)

m3.display()"""

# Add two length

"""class Length:
    def __init__(self, feet, inch):
        self.feet = feet
        self.inch = inch

    def sum(self, l2):
        l = Length(0, 0)

        l.inch = self.inch + l2.inch
        l.feet = self.feet + l2.feet

        if l.inch >= 12:
            l.inch = l.inch - 12
            l.feet = l.feet + 1

        return l

    def display(self):
        print("Length:", self.feet, "feet", self.inch, "inch")


l1 = Length(5, 8)
l2 = Length(3, 7)

l3 = l1.sum(l2)

l3.display()"""

#Add two weigth

"""class Weight:
    def __init__(self, kg, gram):
        self.kg = kg
        self.gram = gram

    def sum(self, w2):
        w = Weight(0, 0)

        w.gram = self.gram + w2.gram
        w.kg = self.kg + w2.kg

        if w.gram >= 1000:
            w.gram = w.gram - 1000
            w.kg = w.kg + 1

        return w

    def display(self):
        print("Weight:", self.kg, "kg", self.gram, "gram")


w1 = Weight(12, 750)
w2 = Weight(8, 500)

w3 = w1.sum(w2)

w3.display()"""

#Add two salaries

"""class Salary:
    def __init__(self, basic, allowance):
        self.basic = basic
        self.allowance = allowance

    def sum(self, s2):
        s = Salary(0, 0)

        s.basic = self.basic + s2.basic
        s.allowance = self.allowance + s2.allowance

        return s

    def display(self):
        print("Basic Salary:", self.basic)
        print("Allowance:", self.allowance)
        print("Total:", self.basic + self.allowance)


s1 = Salary(25000, 5000)
s2 = Salary(20000, 4000)

s3 = s1.sum(s2)

s3.display()"""

#Add two temperature

"""class Temperature:
    def __init__(self, celsius, fahrenheit):
        self.celsius = celsius
        self.fahrenheit = fahrenheit

    def sum(self, t2):
        t = Temperature(0, 0)

        t.celsius = self.celsius + t2.celsius
        t.fahrenheit = self.fahrenheit + t2.fahrenheit

        return t

    def display(self):
        print("Celsius:", self.celsius)
        print("Fahrenheit:", self.fahrenheit)


t1 = Temperature(25, 77)
t2 = Temperature(30, 86)

t3 = t1.sum(t2)

t3.display()"""
