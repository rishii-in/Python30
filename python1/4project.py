print("="*50)
print("      🛡️  AI SCAM DETECTOR 2.0      ")
print("="*50)
print()
input("Enter message scan details (Press Enter):")
print()
risky=0
safe=0
susp=0
messages=0
risk=""
adv=""
action=0
while True:
    count=0
    messages+=1
    print("Is the sender unknown ?")
    print("1.Yes")
    print("2.No")
    ch=int(input("enter your choice: "))
    if ch==1:
        count+=1
        msg1="Unknown ⚠️"
    else:
        count=count+0
        msg1="Normal"
    print("\nDoes the message contain a suspicious link?")
    print("1.Yes")
    print("2.No")   
    ch=int(input("enter your choice: "))
    if ch==1:
        count+=1
        msg2="DETECTED "
    else:
        count=count+0
        msg2="Normal"
    print("\nIs the message asking for money?")
    print("1.Yes")
    print("2.No")   
    ch=int(input("enter your choice: "))
    if ch==1:
        count+=1
        msg3="YES 💰"
    else:
        count=count+0
        msg3="Normal"
    print("\nIs the message asking for OTP/password?")
    print("1.Yes")
    print("2.No")   
    ch=int(input("enter your choice: "))
    if ch==1:
        count+=1
        msg4="YES 🔐"

    else:
        count=count+0
        msg4="Normal"

    if count>=3:
        risk="🔴 High Risk"
        adv="⚠️  WARNING!"
        action="Verify through an official channel and report the message."
        risky+=1
    elif count==2:
        risk="🟡 Medium Risk"
        adv="⚠️  Be careful with this message."
        action="Verify the sender before responding."
        susp+=1
    elif count<=1:
        risk="🟢 SAFE"
        adv="✅  No major warning signs detected."
        action="You can proceed normally, but stay alert."
        safe+=1
    else:
        print("No Messages scanned")
    print()
    print("="*50)
    print("        🔍 MESSAGE ANALYSIS         ")
    print("="*50)
    print()
    print(f"Sender          : {msg1}")
    print(f"Suspisious Link : {msg2}")
    print(f"Money Request   : {msg3}")
    print(f"OTP Request     : {msg4}")
    print()
    print("-"*50)
    print()
    print(f"Risk Level : {risk}")
    print()
    print(f"Warning    :{adv}")
    print()
    print("🛡️  Recommended Action:")
    print(action)
    print()
    print("="*50)
    print("        🛡️ SECURITY SCANNER     ")
    print("="*50)
    print()
    print("1.Scan Another Message")
    print("2.View Security Message")
    print("3.Exit")
    ch=int(input("Enter your Choice :"))
    print()
    if ch==1:
        continue
    elif ch==2:
        print("="*50)
        print("      📊 SECURITY REPORT  ") 
        print("="*50)
        print()
        print(f"Total Messages Scanned : {messages}")
        print(f"🟢 Safe       : {safe}")
        print(f"🟡 Suspicious : {susp}")
        print(f"🔴 High Risk  : {risky}") 
        print()  
        input("Press Enter to return to Security Scanner...")
        print()
    elif ch==3:
        break
    else:
        print("\n Invalid choice !!")
print()
print("="*50)            
print("      Scam Detection checked  ✅    ")
print("="*50)


