class GymMember:
    gym_name="powerfit"

    def __init__(self,name,type):
        self.name=name
        self.type=type
    def show(self):
        print("Name:",self.name)
        print("Type:",self.type)
        print("Gym name:",self.gym_name)

m1= GymMember("Rishi","premium")
m2= GymMember("Vannu","basic")
m3= GymMember("akki","medium")
m1.show()
m2.show()
m3.show()
print()
GymMember.gym_name="Fitzone"
m1.show()
m2.show()
m3.show()

class Electricity:
    @staticmethod
    def calculate_bill(units, price_per_unit):
        return units*(price_per_unit)

total=Electricity.calculate_bill(10,20)
print(total)


class employee:
    company="Ria"
    def __init__(self,name):
        self.name=name
    def show(self):
        print("Name:",self.name)
        print("Company:",self.company)
    @staticmethod
    def salary(m_salary):
        return m_salary*12
emp1=employee("Rishi")
total=employee.salary(30000)
print("Employee Details")
emp1.show()
print("Salary:",total)
print()
employee.company="RIA"
print("Employee Details")
emp1.show()
print("salary:",total)


class wallet:
    def __init__(self,balance):
        self.__balance=balance
    def get_balance(self):
        print("Balance:",self.__balance)
    def deposit(self,amount):
        if amount>=0:
            self.__balance+=amount
            print("depoist amount :",amount)
        else:
            print("Invalid amount")
    def withdraw(self,amount):
        if amount<=0:
            print("Invalid withdraw")
        elif amount>self.__balance:
            print("Insufficient balance")            
        else:
            self.__balance-=amount
            print("amount withdraw :",amount)
w1=wallet(1500)
w1.get_balance()
w1.deposit(500)
w1.get_balance()
w1.withdraw(1000)
w1.get_balance()
w1.withdraw(5000)
w1.get_balance()
w1.deposit(-500)

class GameCharacter:
    def __init__(self,name,health):
        self.name=name
        self._health=health
    def show(self):
        print(self.name)
        print(self._health)
    def take(self,damage):
        if damage<0:
            print("NO health")
        else:
            self._health-=damage
            print("damage:",damage)
g1=GameCharacter("rishi",100)
g1.show()
g1.take(30)
g1.show()            


class product:
    def __init__(self,price):
        self.__price=price
    def get_price(self):
        print("price:",self.__price)
    def set_price(self,amu):
        if amu>=0:
            self.__price+=amu
            print("Amount added:",amu)
        else:
            print("invalid choice")
p1=product(500)
p1.get_price()
p1.set_price(300)
p1.get_price()


class Vehicle:
    def start(self):
        print("Vehicle Started")
    def stop(self):
        print("Vehicle stopped")
class ambulance(Vehicle):
    def siren(self):
        print("siren on")
a1=ambulance()
a1.start()
a1.stop()
a1.siren()

class employee:
    def work(self):
        print("Working")
class manager(employee):
    def work1(self):
        super().work()
        print("I am a manager")
e1=manager()
e1.work1()


    