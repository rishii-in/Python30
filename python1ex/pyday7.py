t=(10,20,30,40,50)
print(t)

t1=("rishi",19,"CSM")
print(t1)

t2=()
print(type(t2))

t3=('python',)
print(t3)
print(type(t3))

n=[10,20,30,40]
n1=tuple(n)
print(n1)

st="Python"
t=tuple(st)
print(t)

c=("Red","Blue","Green")
print(c[0])

print(c[-1])

m=(90,80,70,60)
print(len(m))

f=("apple","mango","banana")
if "apple" in f:
    print("True")

n=(10,20,30,40,50,60)
print(n[1:4])

print(n[:4])

print(n[-3:])

print(n[::-1])

print(n[1::2])

mem=(10,20,30,20,40,20)
print(mem.count(20))

f=("Apple","mango","orange","banana")
print(f.index("orange"))

stu=("Rishi",19,"AIML")
name,age,branch=stu
print(name,age,branch)

n=(10,20,30,40,50)
a,*b=n
print(a)
print(b)

copy=n[:]
print(copy)

t=(1,2,3,2,3,2)
print(t.count(2))
print(t.index(3))

for i in t:
    print(i)

i=0
while i<len(t):
    print(t[i])
    i+=1

max=0
p=(1,4,6,3,2)
for i in p:
    if i>max:
        max=i
print(max)


p=(4,6,3,2,7)
min=p[0]
for i in p:
    if i<min:
        min=i
print(min)

sum=0
p=(1,5,2,8,6)
for i in p:
    sum+=i
print(sum)
avg=0
print(sum/len(p))

c1=0
c2=0
p=(10,15,22,17,40,55)
for i in p:
    if i%2==0:
        c1+=1
    else:
        c2+=1
print(c1)
print(c2)

n=("rishi","vannu","ria","ammu")
name=input("enter name to search:")
if name in n:
    print(f"name is found at index {n.index(name)}")
else:
    print("Not Found")

employee = ("Rishi","EMP101","Developer",75000)
name,empid,role,salary=employee
print("Name :",name)
print("ID no:",empid)
print("role:",role)
print("salary:",salary)


m=(10,50,70,20,50,70,60,70,40,50)
for i in m:
    if i>50:
        print(i)

month=("jan","feb","mar","apr","may","june","july","aug","sep","oct","nov","dec")
m=input("enter month : ")
if m in month:
    print(month.index(m))


t=(30,25,27,38,40,22,42)
h=0
c=t[0]
sum=0
for i in t:
    sum+=i
    if i>h:
        h=i
    if i<c:
        c=i
print(f"hottest day: {h}")
print(f"coldest day :{c}")
print(f"avg is {sum/len(t)}")



