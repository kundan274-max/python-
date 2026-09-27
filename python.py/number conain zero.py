n=int(input("enter a number:"))
find=False
while n!=0:
    r=n%10
    if r==0:
        find=True
        break
if find:
    print("the number contains zero")
else:
    print("the number does not contain zero")