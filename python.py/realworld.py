amt=int(input("enter amount:"))
if amt>=10000:
    dis=amt*0.25
elif amt>=5000:    
    dis=amt*0.15
else:    
    dis=amt*0.05
fin_amt=amt-dis
print("final amount:", fin_amt)
