n=int(input("enter a number:"))
even=0
odd=0
while n!=0:
    r=n%10
    if r%2==0:
        even+=1
    else:
        odd+=1
print("even digits:", even)
print("odd digits:", odd)