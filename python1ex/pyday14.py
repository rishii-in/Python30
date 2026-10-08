print(10/0)

age=int(input("enter age:"))
print(age)

num= [10, 20, 30]
print(num[4])

student = {
    "name": "Ravi",
    "age": 20
}
print(student["branch"])

file=open("python.txt","r")

try:
    age=int(input("enter num:"))
except:
    print("invalid number")

try:
    a=int(input("enter 1"))
    b=int(input("enter 2"))
    print(a/b)
except:
    print("zero is not divisible")

try:
    file=open("python.txt","r")
    file.close()
except:
    print("file not found")



try:
    n=int(input("enter an integer:"))
    print(n)
except ValueError:
    print("invalid input !!")


res=0
try:
    one=int(input("enter num 1: "))
    two=int(input("enter num 2: "))
    res=one/two
    print(res)
except ValueError:
    print("Invalid value")
except ZeroDivisionError:
    print("Zero cannot be divided")




numbers = [10, 20, 30, 40, 50]
try:
    i=int(input("enter index no:"))
    print(numbers[i])
except IndexError:
    print("Invalid index")
except ValueError:
    print("Invalid input")



student = {"name": "Ravi", "age": 20, "marks": 85}
try:
    key=input("enter a key:")
    print(student[key])
except KeyError:
    print("Key not exists")



res=0
try:
    one=int(input("enter num 1: "))
    two=int(input("enter num 2: "))
    res=one/two
except ValueError:
    print("Invalid value")
except ZeroDivisionError:
    print("Zero cannot be divided")
else:
    print(res)

try:
    age=int(input("enter age:"))
    print(age)
except ValueError:
    print("Invalid input")
finally:
    print("Program completed ")

try:
    m1=int(input("enter marks:"))

    if m1<0 or m1>100:
        raise ValueError("Invalid value")
except ValueError as e:
    print(e)
else:
    print("Valid Marks")

try:
    balance=int(input("enter balance:"))
    withdraw=int(input("enter withdraw amount"))

    if withdraw<=0:
        raise ValueError("withdraw is less")
    if withdraw>balance:
        raise ValueError("More withdraw")
except ValueError as e:
    print(e)
else:
    print("Sucess")
finally:
    print("ATM session ended")

class AgeError(Exception):
    pass
try:
    age=int(input("enter age:"))
    print(age)
    if age<18:
        raise AgeError("Invalid number")
except AgeError as e:
    print(e)

class InvalidMarksError(Exception):
    pass
try:
    m1=int(input("enter marks:"))

    if m1<0 or m1>100:
        raise InvalidMarksError("Invalid value")
except ValueError as e:
    print(e)
except InvalidMarksError as e:
    print(e)
else:
    print("Valid Marks")
finally:
    print("end")

class OutOfStockError(Exception):
    pass
try:
    q1=int(input("enter q1:"))
    q2=int(input("Enter q2:"))
    if q2<q1:
        raise OutOfStockError("Out of cart:")
except OutOfStockError as e:
    print(e)
else:
    print("IN cart")
finally:
    print("End")



class InsufficientBalanceError(Exception):
    pass
class InvalidWithdrawError(Exception):
    pass

try:
    balance=int(input("enter balance:"))
    withdraw=int(input("enter withdraw amount:"))

    if withdraw>balance:
        raise InsufficientBalanceError("Insufficient Balance")
    if withdraw<=0:
        raise InvalidWithdrawError("Zero or negative Withdrawl")
except ValueError:
    print("invalid Input")
except InsufficientBalanceError as e:
    print(e)
except InvalidWithdrawError as e:
    print(e)
else:
    balance=balance-withdraw
    print(f"Balance amount: {balance}")
    print("succesfull")
finally:
    print("ATM session ended")



class AgeError(Exception):
    pass
class MarksError(Exception):
    pass
try:
    name=input("enter name: ")
    age=int(input("enter age: "))
    marks=int(input("enter marks: "))

    if age<1 or age>120:
        raise AgeError("Invalid Age")
    if marks<0 or marks>100:
        raise MarksError("Invalid Marks")
except ValueError:
    print("Invalid Input")
except AgeError as e:
    print(e)
except MarksError as e:
    print(e)
else:
    print("Student Details are valid")
    print(f"Name: {name}")
    print(f"Age :{age}")
    print(f"Marks: {marks}")
finally:
    print("Validation Completed !!")



try:
    filename=input("enter file name:")
    file=open(filename,"r")
except FileNotFoundError:
    print("File not Found")
else:
    print("File Contents")
    data=file.read()
    print(data) 
    print("File Read Successfully")
finally:
    print("File operation completed")



