import math

radius = float(input("Enter radius (cm): "))
height = float(input("Enter height (cm): "))

volume = math.pi * radius * radius * height

print("Volume =", volume, "cubic cm")

litres = volume / 1000

cost = litres * 40

print("Milk =", litres, "litres")
print("Cost = Rs.", cost)