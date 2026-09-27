class Student:

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

# class Kundan:
#     name = "kundan kumar"
# s1 = Kundan()
# print(s1.name)



# class Car:
#     color = "blue"
#     brand = "mercidies"
# car1 = Car()
# print(car1.color)
# print(car1.brand)