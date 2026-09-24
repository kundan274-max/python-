# # Create a Class and Object 
# ## Create a class Student and take student name from user.

# class Student:
#     def display(self):
#         print("Student Name:", self.name)


# s = Student()

# s.name = input("Enter student name: ")

# s.display()
# # Constructor with User Input 
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)


# name = input("Enter name: ")
# age = int(input("Enter age: "))

# s = Student(name, age)

# s.display()

# # Student Details

# class Student:
#     def __init__(self, name, roll, marks):
#         self.name = name
#         self.roll = roll
#         self.marks = marks

#     def display(self):
#         print("Name:", self.name)
#         print("Roll:", self.roll)
#         print("Marks:", self.marks)


# name = input("Enter name: ")
# roll = int(input("Enter roll number: "))
# marks = float(input("Enter marks: "))

# s = Student(name, roll, marks)
# s.display()

# # Add Two Numbers Using Class 
# class Calculator:
#     def add(self, a, b):
#         return a + b


# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# c = Calculator()

# print("Sum =", c.add(a, b))

# # Calculator Using Class 
# class Calculator:
#     def add(self, a, b):
#         return a + b

#     def subtract(self, a, b):
#         return a - b

#     def multiply(self, a, b):
#         return a * b

#     def divide(self, a, b):
#         return a / b


# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))

# c = Calculator()

# print("Addition =", c.add(a, b))
# print("Subtraction =", c.subtract(a, b))
# print("Multiplication =", c.multiply(a, b))
# print("Division =", c.divide(a, b))
# # Check Even or Odd Using Class
# class Number:
#     def check(self, n):
#         if n % 2 == 0:
#             print("Even")
#         else:
#             print("Odd")


# n = int(input("Enter number: "))

# obj = Number()
# obj.check(n)
# # Find Factorial Using Class 
# class Number:
#     def factorial(self, n):
#         fact = 1

#         for i in range(1, n + 1):
#             fact = fact * i

#         return fact


# n = int(input("Enter number: "))

# obj = Number()

# print("Factorial =", obj.factorial(n))
# # Find Largest of Two Numbers
# class Number:
#     def largest(self, a, b):
#         if a > b:
#             return a
#         else:
#             return b


# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# obj = Number()

# print("Largest =", obj.largest(a, b))
# # Find Largest of Three Numbers 
# class Number:
#     def largest(self, a, b, c):
#         if a >= b and a >= c:
#             return a
#         elif b >= a and b >= c:
#             return b
#         else:
#             return c


# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# obj = Number()

# print("Largest =", obj.largest(a, b, c))
# # Check Palindrome Using Class
# class String:
#     def palindrome(self, text):
#         if text == text[::-1]:
#             print("Palindrome")
#         else:
#             print("Not Palindrome")


# text = input("Enter a string: ")

# obj = String()
# obj.palindrome(text)
# #Inheritance 
# # # Simple Inheritance
# class Parent:
#     def show(self):
#         print("This is Parent class")


# class Child(Parent):
#     def display(self):
#         print("This is Child class")


# obj = Child()

# obj.show()
# obj.display()
# # Inheritance with User Input
# class Person:
#     def get_name(self):
#         self.name = input("Enter name: ")


# class Student(Person):
#     def display(self):
#         print("Student Name:", self.name)


# s = Student()

# s.get_name()
# s.display()
# # Student Result Using Inheritance 
# class Student:
#     def get_data(self):
#         self.name = input("Enter name: ")
#         self.marks = float(input("Enter marks: "))


# class Result(Student):
#     def display(self):
#         print("Name:", self.name)
#         print("Marks:", self.marks)

#         if self.marks >= 40:
#             print("Result: Pass")
#         else:
#             print("Result: Fail")


# r = Result()

# r.get_data()
# r.display()
# ## Encapsulation
# # Private Variable 
# class Student:
#     def __init__(self):
#         self.__marks = int(input("Enter marks: "))

#     def display(self):
#         print("Marks:", self.__marks)


# s = Student()

# s.display()


# # Getter and Setter 
# class Student:
#     def __init__(self):
#         self.__marks = 0

#     def set_marks(self, marks):
#         self.__marks = marks

#     def get_marks(self):
#         return self.__marks


# s = Student()

# marks = int(input("Enter marks: "))

# s.set_marks(marks)

# print("Marks =", s.get_marks())
# # Polymorphism
# # Method Overriding
# class Animal:
#     def sound(self):
#         print("Animal makes sound")


# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")


# obj = Dog()

# obj.sound()
# # Polymorphism with Two Classes
# class Dog:
#     def sound(self):
#         print("Dog says Woof")


# class Cat:
#     def sound(self):
#         print("Cat says Meow")


# d = Dog()
# c = Cat()

# d.sound()
# c.sound()
# #More Practical Questions
# # Bank Account Program 
# class Bank:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance = self.balance + amount

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance = self.balance - amount
#         else:
#             print("Insufficient balance")

#     def display(self):
#         print("Account Holder:", self.name)
#         print("Balance:", self.balance)


# name = input("Enter account holder name: ")
# balance = float(input("Enter initial balance: "))

# b = Bank(name, balance)

# deposit = float(input("Enter deposit amount: "))
# b.deposit(deposit)

# withdraw = float(input("Enter withdrawal amount: "))
# b.withdraw(withdraw)

# b.display()
# # Employee Salary Program
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def display(self):
#         print("Employee Name:", self.name)
#         print("Salary:", self.salary)


# name = input("Enter employee name: ")
# salary = float(input("Enter salary: "))

# e = Employee(name, salary)

# e.display()
# # Area of Circle Using Class 

# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
#         def area(self):
#             return 3.14 * self.radius * self.radius
# radius = float(input("enter radius:"))
# c = Circle(radius)
# print("Area of circle=",c.area())
#complex number
class Complex:
    def getdata(self)
       self.r = int(input("enter real number: "))
       self.i = int(input("enter imaginary : "))
    def calculate(self.c2):
          self.r = self.r + c2.r
          self.i =  self.i + c2.i
     def display(self):
         print("Real number : ", self.r)
         print("imaginary number : ", self.i)
         print(self.r,"+",self.i,"i")
         c1.Complex()
         c2.Complex()
         c1.getdata()
         c2.getdata()
         c1.sum(c2)
         c1.display()
              
