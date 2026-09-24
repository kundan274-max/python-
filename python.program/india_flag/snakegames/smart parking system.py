slots = 5
parking = {}
TOTAL_SLOTS = 5
parking = {}
ticket_no = 1
rates = {"Bike": (10, 20), "Car": (20, 30), "Van": (40, 50), "Bus": (60, 80)}


def read_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


while True:
    available_slots = TOTAL_SLOTS - len(parking)
    print("\n----- SMART PARKING SYSTEM -----")
    print(f"Available slots: {available_slots}/{TOTAL_SLOTS}")
    print("1. Entry")
    print("2. Exit")
    print("3. Show parking")
    print("4. Stop")

    choice = read_integer("Enter your choice (1-4): ")

    if choice == 1:
        if available_slots == 0:
            print("No parking slots available.")
            continue

        vehicle_number = input("Enter vehicle number: ").strip().upper()
        vehicle_type = input("Enter vehicle type (Bike/Car/Van/Bus): ").strip().title()
        vip = input("Enter VIP status (Yes/No): ").strip().title()
        entry_time = read_integer("Enter entry time (hour, 0-23): ")

        if not vehicle_number or vehicle_type not in rates or vip not in ("Yes", "No") or not 0 <= entry_time <= 23:
            print("Invalid vehicle details. Entry cancelled.")
            continue

        parking[ticket_no] = {
            "vehicle_number": vehicle_number,
            "vehicle_type": vehicle_type,
            "vip": vip,
            "entry_time": entry_time,
        }
        print(f"Entry successful. Ticket number: {ticket_no}")
        ticket_no += 1

    elif choice == 2:
        ticket = read_integer("Enter ticket number: ")
        if ticket not in parking:
            print("Invalid ticket number.")
            continue

        record = parking[ticket]
        exit_time = read_integer("Enter exit time (hour, 0-23): ")
        if not 0 <= exit_time <= 23:
            print("Invalid exit time.")
            continue

        hours = (exit_time - record["entry_time"]) % 24
        hours = max(hours, 1)
        first_two_hours, later_hours = rates[record["vehicle_type"]]
        bill = min(hours, 2) * first_two_hours + max(hours - 2, 0) * later_hours
        if record["vip"] == "Yes":
            bill *= 0.8
        if hours > 24:
            bill += 1000

        print(f"\nVehicle: {record['vehicle_number']}")
        print(f"Vehicle type: {record['vehicle_type']}")
        print(f"Hours parked: {hours}")
        print(f"VIP status: {record['vip']}")
        print(f"Parking bill: Rs. {bill:.2f}")
        del parking[ticket]

    elif choice == 3:
        if not parking:
            print("Parking is empty.")
        else:
            print("\nCurrent parking:")
            for ticket, record in parking.items():
                print(f"Ticket {ticket}: {record['vehicle_number']} ({record['vehicle_type']})")

    elif choice == 4:
        print("Exiting the system.")
        break

    else:
        print("Invalid choice. Please try again.")
