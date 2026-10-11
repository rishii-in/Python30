class Cab:
    def __init__(self, driver, cab_no, cab_type, location, price):
        self.driver = driver
        self.cab_no = cab_no
        self.cab_type = cab_type
        self.location = location
        self.price = price
        self.available = True
    def show_info(self):
        print("Driver:", self.driver)
        print("Cab No:", self.cab_no)
        print("Type:", self.cab_type)
        print("Location:", self.location)
        print("Price/km: ₹", self.price)
        print("Status:", "Available" if self.available else "Booked")
        print()
class Passenger:
    def __init__(self, user, pickup, destination, km, cab):
        self.user = user
        self.pickup = pickup
        self.destination = destination
        self.km = km
        self.cab = cab
        self.status = "Confirmed"
    def view(self):
        print("Passenger:", self.user)
        print("Pickup:", self.pickup)
        print("Destination:", self.destination)
        print("Driver:", self.cab.driver)
        print("Cab No:", self.cab.cab_no)
        print("Cab Type:", self.cab.cab_type)
        print("Fare: ₹", self.cab.price * self.km)
        print("Status:", self.status)

cab1 = Cab("Rishi", 1, "Sedan", "Vijayawada", 7)
cab2 = Cab("Vannu", 2, "SUV", "Nandigama", 8)
cab3 = Cab("Akki", 3, "SUV", "Nandigama", 6)

cab = [cab1, cab2, cab3]

booking = None

while True:

    print("=" * 50)
    print("          🚕 CAB BOOKING APP")
    print("=" * 50)
    print("1. View Available Cabs")
    print("2. Book a Cab")
    print("3. View Booking")
    print("4. Complete Ride")
    print("5. Cancel Booking")
    print("6. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        print("\n------- Available Cabs ----------")
        for i in cab:
            if i.available:
                i.show_info()
    elif ch == 2:
        if booking is not None and booking.status == "Confirmed":
            print("\nYou already have an active booking!")
            continue
        print("\n------- Book a Cab ----------")
        user = input("Enter passenger name: ")
        loc = input("Enter pickup location: ")
        dest = input("Enter destination: ")
        km = int(input("Enter distance in km: "))
        print("\nChoose Cab:")
        for i in cab:
            if i.available:
                print(
                    i.cab_no,
                    "-",
                    i.driver,
                    "-",
                    i.cab_type,
                    "- ₹",
                    i.price,
                    "/km"
                )
        c = int(input("Enter cab number: "))
        if c < 1 or c > len(cab):
            print("Invalid cab number!")
            continue
        selected_cab = cab[c - 1]
        if not selected_cab.available:
            print("Sorry! This cab is already booked.")
            continue
        selected_cab.available = False
        booking = Passenger(
            user,
            loc,
            dest,
            km,
            selected_cab
        )
        print("\n" + "=" * 50)
        print("          🚕 BOOKING CONFIRMED")
        print("=" * 50)
        booking.view()
    elif ch == 3:
        if booking is None:
            print("\nNo booking found!")
        else:
            print("\n------ YOUR BOOKING -----------")
            booking.view()
    elif ch == 4:
        if booking is None:
            print("\nNo booking found!")
        elif booking.status != "Confirmed":
            print("\nThis booking is already", booking.status)
        else:
            booking.status = "Completed"
            booking.cab.available = True
            print("\n✅ Ride completed successfully!")
            booking.view()
    elif ch == 5:
        if booking is None:
            print("\nNo booking found!")
        elif booking.status != "Confirmed":
            print("\nThis booking is already", booking.status)
        else:
            booking.status = "Cancelled"
            booking.cab.available = True
            print("\n❌ Booking cancelled!")
            booking.view()
    elif ch == 6:
        print("\nThanks for using Cab Booking App 🚕")
        print("See you again!")
        break
    else:
        print("\nInvalid choice!")




