vehicle = input("Enter vehicle type (Bike/Car/Van/Bus): ")
entry_time = input("Enter entry time (HH:MM): ")
exit_time = input("Enter exit time (HH:MM): ")
if vehicle == "Bike":
    rate = 20
elif vehicle == "Car":
    rate = 40
elif vehicle == "Van":
    rate = 60
elif vehicle == "Bus":
    rate = 100
else:
    print("Invalid Vehicle Type")
    exit()


if hours == 0:
    hours = 1

if hours <= 5:
    charge = hours * rate
else:
    charge = (5 * rate) + ((hours - 5) * rate * 1.5)

print("\n----- PARKING RECEIPT -----")
print("Vehicle Type:", vehicle)
print("Entry Time:", entry_time)
print("Exit Time:", exit_time)
print("Parking Duration:", hours, "Hour(s)")
print("Parking Fee: ₹", charge)