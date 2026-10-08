'''
n={10,20,30,40,50}
print(n)
print(type(n))

n={10,20,10,30,20,40,30}
print(n)

n={10,20,30,10,20,40}
print(len(n))

c={"red","blue"}
c.add("green")
print(c)
c.update({"yellow","black","white"})
print(c)

n={10,20,30,40,50}
n.remove(30)
print(n)
n.discard(40)
print(n)
n.pop()
print(n)
n.clear()
print(n)

lang={"python","java","c","sql"}
user=input("enter a lang :")
if user in lang:
    print("lang is found")
if user not in lang:
    print("lang is not found")

a={1,2,3,4}
b={4,5,6,7}
print(a|b)
print(a&b)
print(a-b)
print(b-a)
print(a^b)

python = {"Rishi", "Rahul", "Priya", "Akhil"}
ml = {"Rishi", "Priya", "Kiran", "Anu"}

print(python|ml)
print(python&ml)
print(python^ml)
print(ml-python)

n=input("enter a sentence:").split()
print(set(n))

n=set()
for i in range(10):
     n.add(input("enter a num:"))
print(n)
'''

emails = [
    "rishi@gmail.com",
    "rahul@gmail.com",
    "rishi@gmail.com",
    "priya@gmail.com",
    "rahul@gmail.com"
]

print(set(emails))
print(len(set(emails)))
a=set(emails)
if len(a)!=len(emails):
    print("duplicate ele present")
else:
    print("Duplicate ele not present")

monday = {101, 102, 103, 104, 105}
tuesday = {102, 103, 105, 106, 107}
print(monday&tuesday)
print(monday-tuesday)
print(tuesday-monday)
print(monday|tuesday)
print(monday^tuesday)

rishi = {"Python", "SQL", "HTML", "CSS", "ML"}

rahul = {"Python", "Java", "SQL", "ML"}

priya = {"Python", "SQL", "ML", "JavaScript"}

print(rishi&rahul&priya)
print(rishi&rahul)
print(rishi-rahul)
print(rishi|rahul|priya)

