"""
file=open("data/notes.txt","r")
count=0
words=0
for i in file:
    data=i.strip()
    print(data)
    count+=1
    words+=len(data.strip().split())
print(f"lines : {count}")
print(f"words : {words}")
file.close()

file=open("data/messages.txt","r")
count=0
for line in file:
    data=line.strip().split()
    count+=1
    print(f"Line {count} : {len(data)} words ")
file.close()

file=open("data/students.txt","r")
student=input("enter student name:")
found=0
for i in file:
    data=i.split()
    if student in data:
        print("student found")
        found=1
if found==0:
    print("student not found")
file.close()

file=open("data/marks.csv","r")
file.readline()
max=0
top=""
low=""
total=0
count=0
min=100
avg=0
for i in file:
    data=i.strip().split(",")
    for i in data:
        total+=int(data[1])
        count+=1
        if int(data[1])>max:
            max=int(data[1])
            top=data[0]
        if int(data[1])<min:
            min=int(data[1])
            low=data[0]
    avg=total/count
print(f"Max Marks :{max}")
print(f"Min Marks :{min}")
print(f"Top student :{top}")
print(f"Low student :{low}")
print(f"Average marks :{avg}")
file.close()

file=open("data/employees.csv","r")
count=0
total=0
top=0
topname=""
name=[]
file.readline()
for i in file:
    data=i.strip().split(",")
    total+=int(data[1])
    count+=1
    if  int(data[1])>top:
        top=int(data[1])
        topname=data[0]
    if int(data[1])>30000:
        name.append(data[0])
            

print(f"Total employees : {count}")
print(f"total salary :{total}")
print(f"average :{total/count}")
print(f"Highest salary : {top}")
print(f"Highest paid employee : {topname}")
print(f"Employees with more  than 30000")
for i in name:
    print(i)
file.close()

file=open("data/expenses.txt","r")
total=0
list1={}
exp=0
item=input("enter category name:").lower()
for i in file:
    data=i.strip().split(",")
    total+=int(data[1])
    if data[0].lower()==item:
        exp+=int(data[1])
    if data[0].lower() in list1:
        list1[data[0].lower()]+=int(data[1])

    else:
        list1[data[0].lower()]=int(data[1])

print("============================")
print(f"    Expense Traker        ")
print("============================")
print()
print(f"Total expenses: {total}")
print()
print(list1)
print()
print(f"Item searched :{item} total : {exp}")
file.close()

file=open("data/products.csv","r")
file.readline()
max=0
highpr=""
value=0
for line in file:
    data=line.strip().split(",")
    name=data[0]
    price=int(data[1])
    quantity=int(data[2])
    value=price*quantity
    print(f"{name}->{value}")

    if value>max:
        max=value
        highpr=data[0]
print(f"Higher product value :{highpr}")
print(f"value : {max}")
file.close()


file=open("data/story.txt","r")
list1={}
for line in file:
    data=line.strip().lower().split()
    for word in data:
        if word in list1:
            list1[word]+=1
        else:
            list1[word]=1
file.close()

print()
for word in list1:
    print(word,":",list1[word])

item=input("enter the word to search :")
if item.lower() in list1:
    print(f"{item} found {list1[item]} times")
else:
    print(f"{item} not found !!")

"""

file=open("data/results.csv","r")
file.readline()
total=0
avg=0
max=0
min=300
maxname=""
minname=""
avgs=[]
for line in file:
    data=line.strip().split(",")
    print(data[0])
    total=int(data[1])+int(data[2])+int(data[3])
    avg=total/(len(data)-1)
    print(f"total : {total}")
    print(f"Average : {avg}")
    if total>max:
        max=total
        maxname=data[0]

    if total<min:
        min=total
        minname=data[0]

    avgs.append(avg)

print("========================")
print()
print(f"Highest total: {max}")
print(f"Top student : {maxname}")
print()
print(f"Lowest Total : {min}")
print(f"Lowest student : {minname}")
print()
print(f"class average : {sum(avgs)/len(avgs)}")
file.close()

file=open("data/sales.csv","r")
file.readline()
total=0
value=0
max=0
maxname=""
list1={}
for line in file:
    data=line.strip().split(",")
    value=int(data[1])*int(data[2])
    list1[data[0]]=value
    total+=value
    if value>max:
        max=value
        maxname=data[0]
print()
print("=========================")
print("     Sales Report         ")
print("===========================")
print()
for i in list1:
    print(i ,"  :",list1[i])
print()
print(f"Total sales : {total}")
print()
print(f"Highest sale :")
print(f"{maxname} -> {max}")

file=open("data/sales.csv","r")
data=file.read()
file.close()
file=open("data/sales_report.txt","a")
file.write(data)
file.close()
print(file.closed)