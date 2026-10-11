class Iot:
    total=0
    def __init__(self,name,room,type):
        self.name=name
        self.room=room
        self.type=type
        self.status="OFF"
        Iot.total+=1
    def on(self):
        if self.status=="ON":
            print(f" ⚠️ {self.name} is already ON")
        else:
            self.status="ON"
            print(f"🟢 {self.name} is turned ON Succesfully !!")
    def off(self):
        if self.status=="OFF":
            print(f" ⚠️ {self.name} is already OFF")
        else:
            self.status="OFF"
            print(f"🔴 {self.name} is turned OFF Succesfully !!")
    def show(self):
        print()
        print("="*50)
        print("   📡 DEVICE DETAILS ")  
        print("="*50)
        print("Device Name :", self.name)
        print("Device Type :", self.type)
        print("Room        :", self.room)

        if self.status=="ON":
            print("Status      : 🟢 ON")
        else:
            print("Status      : 🔴 OFF")
        print("========================================")               

class SmartLight(Iot):
    def __init__(self,name,room):
        super().__init__(name,room,"Smart Light")

        self.bright=80
        self.power="12W"
    def show(self):
        super().show()
        print("Brightness  :",self.bright,"%")
        print("Power       :",self.power)
        print()
        print("="*50)
class SmartFan(Iot):

    def __init__(self, name, room):
        super().__init__(name, room, "Smart Fan")

        self.speed = 3
        self.power = "75W"

    def show(self):
        super().show()

        print("Speed       :", self.speed)
        print("Power       :", self.power)

        print("========================================")

class SmartAc(Iot):

    def __init__(self, name, room):
        super().__init__(name, room, "Smart AC")

        self.temperature = 24
        self.mode = "Cooling"
        self.power = "1500W"

    def show(self):
        super().show()

        print("Temperature :", self.temperature, "°C")
        print("Mode        :", self.mode)
        print("Power       :", self.power)

        print("========================================")

class SmartSensor(Iot):

    def __init__(self, name, room):
        super().__init__(name, room, "Smart Sensor")

        self.sensor_type = "Temperature Sensor"
        self.reading = "28°C"

    def show(self):
        super().show()

        print("Sensor Type :", self.sensor_type)
        print("Reading     :", self.reading)

        print("========================================")
def find(devices,name):
    for device in devices:
        if device.name.lower()==name.lower():
            return device
    return None

devices=[]

while True:
    print("=" * 50)
    print("      📡 SMART IoT CONTROL SYSTEM    ")
    print("=" * 50)
    print("1. Add Device")
    print("2. View All Devices")
    print("3. Turn Device ON")
    print("4. Turn Device OFF")
    print("5. View Device Information")
    print("6. Exit")
    print()
    ch = int(input("Enter your choice: "))
    print()
    if ch == 1:
        print()
        print("1.Smart Light")
        print("2.Smart Fan")
        print("3.Smart AC")
        print("4.Smart Sensor")

        dch=int(input("\nEnter your choice:"))
        name=input("\nEnter device name:")
        room=input("\nEnter room name:")

        if dch==1:
            device=SmartLight(name,room)
        elif dch==2:
            device=SmartFan(name,room)
        elif dch==3:
            device=SmartAc(name,room)
        elif dch==4:
            device=SmartSensor(name,room)
        else:
            print("Invalid Choice !!")
            continue
        devices.append(device)

        print()
        print("="*50)
        print("   📡 DEVICE REGISTRATION")
        print("="*50)
        print()
        print("Device Type :",device.type)
        print("Device Name :",device.name)
        print("Room        :",device.room)
        print("Status      : 🔴 OFF")
        print()
        print(" ✅ Device added successfully!")
        print()
    elif ch == 2:

            print("\n========================================")
            print("             📊 ALL DEVICES")
            print("========================================")

            print("No.  Device              Room        Status")
            print("--------------------------------------------")


            for i, device in enumerate(devices, start=1):

                if device.status == "ON":
                    status = "🟢 ON"
                else:
                    status = "🔴 OFF"


                print(
                    f"{i:<4} "
                    f"{device.name:<20} "
                    f"{device.room:<10} "
                    f"{status}"
                )
            print()
            print("--------------------------------------------")
            print("Total Devices:", len(devices))
            print()
            print("========================================")        
    elif ch == 3:
        if len(devices)==0:
            print("\n⚠️  No Devices Available")
        else:
            name=input("\nEnter device Name:")
            device=find(devices,name)

            if device is None:
                print("\n❌ No Device Found")

            else:
                device.on()

    elif ch == 4:
        if len(devices)==0:
            print("\n⚠️  No Devices Available")
        else:
            name=input("\nEnter device Name:")
            device=find(devices,name)

            if device is None:
                print("\n❌ No Device Found")

            else:
                device.off()        

    elif ch == 5:
        if len(devices)==0:
            print("\n⚠️  No Devices Available")
        else:
            name=input("\nEnter device Name:")
            device=find(devices,name)
            if device is None:
                print("\n❌ No Device Found")

            else:
                device.show()            

    elif ch == 6:
        print("\n========================================")
        print("       📡 SMART IoT SYSTEM")
        print("========================================")

        print("\n Thank you for using Smart IoT System! 👋")
        print("\n System shutting down... \n")

        print("========================================")

        break

    else:
        print("\n❌ Invalid choice. Please select 1-6.")

