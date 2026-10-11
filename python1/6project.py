print("================================================")
print("========= Shopping Bill Generator =============")
print("================================================")
print()
pname=[]
price=[]
while True:
    print()
    print("1.Add Product")
    print("2.Remove Product")
    print("3.View cart")
    print("4.Search Product")
    print("5.Generate Bill")
    print("6.Clear Cart")
    print("7.Exit")
    print()
    ch=int(input("enter choice : "))
    if ch==1:
        print()
        pn=input("enter product name :")
        print()
        p=int(input("enter product price :"))
        pname.append(pn)
        price.append(p)
        print()
        print("✅Product added Successfully")
        print()
        print(pname)
        print(price)

    if ch==2:
        print()
        name=input("enter product name: ")
        print()
        if name in pname:
            i=pname.index(name)
            pname.pop(i)
            price.pop(i)
            print(pname)
            print(price)
            print()
            print("Removed Succesfully")
            print()
        else:
            print()
            print("Not Found !!")
            print()

    if ch==3:
        print()
        print("============ cart ==============")
        print()
        index=0
        while index<len(pname):
            print(f"1. {pname[index]} -- ${price[index]}")
            index+=1

    if ch==4:
        print()
        pr=input("enter product name:")
        print()
        if pr in pname:
            i=pname.index(pr)
            print(F"Product {pr} is found and price : {price[i]}")
        else:
            print()
            print("Not Found!!")
            print()

    if ch==5:
        print("-----------Bill--------------")
        i=0
        while i<len(pname):
            print(f"1.{pname[i]} -- {price[i]}")
            i+=1
        print()
        print(f"Items -{i}")
        print(f"Bill - {sum(price)}")
        print()
        print("THANKS FOR SHOPPING !!")
        print()

    if ch==6:
        print()
        i=input("Are you Sure(yes/no): ")
        if i=="yes":
            pname.clear()
            price.clear()
            print()
            print("Cart is cleared successfully")
            print()
        else:
            continue

    if ch==7:
        print("Thanks For shopping !!")
        print()
        print("Visit Again")
        print()
        break