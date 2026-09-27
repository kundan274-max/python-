"""class Student:

    #default constructor
    def __init__(self):
        pass

    def __init__(self,name, marks):
       # print(self)
    #    self.name = fullname
    #    print("hey kundan i am here")
        self.name = name
        self.marks = marks
s1= Student("kumar",78) 
print(s1.name, s1.marks) #kundan
s2 = Student("kundan",88)
print(s2.name, s2.marks)      

class Kundan:
    name = "kundan kumar"
s1 = Kundan()
print(s1.name)



class Car:
    color = "blue"
    brand = "mercidies"
car1 = Car()
print(car1.color)
print(car1.brand)"""


# encapsulation


# 1. BankAccount — Private Balance

"""class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited successfully.")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount.")

    def show_balance(self):
        print("Current Balance:", self.__balance)


balance = float(input("Enter initial balance: "))

account = BankAccount(balance)

account.show_balance()

deposit = float(input("Enter amount to deposit: "))
account.deposit(deposit)

withdraw = float(input("Enter amount to withdraw: "))
account.withdraw(withdraw)

account.show_balance()"""

# 2. Student — @property with Validation

"""class Student:
    def __init__(self, marks):
        self.marks = marks

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self.__marks = value
        else:
            print("Marks must be between 0 and 100.")
            self.__marks = 0


marks = float(input("Enter student marks: "))

student = Student(marks)

print("Marks:", student.marks)

new_marks = float(input("Enter new marks: "))
student.marks = new_marks

print("Updated Marks:", student.marks)"""

# Main concept:

# @property → value get karne ke liye
# @marks.setter → value set/change karne ke liye

#3. Employee — Private Salary

"""class Employee:
    def __init__(self, salary):
        self.salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value >= 0:
            self.__salary = value
        else:
            print("Salary cannot be negative.")
            self.__salary = 0


salary = float(input("Enter employee salary: "))

employee = Employee(salary)

print("Salary:", employee.salary)

new_salary = float(input("Enter new salary: "))
employee.salary = new_salary

print("Updated Salary:", employee.salary)"""


# Negative salary dene par:

# Salary cannot be negative.
#4. Automatically Generate Unique ID

"""class Student:
    count = 0

    def __init__(self, name):
        Student.count += 1
        self.id = Student.count
        self.name = name

    def show(self):
        print("ID:", self.id)
        print("Name:", self.name)


name1 = input("Enter first student name: ")
name2 = input("Enter second student name: ")
name3 = input("Enter third student name: ")

s1 = Student(name1)
s2 = Student(name2)
s3 = Student(name3)

print("\nStudent Details")

s1.show()
print()

s2.show()
print()

s3.show()"""

# 5. PasswordManager — Private Password
"""class PasswordManager:
    def __init__(self, password):
        self.__password = password

    def change_password(self, old_password, new_password):
        if old_password == self.__password:
            if len(new_password) >= 6:
                self.__password = new_password
                print("Password changed successfully.")
            else:
                print("New password must contain at least 6 characters.")
        else:
            print("Old password is incorrect.")

    def check_password(self, password):
        if password == self.__password:
            print("Correct password.")
        else:
            print("Wrong password.")


password = input("Create password: ")

manager = PasswordManager(password)

old = input("Enter old password: ")
new = input("Enter new password: ")

manager.change_password(old, new)

check = input("Enter password to check: ")
manager.check_password(check)"""


# Yahan password directly access nahi kiya ja sakta:

# manager.__password

# 6. Temperature — Celsius & Fahrenheit

"""class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        if value >= -273.15:
            self.__celsius = value
        else:
            print("Invalid temperature.")
            self.__celsius = 0

    @property
    def fahrenheit(self):
        return (self.__celsius * 9 / 5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.__celsius = (value - 32) * 5 / 9


c = float(input("Enter temperature in Celsius: "))

temp = Temperature(c)

print("Celsius:", temp.celsius)
print("Fahrenheit:", temp.fahrenheit)

f = float(input("Enter new temperature in Fahrenheit: "))

temp.fahrenheit = f

print("\nUpdated Temperature")
print("Celsius:", temp.celsius)
print("Fahrenheit:", temp.fahrenheit)"""

# 7. ShoppingCart — Private Product List

"""class ShoppingCart:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)
        print(product, "added to cart.")

    def remove_product(self, product):
        if product in self.__products:
            self.__products.remove(product)
            print(product, "removed from cart.")
        else:
            print("Product not found.")

    def show_cart(self):
        print("Shopping Cart:")
        for product in self.__products:
            print("-", product)


cart = ShoppingCart()

n = int(input("How many products do you want to add? "))

for i in range(n):
    product = input("Enter product name: ")
    cart.add_product(product)

cart.show_cart()

remove = input("\nEnter product to remove: ")
cart.remove_product(remove)

cart.show_cart()"""

#_products private hai, so outside se directly modify nahi karna chahiye.

# 8. __slots__ — New Attributes Not Allowed
"""class Student:
    __slots__ = ["name", "age"]

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)


name = input("Enter student name: ")
age = int(input("Enter student age: "))

student = Student(name, age)

student.show()

student.city = input("Enter city: ")"""

# Last line par error aayega:

# AttributeError

# Kyuki __slots__ me sirf:

# name
# age

# allowed hain.

# 9. Immutable Class
"""class Student:
    def __init__(self, name, age):
        object.__setattr__(self, "name", name)
        object.__setattr__(self, "age", age)

    def __setattr__(self, name, value):
        raise AttributeError("Object is immutable")

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)


name = input("Enter student name: ")
age = int(input("Enter student age: "))

student = Student(name, age)

student.show()

new_name = input("Enter new name: ")

student.name = new_name"""

# Last line par:

# AttributeError: Object is immutable

# Matlab object banne ke baad attributes change nahi kiye ja sakte.

# 10. Public, Protected & Private Attributes
"""class User:
    def __init__(self, name, email, password):
        self.name = name
        self._email = email
        self.__password = password

    def show(self):
        print("Name:", self.name)
        print("Email:", self._email)
        print("Password:", self.__password)


name = input("Enter name: ")
email = input("Enter email: ")
password = input("Enter password: ")

user = User(name, email, password)

print("\nInside class:")
user.show()

print("\nOutside class:")

print("Public Name:", user.name)

print("Protected Email:", user._email)"""

# B. Inheritance & Polymorphism
# 11. Vehicle → Car → ElectricCar

"""class Vehicle:
    def start(self):
        print("Vehicle is starting.")


class Car(Vehicle):
    def start(self):
        print("Car is starting with a key.")


class ElectricCar(Car):
    def start(self):
        print("Electric car is starting silently.")


choice = input("Enter vehicle type (vehicle/car/electric): ").lower()

if choice == "vehicle":
    obj = Vehicle()
elif choice == "car":
    obj = Car()
elif choice == "electric":
    obj = ElectricCar()
else:
    print("Invalid choice")
    obj = None

if obj:
    obj.start()"""


#Concept: Method overriding + multilevel inheritance.

# 12. Animal → Dog, Cat, Cow Polymorphism

"""class Animal:
    def sound(self):
        print("Animal makes a sound.")


class Dog(Animal):
    def sound(self):
        print("Dog says: Woof Woof")


class Cat(Animal):
    def sound(self):
        print("Cat says: Meow")


class Cow(Animal):
    def sound(self):
        print("Cow says: Moo")


animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.sound()"""


# 13. Shape — Circle, Rectangle, Triangle


"""import math
class Shape:
    def area(self):
        print("Area is not defined.")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


r = float(input("Enter circle radius: "))
l = float(input("Enter rectangle length: "))
w = float(input("Enter rectangle width: "))
b = float(input("Enter triangle base: "))
h = float(input("Enter triangle height: "))

shapes = [
    Circle(r),
    Rectangle(l, w),
    Triangle(b, h)
]

for shape in shapes:
    print("Area:", round(shape.area(), 2))"""

# 14. Employee → Developer, Manager, Designer

"""class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary


class Developer(Employee):
    def calculate_salary(self):
        return self.salary + 5000


class Manager(Employee):
    def calculate_salary(self):
        return self.salary + 10000


class Designer(Employee):
    def calculate_salary(self):
        return self.salary + 3000


name = input("Enter employee name: ")
salary = float(input("Enter basic salary: "))
role = input("Enter role (developer/manager/designer): ").lower()

if role == "developer":
    employee = Developer(name, salary)
elif role == "manager":
    employee = Manager(name, salary)
elif role == "designer":
    employee = Designer(name, salary)
else:
    print("Invalid role")
    employee = None

if employee:
    print("Employee:", employee.name)
    print("Final Salary:", employee.calculate_salary())"""

# 15. Multiple Inheritance — SmartPhone
"""class Phone:
    def call(self):
        print("Phone is making a call.")
class Camera:
    def take_photo(self):
        print("Camera is taking a photo.")

class SmartPhone(Phone, Camera):
    def use_phone(self):
        print("SmartPhone is ready to use.")

phone = SmartPhone()

phone.use_phone()
phone.call()
phone.take_photo()"""


# Concept: SmartPhone inherits from both Phone and Camera.

# 16. Diamond Inheritance + MRO

"""class A:
    def show(self):
        print("A class")


class B(A):
    def show(self):
        print("B class")
        super().show()


class C(A):
    def show(self):
        print("C class")
        super().show()


class D(B, C):
    def show(self):
        print("D class")
        super().show()


obj = D()

obj.show()

print("\nMRO:")
print(D.mro())"""

# 17. Three-Level Inheritance + super()

"""class A:
    def show(self):
        print("A class method")


class B(A):
    def show(self):
        print("B class method")
        super().show()


class C(B):
    def show(self):
        print("C class method")
        super().show()


obj = C()

obj.show()
Output
C class method
B class method
A class method"""


# super() parent class ke method ko call karta hai.

# 18. Person → Student → CollegeStudent

"""class Person:
    def __init__(self, name):
        self.name = name
        print("Person constructor called")


class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll
        print("Student constructor called")


class CollegeStudent(Student):
    def __init__(self, name, roll, college):
        super().__init__(name, roll)
        self.college = college
        print("CollegeStudent constructor called")

    def show(self):
        print("\nName:", self.name)
        print("Roll No:", self.roll)
        print("College:", self.college)


name = input("Enter name: ")
roll = input("Enter roll number: ")
college = input("Enter college name: ")

student = CollegeStudent(name, roll, college)

student.show()"""

# 19. Parent Method Calls Overridden Child Method

"""class Parent:
    def display(self):
        print("Parent display method")

    def start(self):
        print("Parent start method")
        self.display()


class Child(Parent):
    def display(self):
        print("Child display method")


obj = Child()

obj.start()"""


# 20. Multiple Inheritance — Same Method Name

"""class Father:
    def show(self):
        print("Father class")


class Mother:
    def show(self):
        print("Mother class")


class Child(Father, Mother):
    pass


obj = Child()

obj.show()

print("\nMRO:")
print(Child.mro())"""

# Python pehle Father me show() search karega because:

# Child → Father → Mother → object
# C. Magic / Dunder Methods

# 21. ComplexNumber — +, -, *, /

"""class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(
            self.real + other.real,
            self.imag + other.imag
        )

    def __sub__(self, other):
        return ComplexNumber(
            self.real - other.real,
            self.imag - other.imag
        )

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real, imag)

    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imag ** 2

        real = (self.real * other.real + self.imag * other.imag) / denominator
        imag = (self.imag * other.real - self.real * other.imag) / denominator

        return ComplexNumber(real, imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"


r1 = float(input("Enter real part of first number: "))
i1 = float(input("Enter imaginary part of first number: "))

r2 = float(input("Enter real part of second number: "))
i2 = float(input("Enter imaginary part of second number: "))

c1 = ComplexNumber(r1, i1)
c2 = ComplexNumber(r2, i2)

print("Addition:", c1 + c2)
print("Subtraction:", c1 - c2)
print("Multiplication:", c1 * c2)
print("Division:", c1 / c2)"""

# 22. Vector — +, -, *

"""class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __str__(self):
        return f"({self.x}, {self.y})"


x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))

x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

scalar = float(input("Enter scalar: "))

v1 = Vector(x1, y1)
v2 = Vector(x2, y2)

print("v1 + v2 =", v1 + v2)
print("v1 - v2 =", v1 - v2)
print("v1 * scalar =", v1 * scalar)"""

# 23. BankAccount — Comparison Operators

"""class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __ge__(self, other):
        return self.balance >= other.balance


b1 = float(input("Enter first account balance: "))
b2 = float(input("Enter second account balance: "))

account1 = BankAccount(b1)
account2 = BankAccount(b2)

print("Equal:", account1 == account2)
print("Less than:", account1 < account2)
print("Greater than:", account1 > account2)
print("Less or equal:", account1 <= account2)
print("Greater or equal:", account1 >= account2)"""

# 24. __str__() vs __repr__()

"""class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def __str__(self):
        return f"Student Name: {self.name}, Roll: {self.roll}"

    def __repr__(self):
        return f"Student('{self.name}', {self.roll})"


name = input("Enter student name: ")
roll = int(input("Enter roll number: "))

student = Student(name, roll)

print("Using str():")
print(str(student))

print("\nUsing repr():")
print(repr(student))"""

# Difference:

# __str__() → user-friendly representation
# __repr__() → developer/debugging representation

# 25. Book — len(book)

"""class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __len__(self):
        return self.pages


title = input("Enter book title: ")
pages = int(input("Enter number of pages: "))

book = Book(title, pages)

print("Book:", book.title)
print("Number of pages:", len(book))"""

# 26. ShoppingCart — len, indexing, in, +

"""class ShoppingCart:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __contains__(self, item):
        return item in self.items

    def __add__(self, other):
        return ShoppingCart(self.items + other.items)

    def show(self):
        print(self.items)


cart1 = ShoppingCart(["Shirt", "Shoes", "Watch"])
cart2 = ShoppingCart(["Bag", "Cap"])

print("Cart 1:")
cart1.show()

print("\nNumber of items:", len(cart1))

print("First item:", cart1[0])

item = input("Enter item to search: ")

if item in cart1:
    print("Item is present.")
else:
    print("Item is not present.")

cart3 = cart1 + cart2

print("\nCombined cart:")
cart3.show()"""

# 27. Matrix — Matrix Addition

"""class Matrix:
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        result = []

        for i in range(len(self.data)):
            row = []

            for j in range(len(self.data[0])):
                row.append(
                    self.data[i][j] + other.data[i][j]
                )

            result.append(row)

        return Matrix(result)

    def show(self):
        for row in self.data:
            print(row)


rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("\nEnter first matrix:")

matrix1 = []

for i in range(rows):
    row = []

    for j in range(cols):
        value = int(input(f"Enter element [{i}][{j}]: "))
        row.append(value)

    matrix1.append(row)


print("\nEnter second matrix:")

matrix2 = []

for i in range(rows):
    row = []

    for j in range(cols):
        value = int(input(f"Enter element [{i}][{j}]: "))
        row.append(value)

    matrix2.append(row)


m1 = Matrix(matrix1)
m2 = Matrix(matrix2)

result = m1 + m2

print("\nResult:")
result.show()"""

# 28. Fraction — +, -, *, /

"""from math import gcd
class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")

        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        n = self.numerator * other.denominator
        n += other.numerator * self.denominator

        d = self.denominator * other.denominator

        return Fraction(n, d)

    def __sub__(self, other):
        n = self.numerator * other.denominator
        n -= other.numerator * self.denominator

        d = self.denominator * other.denominator

        return Fraction(n, d)

    def __mul__(self, other):
        return Fraction(
            self.numerator * other.numerator,
            self.denominator * other.denominator
        )

    def __truediv__(self, other):
        return Fraction(
            self.numerator * other.denominator,
            self.denominator * other.numerator
        )

    def __str__(self):
        g = gcd(self.numerator, self.denominator)

        return f"{self.numerator // g}/{self.denominator // g}"


n1 = int(input("Enter numerator 1: "))
d1 = int(input("Enter denominator 1: "))

n2 = int(input("Enter numerator 2: "))
d2 = int(input("Enter denominator 2: "))

f1 = Fraction(n1, d1)
f2 = Fraction(n2, d2)

print("Addition:", f1 + f2)
print("Subtraction:", f1 - f2)
print("Multiplication:", f1 * f2)
print("Division:", f1 / f2)"""

# 29. Employee — __eq__() and __hash__()

"""class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def __eq__(self, other):
        return self.emp_id == other.emp_id

    def __hash__(self):
        return hash(self.emp_id)

    def __str__(self):
        return f"{self.emp_id} - {self.name}"


id1 = int(input("Enter first employee ID: "))
name1 = input("Enter first employee name: ")

id2 = int(input("Enter second employee ID: "))
name2 = input("Enter second employee name: ")

id3 = int(input("Enter third employee ID: "))
name3 = input("Enter third employee name: ")

e1 = Employee(id1, name1)
e2 = Employee(id2, name2)
e3 = Employee(id3, name3)

employees = {e1, e2, e3}

print("\nEmployees in set:")

for employee in employees:
    print(employee)

print("\nTotal unique employees:", len(employees))"""


# Yahan employees ki equality emp_id ke basis par check ho rahi hai.

# 30. CustomList — Indexing, Slicing, Iteration, len(), in

"""class CustomList:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]

    def __iter__(self):
        return iter(self.items)

    def __len__(self):
        return len(self.items)

    def __contains__(self, item):
        return item in self.items


n = int(input("How many items do you want to enter? "))

items = []

for i in range(n):
    value = input(f"Enter item {i + 1}: ")
    items.append(value)


my_list = CustomList(items)

print("\nComplete list:")
print(list(my_list))

print("\nLength:", len(my_list))

index = int(input("\nEnter index: "))
print("Item:", my_list[index])

start = int(input("Enter slice starting index: "))
end = int(input("Enter slice ending index: "))

print("Slice:", my_list[start:end])

search = input("\nEnter item to search: ")

if search in my_list:
    print("Item found.")
else:
    print("Item not found.")

print("\nIterating through list:")

for item in my_list:
    print(item)"""


# D. Abstract Classes
# 31. Abstract Shape — Circle, Square, Rectangle

"""from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


r = float(input("Enter circle radius: "))
s = float(input("Enter square side: "))
l = float(input("Enter rectangle length: "))
w = float(input("Enter rectangle width: "))

shapes = [
    Circle(r),
    Square(s),
    Rectangle(l, w)
]

for shape in shapes:
    print("Area:", shape.area())"""

# Concept: Shape abstract class hai aur area() abstract method hai. Har child class ko area() implement karna compulsory hai.

# 32. Abstract Payment — UPI, CreditCard, NetBanking

"""from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
class UPI(Payment):
    def pay(self, amount):
        print("Paid ₹", amount, "using UPI.")

class CreditCard(Payment):
    def pay(self, amount):
        print("Paid ₹", amount, "using Credit Card.")

class NetBanking(Payment):
    def pay(self, amount):
        print("Paid ₹", amount, "using Net Banking.")

amount = float(input("Enter amount: "))
choice = input("Enter payment method (upi/card/netbanking): ").lower()

if choice == "upi":
    payment = UPI()
elif choice == "card":
    payment = CreditCard()
elif choice == "netbanking":
    payment = NetBanking()
else:
    print("Invalid payment method.")
    payment = None

if payment:
    payment.pay(amount)"""

# 33. Abstract Database

"""from abc import ABC, abstractmethod
class Database(ABC):
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def insert(self, data):
        pass
    @abstractmethod
    def delete(self, data):
        pass

class MySQL(Database):
    def connect(self):
        print("Connected to MySQL database.")

    def insert(self, data):
        print(data, "inserted into MySQL.")

    def delete(self, data):
        print(data, "deleted from MySQL.")

db = MySQL()
data = input("Enter data: ")
db.connect()
db.insert(data)
db.delete(data)"""

# Yahan MySQL ko parent ke teeno abstract methods implement karne pade.

# 34. Abstract Employee — Salary Calculation

"""from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    @abstractmethod
    def calculate_salary(self):
        pass
class Developer(Employee):
    def calculate_salary(self):
        return self.salary + 5000

class Manager(Employee):
    def calculate_salary(self):
        return self.salary + 10000
class Designer(Employee):
    def calculate_salary(self):
        return self.salary + 3000
name = input("Enter employee name: ")
salary = float(input("Enter basic salary: "))
role = input("Enter role: ").lower()
if role == "developer":
    employee = Developer(name, salary)
elif role == "manager":
    employee = Manager(name, salary)
elif role == "designer":
    employee = Designer(name, salary)
else:
    print("Invalid role.")
    employee = None

if employee:
    print("Name:", employee.name)
    print("Final Salary:", employee.calculate_salary())"""

# 35. Creating Object of Abstract Class

"""from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

animal = Animal()"""

# Output:
# TypeError: Can't instantiate abstract class Animal
# with abstract method sound
# Why?

# Animal me sound() abstract method hai, isliye directly:

# Animal()

# ka object nahi bana sakte.

# 36. Abstract Notification

"""from abc import ABC, abstractmethod
class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass
class EmailNotification(Notification):
    def send(self, message):
        print("Email:", message)
class SMSNotification(Notification):

    def send(self, message):
        print("SMS:", message)

class PushNotification(Notification):
    def send(self, message):
        print("Push Notification:", message)

message = input("Enter notification message: ")
choice = input("Enter type (email/sms/push): ").lower()

if choice == "email":
    notification = EmailNotification()
elif choice == "sms":
    notification = SMSNotification()
elif choice == "push":
    notification = PushNotification()
else:
    print("Invalid choice.")
    notification = None

if notification:
    notification.send(message)"""

# 37. Interface-like System Using ABC

# Python me Java jaisa separate interface keyword nahi hota. ABC ka use karke interface-like contract bana sakte hain.

"""from abc import ABC, abstractmethod
class PaymentSystem(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
    @abstractmethod
    def refund(self, amount):
        pass
class UPI(PaymentSystem):
    def pay(self, amount):
        print("UPI payment:", amount)
    def refund(self, amount):
        print("UPI refund:", amount)
class Card(PaymentSystem):
    def pay(self, amount):
        print("Card payment:", amount)

    def refund(self, amount):
        print("Card refund:", amount)

class Wallet(PaymentSystem):
    def pay(self, amount):
        print("Wallet payment:", amount)

    def refund(self, amount):
        print("Wallet refund:", amount)
amount = float(input("Enter amount: "))
payments = [
    UPI(),
    Card(),
    Wallet()
]

for payment in payments:
    payment.pay(amount)
    payment.refund(amount)"""


# Main idea: Sabhi classes ko pay() aur refund() methods provide karne hi padenge.

# E. Class Methods, Static Methods & Decorators

# 38. @classmethod — Object from String

# String:
# Rahul,50000,IT
# ko object me convert karenge.

"""class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department
    @classmethod
    def from_string(cls, data):
        name, salary, department = data.split(",")
        return cls(
            name,
            float(salary),
            department
        )
    def show(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Department:", self.department)

data = input("Enter employee details (Name,Salary,Department): ")

employee = Employee.from_string(data)

employee.show()"""
# 39. Date Class — Three Class Methods

"""from datetime import datetime
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    @classmethod
    def from_string(cls, date_string):
        date = datetime.strptime(date_string, "%d-%m-%Y")
        return cls(
            date.day,
            date.month,
            date.year
        )
    @classmethod
    def from_timestamp(cls, timestamp):
        date = datetime.fromtimestamp(timestamp)
        return cls(
            date.day,
            date.month,
            date.year
        )
    @classmethod
    def from_today(cls):
        date = datetime.today()
        return cls(
            date.day,
            date.month,
            date.year
        )
    def show(self):
        print(
            f"{self.day:02d}-{self.month:02d}-{self.year}"
        )
date_string = input("Enter date (DD-MM-YYYY): ")

d1 = Date.from_string(date_string)

print("From string:")
d1.show()
timestamp = float(input("\nEnter timestamp: "))
d2 = Date.from_timestamp(timestamp)

print("From timestamp:")
d2.show()
d3 = Date.from_today()
print("Today's date:")
d3.show()"""

# 40. Counter — Total Objects

"""class Counter:
    total_objects = 0
    def __init__(self):
        Counter.total_objects += 1
    @classmethod
    def show_count(cls):
        print("Total objects created:", cls.total_objects)
n = int(input("How many objects do you want to create? "))
objects = []
for i in range(n):
    objects.append(Counter())
Counter.show_count()"""

# 41. @staticmethod — Salary Validation

"""class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @staticmethod
    def validate_salary(salary):
        if salary >= 0:
            return True
        return False

    def show(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


name = input("Enter employee name: ")
salary = float(input("Enter salary: "))

if Employee.validate_salary(salary):
    employee = Employee(name, salary)
    employee.show()
else:
    print("Invalid salary.")"""

# Difference: Static method ko object ke data ki zarurat nahi hoti.

# 42. Temperature — Celsius & Fahrenheit using @property

"""class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        self.__celsius = value

    @property
    def fahrenheit(self):
        return (self.__celsius * 9 / 5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.__celsius = (value - 32) * 5 / 9


celsius = float(input("Enter temperature in Celsius: "))

temp = Temperature(celsius)

print("Celsius:", temp.celsius)
print("Fahrenheit:", temp.fahrenheit)

new_celsius = float(input("\nEnter new Celsius value: "))

temp.celsius = new_celsius

print("Updated Celsius:", temp.celsius)
print("Updated Fahrenheit:", temp.fahrenheit)"""


# 43. Custom Decorator — Log Class Method

"""def log_method(func):
    def wrapper(*args, **kwargs):
        print("Calling method:", func.__name__)
        result = func(*args, **kwargs)
        return result
    return wrapper

class Student:

    def __init__(self, name):
        self.name = name

    @log_method
    def show(self):
        print("Student name:", self.name)

name = input("Enter student name: ")

student = Student(name)

student.show()"""

# Output
# Calling method: show
# Student name: Kundan

# Decorator method execute hone se pehle method ka naam print karta hai.

# 44. Decorator — Execution Time

"""import time
def calculate_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Execution time:",
              round(end - start, 6),
              "seconds")
        return result
    return wrapper
class Calculator:
    @calculate_time
    def calculate(self, number):
        total = 0
        for i in range(number):
            total += i
        print("Calculation completed.")
number = int(input("Enter a number: "))
calculator = Calculator()
calculator.calculate(number)"""

# Yahan decorator method ke execution se pehle aur baad ka time measure karta hai.

# 45. Decorator — Retry Up to 3 Times

"""def retry(func):
    def wrapper(*args, **kwargs):
        for attempt in range(1, 4):
            try:
                return func(*args, **kwargs)
            except Exception as error:
                print(
                    "Attempt",
                    attempt,
                    "failed:",
                    error
                )

        print("All 3 attempts failed.")

    return wrapper
class Calculator:
    @retry
    def divide(self):

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        print("Result:", a / b)


calculator = Calculator()

calculator.divide()"""


