n=int(input("enter a number:"))
temp=n
rev=0
while n!=0:
    r=n%10
    rev=rev*10+r
    n//=10
if temp==rev:
    print("palindrome")
else:
    print("not palindrome")