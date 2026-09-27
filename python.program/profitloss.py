cp = float(input("Enter Cost Price: "))
sp = float(input("Enter Selling Price: "))

if sp > cp:
    print("Profit =", sp - cp)
elif cp > sp:
    print("Loss =", cp - sp)
else:
    print("No Profit No Loss")