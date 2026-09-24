n=int(input("enter a number:"))
c=0
while n!=0:
    r=n%10
    c+=1
    n//=10
print("count of digits:", c)