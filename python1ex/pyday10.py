def greet():
    print("Welcome to python programming")
greet()

def greet2(name):
    print("Hello",name)
greet2("Rishi")

def square(n):
    return n*n
res=square(5)
print(res)

def even_or_odd(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
res=even_or_odd(14)
print(res)

def add(a,b):
    return a+b
print(add(5,5))

def max(a,b):
    if a>b:
        return a
    else:
        return b
print(max(2,3))

def percentage(marks,total_marks):
    total=sum(marks)
    return (total/total_marks)*100
print(percentage([80,70,95],300))

def calc(a,b):
    return a+b,a-b,a*b
add,sub,mul=calc(10,5)
print(add)
print(sub)
print(mul)

def student(name,branch="AI & ML"):
    return name,branch
print(student("Rishi"))
print(student("Ria","csm"))

def total(*num):
    return sum(num)
print(total(5,10,15,20))

def stu_det(**details):
    print(details)
stu_det(name='rishi',age=19,branch='csm')

def grade(marks):
    if marks>=90 and marks<=100:
        return "A"
    elif marks>=80 and marks<90:
        return "B"
    elif marks>=70 and marks<80:
        return "C"
    elif marks>=60 and marks<70:
        return "D"
    else:
        return "F"
print(grade(90))

def att(present,total):
    res=(present/total)*100
    if res>=75:
        return "Eligible",res
    else:
        return "Not Eligible",res
present=int(input("enter present days:"))
total=int(input("enter total days:"))
status,atten=att(present,total)
print(f"Attendence:{atten}%")
print("Status:",status)

def common(python,aiml):
    return python.intersection(aiml)
python={"Rishi","Ria","Vannu","Pavi"}
aiml={"Rishi","Vann","Raju"}
res=common(python,aiml)
print("Students in both courses:")
for i in res:
    print(i)

def res(name,marks):
    total=sum(marks)
    avg=(total/len(marks))
    percent=(total/500)*100

    def grade(percent):
        if percent>=90 and percent<=100:
            return "A"
        elif percent>=80 and percent<90:
            return "B"
        elif percent>=70 and percent<80:
            return "C"
        elif percent>=60 and percent<70:
            return "D"
        else:
            return "F"
    res=grade(percent)  
    return res,name,total,avg,percent

name=input("enter name :")
a,b,c,d,e=res(name,[65,72,68,75,70])
print()
print("========= Student Result ===========")
print()
print("Name:",b)
print("total:",c)
print("avg:",d)
print("percentage:",e)
print("Grade:",a)