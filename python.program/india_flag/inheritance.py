"""class A:
    def getdata1(self):
        self.x = int(input("enter value of x: "))
        self.y = int(input("enter value of y: "))


class B(A):
    def getdata2(self):
        self.m = int(input("enter value of m: "))

    def calculate(self):
        self.z = self.x * self.y + self.m

    def display(self):
        print("result=", self.z)


obj = B()
obj.getdata1()
obj.getdata2()
obj.calculate()
obj.display()"""

"""class A:
    def getdata1(self):
        self.x = int(input("enter value of x: "))
        self.y = int(input("enter value of y: "))


class B:
    def getdata2(self):
        self.z = int(input("enter value of z: "))


class C (A,B):
    def getdata3(self):
        self.m = int(input("enter value of m: "))
    def calculate(self):
        self.r = self.x + self.y * self.z + self.m
    def display(self):
        print("result = ",self.r)


obj = C()
obj.getdata1()
obj.getdata2()
obj.getdata3()
obj.calculate()
obj.display()"""


class A:
    def getdata1(self):
        self.x = int(input("enter the value of x: "))


class B:
    def getdata2(self):
        self.y = int(input("enter the value of y: "))


class C:
    def getdata3(self):
        self.z = int(input("enter the value of z: "))


class D(A, B, C):
    def getdata4(self):
        self.m = int(input("enter the value of m: "))
