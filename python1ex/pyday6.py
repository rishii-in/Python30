f=["apple","mango","banana","kiwi"]
print(f)

m=[90,80,70,60]
print(m[0])
print(m[-1])

colors=["red","blue","green"]
print(colors[1])

emp=["raju","ramu","raghu"]
emp.append("Rishi")
print(emp)

n=[10,20,30]
n[1]=200
print(n)

city=["vij","hyd","chennai"]
city.insert(1,"banglore")
print(city)

f=["apple","mango","banana"]
f.remove("banana")
print(f)

n=[10,20,30,40,50]
print(n[1:4])

print(n[::-1])

l1=[1,2]
l2=[3,4]
print(l1+l2)

n=[1,2]
print(n*4) 

lang=["java","python","c"]
print("python" in lang)

n=[10,2,30,40,50]
rem=n.pop()
print(f"removed value:{rem}")
print(f"updated list: {n}")

stud=["a","b"]
stud.extend(["c","d","e"])
print(stud)

emp=["raju","ramu","vannu","rishi"]
for i in emp:
    print(f"emp : {i}")

i=0
while i<len(emp):
    print(emp[i])
    i+=1

n=[10,20,30,40]
n[1:]=[200,300,400]
print(n)

cart=["milk","rice","eggs"]
cart.append("bread")
cart.remove("rice")
cart.insert(1,"butter")
print(cart)

m=["raju","ria"]
e=["vannu","rishi"]
print(m+e)
print("priya" in m+e)

