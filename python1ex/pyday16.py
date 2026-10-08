class book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def display(self):
        print("Title:",self.title)
        print("Author",self.author)
        print("Price",self.price)

book1=book("I1","Rishi","200")
book2=book("I2","Vannu","150")
book1.display()
book2.display()

class mobile():
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def display(self):
        print("Brand:",self.brand)
        print("Model:",self.model)
        print("Price:",self.price)
mobile1=mobile("Samsung","S24","120000")
mobile2=mobile("Iphone","14","100000")
mobile3=mobile("Nothing","1","50000")
mobile1.display()
mobile2.display()
mobile3.display()

class player():
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def display(self):
        print("Name:",self.name)
        print("Score:",self.score)
player1=player("Rishi",90)
player2=player("Vannu",95)
player1.display()
player2.display()


class account():
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def show_balance(self):
        print("Name:",self.name)
        print("Balance:",self.balance)
acc1=account("rishi",20000)
acc2=account("Vannu",30000)
acc1.show_balance()
acc2.show_balance()


class player():
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def display(self):
        print(self.name)
        print(self.score)
p1=player("rishi",90)
p2=player("vannu",95)
print("Before")
p1.display()
p2.display()
print("After")
p1.score=250
p2.score=300
p1.display()
p2.display()


class FitnessTracker:
    def __init__(self,name,steps,calories):
        self.name=name
        self.steps=steps
        self.calories=calories
    def show(self):
        print("Name:",self.name)
        print("Steps:",self.steps)
        print("Calories:",self.calories)
p1=FitnessTracker("Rishi",50,80)
p2=FitnessTracker("vannu",60,90)
p3=FitnessTracker("akki",70,100)
print("Before")
p1.show()
p2.show()
p3.show()
p1.name="ishi"
p1.steps=80
p1.calories=120
print("After")
p1.show()
p2.show()
p3.show()


class Rc():
    def __init__(self,d,c,s,f):
        self.d=d
        self.c=c
        self.s=s
        self.f=f
    def accelerate(self):
        self.s+=20
        self.f-=10
    def show(self):
        print("Name:",self.d)
        print("Car:",self.c)
        print("Speed:",self.s)
        print("fuel:",self.f)
        
rc1=Rc("rishi","Bmw",100,80)
rc2=Rc("Vannu","Bmw",120,70)
rc3=Rc("Akki","Bmw",130,60)
print("Before Race")
rc1.show()
rc2.show()
rc3.show()
rc1.accelerate()
rc2.accelerate()
rc1.accelerate()
print("after")
rc1.show()
rc2.show()
rc3.show()