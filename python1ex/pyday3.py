"""n=int(input("enter the number :"))
if n>0:
    print("Positive number")

age=int(input("enter your age:"))
if age>=18:
    print("Eligible to Vote")

marks=int(input("enter marks:"))
if marks>=35:
    print("Pass")

num=int(input("enter num :"))
if num%2==0:
    print("Even")

a=int(input("enter your age:"))
if a>=18:
    print("Adult")
"""
'''
m=int(input("enter marks:"))
if m>=35:
    print("Pass")
else:
    print("Fail")

n1=int(input("enter num :"))
if n1%2==0:
    print("Even")
else:
    print("Odd")

x=int(input("enter 1 number: "))
y=int(input("enter 2 number: "))

if x>y:
    print(x)
else:
    print(y)

d=int(input("enter your age:"))
if d>=18:
    print("Eligible for driving license")
else:
    print("Not Eligible")


p1="Rishi3"
pass1=input("enter password: ")
if pass1 == p1:
    print("login succesful")
else:
    print("wrong password")
'''
'''
m = int(input("enter marks: "))
if m>=90:
    print("A")
elif m>=80:
    print("B")
elif m>=70:
    print("C")
elif m>=60:
    print("D")
else:
    print("Fail")


signal=input("enter signal color:").upper()
if signal == 'RED':
    print("Stop")
elif signal == 'GREEN':
    print("GO")
elif signal=='YELLOW':
    print("Get Ready")
else:
    print("Invalid Signal Color")


bill=int(input("enter units:"))
if bill>500:
    print(" Commercial")
elif bill>300:
    print("High Usage")
elif bill>101:
    print("Normal Usage")
else:
    print("Low Usage")



t=int(input("enter temperature:"))
if t>40:
    print("Very Hot")
elif t>30:
    print("Hot")
elif t>20:
    print("pleasent")
else:
    print("cold")

m=int(input("enter month number : "))
if m==1:
    print("January")
elif m==2:
    print("Feburary")
elif m==3:
    print("March")
elif m==4:
    print("April")
elif m==5:
    print("May")
elif m==6:
    print("june")
elif m==7:
    print("July")
elif m==8:
    print("August")
elif m==9:
    print("september")
elif m==10:
    print("october")
elif m==11:
    print("november")
elif m==12:
    print("december")
else:
    print("Invalid month")


stu=input("Are you student?(yes/no):").lower()
id=input("do you have id card?(yes/no):").lower()

if stu=="yes":
    if id=="yes":
        print("Entry allowed")
    else:
        print("Bring id card")
else:
    print("NOT student")

card=input("card is inserted?(yes/no):").lower()
p1=1234
if card=="yes":
    pin=int(input("enter pin :"))
    if p1==pin:
        print("Transaction Allowed")
    else:
        print("Invalid Pin")
else:
    print("Insert card")


marks=int(input("enter marks: "))
att=int(input("enter attendence:"))

if marks>=90 and att>=75:
    print("Scholarship Approved")
else:
    print("Not Eligible")


email=input("is email available ?(yes/no):").lower()
phn=input("is phn num is avaialble?(yes/no):").lower()

if email=="yes" or phn=="yes":
    print("Login Available")
else:
    print("Login Failed")


age=int(input("enter age:"))
id=input("is id avaialble?(yes/no):").lower()

if age>=18 and id=="yes":
    print("Ticket Booked")
else:
    print("cannot book ticket")
'''