vehicle = input("Enter vehicle type (bike/car/van/bus): ")
time = float(input("Enter parking hours: "))

if vehicle == "bike":
    rate = 20
elif vehicle == "car":
    rate = 40
elif vehicle == "van":
    rate = 60
elif vehicle == "bus":
    rate = 100
else:
    print("Invalid vehicle type")
    exit()

if time <=2:
    charge = rate
elif time <= 5:
    charge = rate + (time - 2) * rate
else:
    charge = rate + 3 * rate + (time - 5) * rate * 1.5

print("Vehicle Type:", vehicle)
print("Parking Time:", time, "hours")
print("Total Parking Charge:", charge)