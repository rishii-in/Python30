class EV:
    company = "GreenCharge"

    def __init__(self, owner, ev_number, battery):
        self.owner = owner
        self.ev_number = ev_number
        self.battery = battery
        self.__charging = False

    @classmethod
    def change_company(cls, name):
        cls.company = name

    @staticmethod
    def check_battery(battery):
        return battery > 0

    def get_status(self):
        return self.__charging

    def set_status(self, status):
        self.__charging = status

    def start_charging(self):
        self.set_status(True)
        print("EV charging started!")

    def stop_charging(self):
        self.set_status(False)
        print("EV charging stopped!")


class FastEV(EV):

    def __init__(self, owner, ev_number, battery):
        super().__init__(owner, ev_number, battery)

    def start_charging(self):
        print("Fast charging started!")
        self.set_status(True)


ev = None

while True:

    print("\n====== SMART EV CHARGING ======")
    print("1. Register EV")
    print("2. View EV")
    print("3. Start Charging")
    print("4. Stop Charging")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        owner = input("Enter owner name: ")
        ev_number = input("Enter EV number: ")
        battery = float(input("Enter battery capacity: "))

        if EV.check_battery(battery):
            ev = FastEV(owner, ev_number, battery)
            print("EV registered successfully!")
        else:
            print("Invalid battery!")

    elif choice == "2":

        if ev is None:
            print("Please register an EV first.")

        else:
            print("\n--- EV DETAILS ---")
            print("Company:", EV.company)
            print("Owner:", ev.owner)
            print("EV Number:", ev.ev_number)
            print("Battery:", ev.battery, "kWh")

            if ev.get_status():
                print("Status: Charging")
            else:
                print("Status: Not Charging")

    elif choice == "3":

        if ev is None:
            print("Please register an EV first.")

        elif ev.get_status():
            print("EV is already charging!")

        else:
            ev.start_charging()

    elif choice == "4":

        if ev is None:
            print("Please register an EV first.")

        elif not ev.get_status():
            print("EV is not charging!")

        else:
            ev.stop_charging()

    elif choice == "5":

        print("\nThank you for using Smart EV Charging!\n")
        break

    else:
        print("\nInvalid choice!\n")