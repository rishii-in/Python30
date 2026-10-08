"""
x=1
while x<=10:
    print(x)
    x+=1

x=10
while x>=1:
    print(x)
    x-=1


for i in range(2,21,2):
    print(i)


for i in range(1,21,2):
    print(i)



x=int(input("enter number for multiplication table :"))
for i in range(1,11):
    print(x,"x",i,"=",x*i)

N=int(input("enter number for sum:"))
s=0
for i in range(1,N+1):
    s+=i
print(s)

N=int(input("enter number for factorial:"))
s=1
for i in range(1,N+1):
    s*=i
print(s)


n=input("enter digits:")
dig=0
for i in n:
    dig+=1
print(dig)

n=input("enter digits:")
dig=0
for i in n:
    dig+=int(i)
print(dig)


n=input("enter a number:")
d=""
for i in n:
    d=i+d
print(d)

for i in range(1,11):
    if i==5:
        continue
    print(i)

for i in range(1,11):
    if i==7:
        break
    print(i)


pas="Rishi352007"
while True:
    p=input("Enter password:")
    if p==pas:
        print("LOGIN Succesfull")
        print("WELCOME USER")
        break
    else:
        print("Incorrect Password..Try Again !")



p='rishi'
count=0
while count!=3:
    pas=input('enter password:')
    if pas==p:
        print("login succesfull")
        break
    else:
        print("incorrect password")
        count+=1
if count==3:
    print("Account Locked")



while True:
    i=int(input("enter positive number :"))
    if i>0:
        print("Valid Number")
        break
    else:
        print("Invalid number!Try again.")

"""

while True:
    print()
    print("1.Say Hello!")
    print("2.Print College Name")
    print("3.Exit")
    print()
    ch=int(input("Enter choice(1-3):"))
    print()
    if ch==1:
        print("Hello!")
        print()
    elif ch==2:
        print("Laki Reddy Bali Reddy College Of Engineering")
        print()
    else:
        print("Thank You")
        print()
        break