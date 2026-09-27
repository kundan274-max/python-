# 46. Custom Descriptor — Only Positive Integers

# Descriptor ka kaam hota hai kisi attribute ke get/set behavior ko control karna.

"""class PositiveInteger:

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, owner):
        if obj is None:
            return self

        return obj.__dict__.get(self.name)

    def __set__(self, obj, value):
        if not isinstance(value, int):
            raise TypeError("Value must be an integer.")

        if value <= 0:
            raise ValueError("Value must be positive.")

        obj.__dict__[self.name] = value


class Student:

    age = PositiveInteger()

    def __init__(self, age):
        self.age = age


age = int(input("Enter student age: "))

student = Student(age)

print("Age:", student.age)

new_age = int(input("Enter new age: "))

student.age = new_age

print("Updated age:", student.age)"""


# 47. Singleton Design Pattern

# Singleton ka matlab:

# Puri program me class ka sirf ek object exist kare.

"""class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance


obj1 = Singleton()
obj2 = Singleton()

print("Object 1:", id(obj1))
print("Object 2:", id(obj2))

if obj1 is obj2:
    print("Both objects are the same.")
else:
    print("Both objects are different.")"""

# 48. Metaclass — Automatically Inspect Methods

# Metaclass ko simple language me class banane wali class samajh sakte ho.

"""class MethodInspector(type):

    def __new__(cls, name, bases, namespace):

        print("\nCreating class:", name)

        for item in namespace:
            if callable(namespace[item]) and not item.startswith("__"):
                print("Method found:", item)

        return super().__new__(cls, name, bases, namespace)


class Student(metaclass=MethodInspector):

    def show(self):
        print("Showing student.")

    def study(self):
        print("Student is studying.")


student = Student()

student.show()"""

# 49. Plugin Architecture

# Isme plugins automatically register honge aur common interface ke through execute honge.

"""from abc import ABC, abstractmethod
class Plugin(ABC):
    registry = {}
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        Plugin.registry[cls.__name__] = cls
    @abstractmethod
    def run(self):
        pass
class CalculatorPlugin(Plugin):
    def run(self):
        print("Calculator plugin executed.")
class GreetingPlugin(Plugin):
    def run(self):
        print("Greeting plugin executed.")
class TimePlugin(Plugin):
    def run(self):
        print("Time plugin executed.")
print("Available plugins:")
for name in Plugin.registry:
    print("-", name)
choice = input("\nEnter plugin name: ")
if choice in Plugin.registry:
    plugin = Plugin.registry[choice]()
    plugin.run()
else:
    print("Plugin not found.")"""
