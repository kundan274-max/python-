n=int(input("enter a number:"))
c=0
for i in range(1,n+1):
    if i%2==0:
        c+=1
print("count of even numbers:", c)