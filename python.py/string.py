"""
name="kundan"
friend="saurabh"
another_friend="prashant"
apple='''he said,
hi kundan
hey i am good
"i want to eat an apple'''
print("hello, " + name)
#print(apple)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
#print(name[6])#throws an error
print("lets use a for loop\n")
for character in apple:
    print(character)"""

# names = "kundan"
# kumar = len(names)
# print(kumar)
# # print(names[0:4])#including 0th index and excluding 4th index
# # print(names[1:5])
# # print(names[:5])
# # print(names[0:-3])
# # print(names[:len(names)-3])
# print(names[-1:len(names)-3])
# print(names[-3:-1])
# Quik  Quize
# String are mutable
a = "kundan!!!!!!!!kundan"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("kundan", "harry"))
print(a.split(" "))
print(a.capitalize())
str1 = "welcome to the console!!!"
print(len(str1))
print(len(str1.center(50)))
print(a.count("kundan"))
