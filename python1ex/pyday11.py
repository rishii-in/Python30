def greet():
    print("Hello, Python")
x=greet()

def square(n):
    return n*n
def execute(func,value):
    return func(value)
value=int(input("enter value:"))
print(execute(square,value))

def outer():
    def inner():
        print("Hello from inner")
    return inner
x=outer()
x()

add=lambda a,b:a+b
print(add(10,20))

check=lambda x:"even" if x%2==0 else "odd"
print(check(7))

big=lambda a,b:a if a>b else b
print(big(65,25))

num=[1,2,3,4,5]
res=map(lambda x:x**2,num)
print(list(res))

marks=[60,70,80,90]
res=map(lambda x:x+5,marks)
print(list(res))

num=[10,15,20,25,30,35]
res=filter(lambda x:x%2==0,num)
print(list(res))

marks = [35, 67, 42, 89, 28, 76]
res=filter(lambda x:x>=40,marks)
print(list(res))

from functools import reduce
numbers = [10, 20, 30, 40]
total=reduce(lambda a,b:a+b,numbers)
print(total)

from functools import reduce
numbers = [2, 3, 4, 5]
total=reduce(lambda a,b:a*b,numbers)
print(total)

marks = [45, 67, 82, 38, 91, 56]
passed=list(filter(lambda x:x>=40,marks))
print(f"Passed:{list(passed)}")
bonus=map(lambda y:y+5,passed)
print(f"After bonus:{list(bonus)}")

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even=list(filter(lambda x:x%2==0,numbers))
sqr=list(map(lambda x:x**2,even))
total=reduce(lambda a,b:a+b,sqr)
print(f"Even : {even}")
print(f"Squares:{sqr}")
print(f"Total :{total}")


marks = [35, 55, 72, 40, 88, 30, 95]
passed=list(filter(lambda x:x>=40,marks))
print(f"Passed:{list(passed)}")
bonus=list(map(lambda y:y+5,list(passed)))
print(f"After bonus:{list(bonus)}")
total=reduce(lambda a,b:a+b,bonus)
print(f"Total:{total}")
