# # s=set()
# # for i in range (5):
# #     n= int (input("enter any number"))
# #     s.add(n)
# #     print("element of set= " , s)
   

# # s1=set()
# # s2=set()
# # for i in range (5):
# #     n= int(input("enter any number "))
# #     s1.add(n)
# #     for i in range (5):
# #         n= int(input("enter any number "))
# #         s2.add(n)
# #         print("union=" ,s1.union(s2))
# #         print("intersection=" ,s1.intersection(s2))
# #         print("difference=" ,s1.difference(s2))
        
# s1=set()
# s2=set()
# for i in range (5):
#     n= int(input("enter any number "))
#     s1.add(n)
#     for i in range (5):
#         n= int(input("enter any number "))
#         s2.add(n)
#         print("union=" ,s1.union(s2))
#         print("intersection=" ,s1.intersection(s2))
#         print("difference=" ,s1.difference(s2))


# s = {10, 20, 30, 40, 50}

# print("Set:", s)
# s = {10, 20, 30}

# s.add(40)
# print("After adding:", s)

# s.remove(20)
# print("After removing:", s)

# union

# numbers = [10, 20, 10, 30, 20, 40, 30]

# s = set(numbers)

# print("Original List:", numbers)
# print("After removing duplicates:", s)

# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}

# print("Union:", a | b)

# remove element from set

# n = int(input("Enter number of elements: "))

# s = set()

# for i in range(n):
#     x = int(input("Enter element: "))
#     s.add(x)

# x = int(input("Enter element to remove: "))

# if x in s:
#     s.remove(x)
#     print("Updated Set:", s)
# else:
#     print("Element not found")

# Duplicate data

# n = int(input("Enter number of elements: "))

# numbers = []

# for i in range(n):
#     x = int(input("Enter element: "))
#     numbers.append(x)

# s = set(numbers)

# print("Original List:", numbers)
# print("Set without duplicates:", s)

# Intersection of Two Sets

# n = int(input("Enter number of elements in Set A: "))

# a = set()

# for i in range(n):
#     x = int(input("Enter element: "))
#     a.add(x)

# n = int(input("Enter number of elements in Set B: "))

# b = set()

# for i in range(n):
#     x = int(input("Enter element: "))
#     b.add(x)

# print("Intersection:", a & b)

# Difference of Two Sets

# n = int(input("Enter number of elements in Set A: "))

# a = set()

# for i in range(n):
#     x = int(input("Enter element: "))
#     a.add(x)

# n = int(input("Enter number of elements in Set B: "))

# b = set()

# for i in range(n):
#     x = int(input("Enter element: "))
#     b.add(x)

# print("A - B:", a - b)
# print("B - A:", b - a)

# Check Element Present or Not

# n = int(input("Enter number of elements: "))

# s = set()

# for i in range(n):
#     x = int(input("Enter element: "))
#     s.add(x)

# x = int(input("Enter element to search: "))

# if x in s:
#     print("Element is present")
# else:
#     print("Element is not present")

# Check Set is Subset or Not

# n = int(input("Enter number of elements in Set A: "))

# a = set()

# for i in range(n):
#     x = int(input("Enter element: "))
#     a.add(x)

# n = int(input("Enter number of elements in Set B: "))

# b = set()

# for i in range(n):
#     x = int(input("Enter element: "))
#     b.add(x)

# if a.issubset(b):
#     print("A is a subset of B")
# else:
#     print("A is not a subset of B")

## write a program  to create append and remove in python

# n = int(input("enter number of list: "))
# my_list=[]
# for i in range (n):
#     n1=input("enter element:")
#     my_list.append(n1)

#     #append
#     n1=input("enter element to append:")
#     my_list.append(n1)
#     print("after append:",my_list)

#     #remove
#     n1=input("enter element to remove:")
#     if n1 in my_list:
#         my_list.remove(n1)
#         print("after remove:",my_list)
#     else:
#         print("element not found in list:",my_list)
         

# Write a program to demonstrate working with tuples in python

n= int(input("enter number of element: "))
element =[]
for i in range (n):
    num= input("enter element: ")
    element.append(num)
    my_tuple=tuple(element)

    print("tuple:", my_tuple)

    #access element

    index= int(input("enter index to access: " ))
    if index < len(my_tuple):
        print("element:",my_tuple[index])
    else:
        print("length of tuple:", len(my_tuple))

