from collections import deque

my_list = deque()

print("stack ")

my_list.append("10")
my_list.append("30")
my_list.append("40")
print("Current List:", list(my_list))

print("Stack Pop (Last In):", my_list.pop())
print("List after Stack Pop:", list(my_list))
print("-" * 40)


print("queue")
my_list.append("80")
print("Current List:", list(my_list))
print("Queue Dequeue (First In):", my_list.popleft())
print("List after Queue Dequeue:", list(my_list))
