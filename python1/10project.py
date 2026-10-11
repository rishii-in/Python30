'''
name=input("enter student name:")
print("enter marks:")
py=int(input("Python:"))
sql=int(input("Sql:"))
st=int(input("Statistics:"))
ml=int(input("Machine Learning :"))
m=int(input("Maths:"))
marks=[py,sql,st,ml,m]

def student_result(name,marks):
    total=sum(marks)
    avg=total/len(marks)
    percent=(total/500)*100

    def grade(percent):
            if percent>=90:
                return "A"
            elif percent>=80:
                return "B"
            elif percent>=70:
                return "C"
            elif percent>=60:
                return "D"
            else:
                return "F"
    def result(percent):
        if percent>=40:
            return "PASS"
        else:
            return "FAIL"

    res=grade(percent)
    res1=result(percent)
    return name,total,avg,percent,res,res1

a,b,c,d,e,f=student_result(name,marks)
print()
print("=========Student Result ===========")
print()
print("Name:",a)
print("Total:",b)
print("Average:",c)
print(f"Percentage: {round(d,2)}%")
print("Grade:",e)
print("Result:",f)
print()
print("=====================================")

'''
print("="*50)
print("     📱 SMARTPHONE DECISION ASSISTANT      ")
print("="*50)
print()
budget=int(input("Enter Your budget 💰 : ₹"))
print()
print("What will you mainly use the phone for?")
print("1.Gaming")
print("2.Photography")
print("3.Performance")
print("4.Battery")
print("5.All Rounder")
print()
ch=int(input("enter Your Choice: "))
def get_budget(budget):
    return budget
def get_purpose(ch):
    if ch==1:
        purpose="gaming"
        return purpose
    elif ch==2:
        purpose="photography"
        return purpose
    elif ch==3:
        purpose="performance"
        return purpose
    elif ch==4:
        purpose="battery"
        return purpose
    elif ch==5:
        purpose="all rounder"
        return purpose
    else:
        return "Invalid choice ❌"
def get_requirements(purpose):
    if purpose=="gaming":
        processor="High Performance"
        gpu="Strong Gpu"
        ram="8 GB+"
        storage="128 GB+"
        display="120 Hz+"
        battery="5000 mAh+"
        return processor,gpu,ram,storage,display,battery
    elif purpose=="photography":
        processor= "Efficient mid-to-high-end processor"
        gpu= "Good image-processing GPU"
        ram="8 GB or more"
        storage= "256 GB recommended"
        display= "AMOLED display with good color accuracy"
        battery= "4500 mAh or more" 
        return processor,gpu,ram,storage,display,battery  
    elif purpose=="performance":
        processor = "High-performance processor"
        gpu = "Powerful GPU"
        ram = "8 GB+"
        storage = "256 GB+"
        display = "120 Hz+"
        battery = "5000 mAh+"
        return processor,gpu,ram,storage,display,battery
    elif purpose=="battery":
        processor = "Power-efficient processor"
        gpu = "Efficient GPU"
        ram = "6 GB+"
        storage = "128 GB+"
        display = "AMOLED with adaptive refresh rate"
        battery = "5000 mAh+" 
        return processor,gpu,ram,storage,display,battery
    elif purpose=="all rounder":
        processor = "Balanced mid-to-high-end processor"
        gpu = "Good all-round GPU"
        ram = "8 GB+"
        storage = "128 GB+"
        display = "AMOLED 120 Hz"
        battery = "5000 mAh+"
        return processor,gpu,ram,storage,display,battery
    else:
        return "Invalid purpose ❌"

def suggestion(purpose):
    if purpose=="gaming":
        return "🎮 Prefer gaming-focused phones from ASUS ROG, iQOO, or POCO."
    elif purpose=="photography":
        return "📸 Prefer camera-focused phones from Apple iPhone, Samsung Galaxy, or Google Pixel."
    elif purpose == "performance":
        return "⚡ Prefer performance-focused phones from OnePlus, iQOO, Xiaomi, or Samsung."
    elif purpose == "battery":
        return "🔋 Prefer phones with large batteries from Samsung, OnePlus, Xiaomi, or Motorola."
    elif purpose == "all rounder":
        return "🌟 Consider well-balanced options from Apple iPhone, Samsung Galaxy, OnePlus, or Google Pixel."
    else:
        return "📱 Choose a phone based on your budget and main requirements."  
            
amount=get_budget(budget)
purpose1=get_purpose(ch)
if purpose1 == "Invalid choice":
    print("❌ Invalid choice. Please run the program again.")
else:
    processor,gpu,ram,storage,display,battery=get_requirements(purpose1)
    suggest=suggestion(purpose1)
print()
print("="*50)
print("          📊 PHONE ANALYSIS ")
print("="*50)
print()
print("Budget 💰    :",amount)
print("Purpose 🔍   :",purpose1)
print()
print("-"*50)
print()
print("⚡  Processor  :",processor)
print("🎮  GPU        :",gpu)
print("💾  RAM        :",ram)
print("💽  Storage    :",storage)
print("🖥️   Display    :",display)
print("🔋  Battery    :",battery)
print()
print("-"*50)
print()
print("💡 Suggestion :")
print()
print(suggest)
print()
print("-"*50)


