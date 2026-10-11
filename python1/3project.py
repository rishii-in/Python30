print()
print("==============================================")
print("               RBI BANK ATM                   ")
print("==============================================")
print()
name=input("Enter Account Holder Name : ")
correct_pin=3507
balance=10000
pin=int(input("Enter PIN : "))
print()
if pin==correct_pin:
    print(f"welcome {name}")
    print()
    print("--------Menu--------")
    print("1.check Balance")
    print("2.withdraw")
    print("3.deposit")
    print("4.exit")
    print()
    ch=int(input("enter your choice:"))

    if ch==1:
        print("======================================")
        print(f"Current Balance :{balance}")
        print("======================================")
        print()
    elif ch==2:
        print()
        withdraw=int(input("enter amount for withdraw:"))
        print()
        if withdraw<=balance:
            balance -= withdraw
            print("WITHDRAW succesfull")
            print(f"amount withdraw :{withdraw}")
            print(f"Balance amount : {balance}")
            print()
        else:
            print(f"Insufficient Balance: {balance}")
            print()
    elif ch==3:
        print()
        deposit=int(input("enter amount to deposit:"))
        print()
        print("Deposit succesful")
        print()
        print(f"deposited amount : {deposit}")
        print()
        balance+=deposit
        print(f"Updated balence : {balance}")
        print()
    elif ch==4:
        print()
        print("Thanks for using RBE bank Atm")
        print()
        print("Visit Again")
        print()
    else:
        print()
        print("Invalid choice")
        print()
else:
    print()
    print("Incorrect PIN")
    print()
    print("Access Denied")
    print()

'''
book=10
while True:
    print("=========================")
    print("      Library System     ")
    print("=========================")
    print()
    print("1.Borrow Book")
    print("2.Return Book")
    print("3.Check books")
    print("4.Exit")
    print()
    ch=int(input("Enter choice(1-4):"))
    if ch==1:
        b1=int(input("enter number of books:"))
        if b1>book:
            print("Books Not Available")
        else:
            print()
            book=book-b1
            print("Borrow Succesfull")
            print(f"Books Borrowed:{b1}")

            print(f"Available books:{book}")          
            print()
    elif ch==2:
        b2=int(input("enter no of books : "))
        print()
        book=book+b2
        print("Books Returned")
        print(f"Books Returned:{b2}")
        print(f"Available books : {book}")


    elif ch==3:
        print()
        print(f"Available Books are :{book}")

    elif ch==4:
        print()
        print("Thanks For Visiting the Library")
        print("Visit Again")
        break
    else:
        print()
        print("Invalid Choice!")

'''