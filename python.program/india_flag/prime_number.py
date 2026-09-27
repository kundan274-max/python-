# prime number less then 20
for num in range(2,20):
  c=0
  for i in range(1,num+1):
    if num%i==0:
      c=c+1
    if c==2:
      print(num)

'''n = int(input("Enter number of terms: "))
a = 0
b = 1
i = 1
print("Fibonacci Sequence:")
while i <= n:
    print(a)
    c = a + b
    a = b
    b = c
    i=i+1'''