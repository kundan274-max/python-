units=int(input("enter the number of units consumed:"))
if units<=200:
    bill=0
elif units<=500:
    bill=(units-200)*10
elif units<=1000:
    bill=(300*10)+(units-500)*15
else:
    bill=(300*10)+(500*15)+(units-1000)*20
print("electricity bill:", bill)
