import calculator
a=int(input("enter a value:"))
b=int(input("enter b value:"))
print("Addition:",calculator.add(a,b))
print("subtraction:",calculator.sub(a,b))
print("Multiplication:",calculator.mul(a,b))
print("Divison:",calculator.div(a,b))

from operations import square,cube

a=int(input("enter value for square and cube:"))
print("Square:",square(a))
print("cube:",cube(a))


import temperature as temp

c=int(input("enter value of celsius:"))
f=int(input("enter value of fahrenheit:"))
print("Celsius to Fahrenheit:",temp.celsius_to_fahrenheit(c))
print("Fahrenheit to celsius:",temp.fahrenheit_to_celsius(f))


import math
n=int(input("enter a number:"))

print("Square root :",math.sqrt(n))
print("Ceiling:",math.ceil(n))
print("Floor:",math.floor(n))
print("Factorial:",math.factorial(n))

import random 
l1=["Python", "Java", "C", "C++"]
print("Random number between 1 and 100:",random.randint(1,100))
print("Random number between 50 and 100:",random.randint(50,100))
print("Random choice :",random.choice(l1))
print("Random decimal:",random.random())

import datetime

print("Current Date and time:",datetime.datetime.now())
print("Current Time:",datetime.datetime.now().time())
print("Current Date:",datetime.date.today())


import student as s

a=int(input("enter marks m1:"))
b=int(input("enter marks m2:"))
c=int(input("enter marks m3:"))
print("Total:",s.calculate_total(a,b,c))
print("Average:",s.calculate_average(a,b,c))


import number_tools
from number_tools import cube
import number_tools as nt
a=int(input("enter number:"))
print(nt.square(a))
print(cube(a))
print(nt.double(a))

import random
from password_tools import l1
p1=""
p=int(input("enter length of password:"))
while len(p1)<p:
    p1=p1+random.choice(l1)
    if len(p1)<p:
        p1=p1+str(random.randint(0,9))
print("Generated Password:",p1)

from dice import roll_dice as rd
n=int(input("enter how many times do you want to roll?:"))

for i in range(1,n+1):
    print(f"Roll {i} : {rd()}")



import date_tools as dt
print("1.Date")
print("2.Time")
print("3.Exit")
ch=int(input("enter your choice:"))
if ch==1:
    print("Today's Date:",dt.show_today())
if ch==2:
    print("Today's Time :",dt.show_current_time())
if ch==3:
    print("Exit")


from calculator1 import basic
from calculator1 import advanced

a=int(input("enter a value:"))
b=int(input("enter b value:"))

print("Addition :",basic.add(a,b))
print("Subtraction:",basic.sub(a,b))
print("Multiplication: ",basic.mul(a,b))
print("Division:",basic.div(a,b))
print("Square:",advanced.square(a))
print("Cube:",advanced.cube(a))


from utilities import date_tool,math_tools,random_tools

a=int(input("enter a:"))
print("\nSquare:",math_tools.square(a))
print("Cube:",math_tools.cube(a))
print("Factorial:",math_tools.fact(a))
print("\nRandom Number:",random_tools.random_number())
print("Random Item:",random_tools.random_choice())
print("\nToday's Date:",date_tool.show_today())
print("Current Time:",date_tool.show_current_time())


import employee
import datetime
user=input("enter employee name:")
salary=int(input("enter monthly salary:"))
print("Employee name:",user)
print("Annual Salary:",employee.annual_salary(salary))
print("Bonus:",employee.emp_bonus(salary))
print("Today's Date:",datetime.date.today())


from shopping import price,discount,random_item
p=int(input("enter Product price:"))
q=int(input("enter quantity:"))
d=int(input("enter discount percentage:"))
print()
print("Total Price:",price.total_price(p,q))
print("Discount Amount:",discount.disc(p,q,d))
print("Final Price",discount.final_price(p,q,d))
print("\nRandom Item:",random_item.random_choice())


from tools import date,rand,calci
print("========== Utility Center =============")
while True:
    print("\n1.Calculator")
    print("2.Random Number")
    print("3.Random Item")
    print("4.Today's Date")
    print("5.Current Time")
    print("6.Exit")
    print()
    ch=int(input("enter choice:"))

    if ch==1:
        calci.calci1()
    elif ch==2:
        rand.random_number()
    elif ch==3:
        rand.random_choice()
    elif ch==4:
        date.show_today()
    elif ch==5:
        date.show_current_time()
    elif ch==6:
        print("\nThank you for using Utility Center!")
        print()
        break
    else:
        print("\nInvalid choice")