"""
name=input("enter a name:")
for i in name:
    print(i)

a=input("enter name :")

n=input("enter name:")
print(f"First character :{n[0]}")
print(f"Second character :{n[-1]}")

name=input("enter name:")
print(name.upper())

name=input("enter name:")
print(name.lower())

name=input("enter name:")
v="a,e,i,o,u,A,E,I,O,U"
count=0
for i in name:
    if i in v:
        count+=1
print(count)

p=input("enter name:")
c=0
for i in p:
    if i == " ":
        c+=1
print(c)

name=input("enter string :")
print(name[::-1])

name="i love u java"
print(name.replace("rishi","python"))

name=input("enter string: ").lower()
print(name.count("a"))

user="python"
if user.startswith("py"):
    print("starts with py")

file=input("enter file name: ")
if file.endswith(".pdf"):
    print("Valid PDF File")
else:
    print("Invalid file")

name=input("enter name: ").replace(" ","").lower()
print(name)

user=input("enter name:")
count=0
for i in user:
    if i.isupper():
        count+=1
print(count)

user=input("enter a passowrd: ")
dig=0
upp=0
for i in user:
    if i.isupper():
        upp+=1
    if i.isdigit():
        dig+=1

if len(user)>=8 and upp>=1 and dig>=1 and "@" in user:
    print("strong password")
else:
    print("weak password")
"""