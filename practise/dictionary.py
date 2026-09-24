# Create a Dictionary 
# student = {}

# name = input("Enter name: ")
# age = int(input("Enter age: "))
# marks = float(input("Enter marks: "))

# student["name"] = name
# student["age"] = age
# student["marks"] = marks

# print(student)

# display all key
# student = {}

# for i in range(3):
#     key = input("Enter key: ")
#     value = input("Enter value: ")
#     student[key] = value

# print("Keys:", student.keys())
# dispaly all value
# student = {}

# for i in range(3):
#     key = input("Enter key: ")
#     value = input("Enter value: ")
#     student[key] = value

# print("Values:", student.values())

#Display Keys and Values Using Loop
# student = {}

# for i in range(3):
#     key = input("Enter key: ")
#     value = input("Enter value: ")
#     student[key] = value

# for key, value in student.items():
#     print(key, ":", value)
# Search a Key in Dictionary

# student = {}

# for i in range(3):
#     key = input("Enter key: ")
#     value = input("Enter value: ")
#     student[key] = value

# search = input("Enter key to search: ")

# if search in student:
#     print("Key found")
#  else:
#   print("Key not found")
# search and display value of KeyboardInterruptstudent = {}

# for i in range(3):
#     key = input("Enter key: ")
#     value = input("Enter value: ")
#     student[key] = value

# search = input("Enter key: ")

# if search in student:
#     print("Value =", student[search])
# else:
#     print("Key not found")

#add new item
# student = {}

# for i in range(3):
#     key = input("Enter key: ")
#     value = input("Enter value: ")
#     student[key] = value

# key = input("Enter new key: ")
# value = input("Enter new value: ")

# student[key] = value

# print("Updated dictionary:", student)
# Student Result Using Dictionary
# student = {}

# name = input("Enter student name: ")
# marks = int(input("Enter marks: "))

# student["name"] = name
# student["marks"] = marks

# if marks >= 40:
#     student["result"] = "Pass"
# else:
#     student["result"] = "Fail"

# print(student)
#remove all item
# student = {}

# n = int(input("Enter number of items: "))

# for i in range(n):
#     key = input("Enter key: ")
#     value = input("Enter value: ")
#     student[key] = value

# print("Before:", student)

# student.clear()

# print("After:", student)


#Dictionary of Student Marks
# marks = {}

# n = int(input("Enter number of students: "))

# for i in range(n):
#     name = input("Enter student name: ")
#     mark = int(input("Enter marks: "))
#     marks[name] = mark

# print("Student Marks:")

# for name, mark in marks.items():
#     print(name, ":", mark)

# # Find Student with Highest Marks 
    
# marks = {}

# n = int(input("Enter number of students: "))

# for i in range(n):
#     name = input("Enter student name: ")
#     mark = int(input("Enter marks: "))
#     marks[name] = mark

# highest = max(marks.values())

# for name, mark in marks.items():
#     if mark == highest:
#         print("Highest marks:", name, mark)

# # Find Sum of Dictionary Values

# marks = {}

# n = int(input("Enter number of students: "))

# for i in range(n):
#     name = input("Enter name: ")
#     mark = int(input("Enter marks: "))
#     marks[name] = mark

# total = sum(marks.values())

# print("Total marks =", total)

# # Find Average of Dictionary Values

# marks = {}

# n = int(input("Enter number of students: "))

# for i in range(n):
#     name = input("Enter name: ")
#     mark = int(input("Enter marks: "))
#     marks[name] = mark

# average = sum(marks.values()) / len(marks)

# print("Average =", average)

# # Count Even and Odd Values

# numbers = {}

# n = int(input("Enter number of items: "))

# for i in range(n):
#     key = input("Enter key: ")
#     value = int(input("Enter number: "))
#     numbers[key] = value

# even = 0
# odd = 0

# for value in numbers.values():
#     if value % 2 == 0:
#         even += 1
#     else:
#         odd += 1

# print("Even =", even)
# print("Odd =", odd)

# # Find Largest Value in Dictionary

# numbers = {}

# n = int(input("Enter number of items: "))

# for i in range(n):
#     key = input("Enter key: ")
#     value = int(input("Enter value: "))
#     numbers[key] = value

# print("Largest value =", max(numbers.values()))

#  #Find Smallest Value

# numbers = {}

# n = int(input("Enter number of items: "))

# for i in range(n):
#     key = input("Enter key: ")
#     value = int(input("Enter value: "))
#     numbers[key] = value

# print("Smallest value =", min(numbers.values()))

#  #Check Empty Dictionary

# data = {}

# key = input("Enter key: ")
# value = input("Enter value: ")

# data[key] = value

# if len(data) == 0:
#     print("Dictionary is empty")
# else:
#     print("Dictionary is not empty")