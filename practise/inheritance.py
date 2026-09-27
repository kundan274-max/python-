## single inheritance

#student marks
"""class Student:
    def get_student(self):
        self.name = input("Enter student name: ")
        self.roll = int(input("Enter roll number: "))

class Marks(Student):
    def get_marks(self):
        self.marks = float(input("Enter marks: "))

    def display(self):
        print("\nStudent Name:", self.name)
        print("Roll Number:", self.roll)
        print("Marks:", self.marks)


obj = Marks()
obj.get_student()
obj.get_marks()
obj.display()"""

# person employee
"""class Person:
    def get_person(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))

class Employee(Person):
    def get_employee(self):
        self.salary = float(input("Enter salary: "))

    def display(self):
        print("\nName:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)


obj = Employee()
obj.get_person()
obj.get_employee()
obj.display()"""

#Animal dog

"""class Animal:
    def animal_info(self):
        self.name = input("Enter animal name: ")

class Dog(Animal):
    def dog_info(self):
        self.breed = input("Enter dog breed: ")

    def display(self):
        print("\nAnimal:", self.name)
        print("Breed:", self.breed)


obj = Dog()
obj.animal_info()
obj.dog_info()
obj.display()"""

# vehical car

"""class Vehicle:
    def get_vehicle(self):
        self.brand = input("Enter vehicle brand: ")

class Car(Vehicle):
    def get_car(self):
        self.model = input("Enter car model: ")
        self.price = float(input("Enter car price: "))

    def display(self):
        print("\nBrand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)


obj = Car()
obj.get_vehicle()
obj.get_car()
obj.display()"""



## multiple inheritance

# father & mother -> child

"""class Father:
    def father_info(self):
        self.father_name = input("Enter father's name: ")

class Mother:
    def mother_info(self):
        self.mother_name = input("Enter mother's name: ")

class Child(Father, Mother):
    def child_info(self):
        self.child_name = input("Enter child's name: ")

    def display(self):
        print("\nChild Name:", self.child_name)
        print("Father Name:", self.father_name)
        print("Mother Name:", self.mother_name)


obj = Child()
obj.father_info()
obj.mother_info()
obj.child_info()
obj.display()"""

# Marks& sport -> student

"""class Marks:
    def get_marks(self):
        self.marks = float(input("Enter marks: "))

class Sports:
    def get_score(self):
        self.score = float(input("Enter sports score: "))

class Student(Marks, Sports):
    def display(self):
        print("\nAcademic Marks:", self.marks)
        print("Sports Score:", self.score)


obj = Student()
obj.get_marks()
obj.get_score()
obj.display()"""


# basicsalary & bonus -> salary

"""class BasicSalary:
    def get_basic(self):
        self.basic = float(input("Enter basic salary: "))

class Bonus:
    def get_bonus(self):
        self.bonus = float(input("Enter bonus: "))

class Salary(BasicSalary, Bonus):
    def calculate(self):
        self.total = self.basic + self.bonus

    def display(self):
        print("Basic Salary:", self.basic)
        print("Bonus:", self.bonus)
        print("Total Salary:", self.total)


obj = Salary()
obj.get_basic()
obj.get_bonus()
obj.calculate()
obj.display()"""


# theory & practical -> result

"""class Theory:
    def get_theory(self):
        self.theory = float(input("Enter theory marks: "))

class Practical:
    def get_practical(self):
        self.practical = float(input("Enter practical marks: "))

class Result(Theory, Practical):
    def calculate(self):
        self.total = self.theory + self.practical

    def display(self):
        print("Theory:", self.theory)
        print("Practical:", self.practical)
        print("Total:", self.total)


obj = Result()
obj.get_theory()
obj.get_practical()
obj.calculate()
obj.display()"""


## multilevel inheritance

# Person → Student → Result
"""class Person:
    def get_name(self):
        self.name = input("Enter name: ")

class Student(Person):
    def get_roll(self):
        self.roll = int(input("Enter roll number: "))

class Result(Student):
    def get_marks(self):
        self.marks = float(input("Enter marks: "))

    def display(self):
        print("Name:", self.name)
        print("Roll:", self.roll)
        print("Marks:", self.marks)


obj = Result()
obj.get_name()
obj.get_roll()
obj.get_marks()
obj.display()"""


# Vehicle → Car → ElectricCar

"""class Vehicle:
    def get_brand(self):
        self.brand = input("Enter brand: ")

class Car(Vehicle):
    def get_model(self):
        self.model = input("Enter model: ")

class ElectricCar(Car):
    def get_battery(self):
        self.battery = int(input("Enter battery capacity: "))

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Battery:", self.battery, "kWh")


obj = ElectricCar()
obj.get_brand()
obj.get_model()
obj.get_battery()
obj.display()"""

# Employee → Manager → SeniorManager
"""class Employee:
    def get_employee(self):
        self.name = input("Enter employee name: ")

class Manager(Employee):
    def get_department(self):
        self.department = input("Enter department: ")

class SeniorManager(Manager):
    def get_salary(self):
        self.salary = float(input("Enter salary: "))

    def display(self):
        print("Name:", self.name)
        print("Department:", self.department)
        print("Salary:", self.salary)


obj = SeniorManager()
obj.get_employee()
obj.get_department()
obj.get_salary()
obj.display()"""

# Student → Exam → Result
"""class Student:
    def get_student(self):
        self.name = input("Enter name: ")

class Exam(Student):
    def get_exam(self):
        self.subject = input("Enter subject: ")

class Result(Exam):
    def get_marks(self):
        self.marks = float(input("Enter marks: "))

    def display(self):
        print("Name:", self.name)
        print("Subject:", self.subject)
        print("Marks:", self.marks)


obj = Result()
obj.get_student()
obj.get_exam()
obj.get_marks()
obj.display()"""

# HIERARCHICAL INHERITANCE


# Animal → Dog & Cat
"""class Animal:
    def get_name(self):
        self.name = input("Enter animal name: ")

class Dog(Animal):
    def show_dog(self):
        print("Dog Name:", self.name)
        print("Sound: Bark")

class Cat(Animal):
    def show_cat(self):
        print("Cat Name:", self.name)
        print("Sound: Meow")


dog = Dog()
dog.get_name()
dog.show_dog()

cat = Cat()
cat.get_name()
cat.show_cat()"""

# Person → Student & Teacher
"""class Person:
    def get_name(self):
        self.name = input("Enter name: ")

class Student(Person):
    def show_student(self):
        print("Student Name:", self.name)

class Teacher(Person):
    def show_teacher(self):
        print("Teacher Name:", self.name)


student = Student()
student.get_name()
student.show_student()

teacher = Teacher()
teacher.get_name()
teacher.show_teacher()"""

# Vehicle → Car & Bike

"""class Vehicle:
    def get_brand(self):
        self.brand = input("Enter brand: ")

class Car(Vehicle):
    def car_info(self):
        self.model = input("Enter car model: ")
        print("Car:", self.brand)
        print("Model:", self.model)

class Bike(Vehicle):
    def bike_info(self):
        self.model = input("Enter bike model: ")
        print("Bike:", self.brand)
        print("Model:", self.model)


car = Car()
car.get_brand()
car.car_info()

bike = Bike()
bike.get_brand()
bike.bike_info()"""

# Shape → Circle & Rectangle

"""class Shape:
    def get_name(self):
        self.name = input("Enter shape name: ")

class Circle(Shape):
    def area(self):
        radius = float(input("Enter radius: "))
        print("Circle Area:", 3.14 * radius * radius)

class Rectangle(Shape):
    def area(self):
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        print("Rectangle Area:", length * width)


circle = Circle()
circle.get_name()
circle.area()

rectangle = Rectangle()
rectangle.get_name()
rectangle.area()"""

#HYBRID INHERITANCE


# Hybrid Student Example

"""class Person:
    def get_name(self):
        self.name = input("Enter name: ")

class Student(Person):
    def get_roll(self):
        self.roll = int(input("Enter roll number: "))

class Sports:
    def get_sports(self):
        self.sports = input("Enter sports name: ")

class Result(Student, Sports):
    def get_marks(self):
        self.marks = float(input("Enter marks: "))

    def display(self):
        print("Name:", self.name)
        print("Roll:", self.roll)
        print("Sports:", self.sports)
        print("Marks:", self.marks)


obj = Result()
obj.get_name()
obj.get_roll()
obj.get_sports()
obj.get_marks()
obj.display()"""

# Hybrid Employee Example

"""class Person:
    def get_person(self):
        self.name = input("Enter name: ")

class Employee(Person):
    def get_employee(self):
        self.employee_id = int(input("Enter employee ID: "))

class Manager(Employee):
    def get_manager(self):
        self.department = input("Enter department: ")

class Skills:
    def get_skill(self):
        self.skill = input("Enter skill: ")

class SeniorManager(Manager, Skills):
    def display(self):
        print("Name:", self.name)
        print("Employee ID:", self.employee_id)
        print("Department:", self.department)
        print("Skill:", self.skill)


obj = SeniorManager()
obj.get_person()
obj.get_employee()
obj.get_manager()
obj.get_skill()
obj.display()"""

# Hybrid Result System

"""class Student:
    def get_student(self):
        self.name = input("Enter student name: ")

class Theory(Student):
    def get_theory(self):
        self.theory = float(input("Enter theory marks: "))

class Practical(Student):
    def get_practical(self):
        self.practical = float(input("Enter practical marks: "))

class Result(Theory, Practical):
    def calculate(self):
        self.total = self.theory + self.practical

    def display(self):
        print("Student:", self.name)
        print("Theory:", self.theory)
        print("Practical:", self.practical)
        print("Total:", self.total)


obj = Result()
obj.get_student()
obj.get_theory()
obj.get_practical()
obj.calculate()
obj.display()"""

# Hybrid Company Example

"""class Person:
    def get_person(self):
        self.name = input("Enter name: ")

class Employee(Person):
    def get_employee(self):
        self.salary = float(input("Enter salary: "))

class Developer(Employee):
    def get_developer(self):
        self.language = input("Enter programming language: ")

class Tester(Employee):
    def get_tester(self):
        self.tool = input("Enter testing tool: ")

class TeamLead(Developer, Tester):
    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Language:", self.language)
        print("Testing Tool:", self.tool)


obj = TeamLead()
obj.get_person()
obj.get_employee()
obj.get_developer()
obj.get_tester()
obj.display()"""