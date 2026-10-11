'''
from functools import reduce

def stud_analyze(name,marks):

    passed=list(filter(lambda x:x>=40,marks))
    bonus=list(map(lambda x:x+5,passed))
    total=reduce(lambda a,b:a+b,bonus,0)
    average=total/len(bonus) if bonus else 0
    high=list(filter(lambda x:x>=80,bonus))

    if average>=90:
        grade="A"
    elif average>=80:
        grade="B"
    elif average>=70:
        grade="C"
    elif average>=60:
        grade="D"
    else:
        grade="F"

    print("\n=========Student Analyse System================")
    print("\n Name:",name)
    print("\n Marks:",marks)
    print("\n Passed:",passed)
    print("\n Total",total)
    print("\n bonus:",bonus)
    print("\n average:",average)
    print("\n Grade:",grade)
    print("\n High Performance:",high)
    print("\n================================================")

student=int(input("enter no of students:"))

for i in range(student):

    name=input("\n enter name:")
    print()
    marks=list(map(int,input("enter marks[5]:").split()))

    stud_analyze(name,marks)
'''

def ask(question,options,correct):
    print("\n"+ question)
    for option in options:
        print(option)
    answer=input("enter your answer:").upper()

    if answer==correct:
        print("Correct Answer ✅")
        return 1
    else:
        print("Wrong Answer ❌")
        print("Correct Answer:",correct)
        return 0
def calculate(correct,total=5):
    score=(correct/total)*100
    return score
def show(correct,total):
    score=calculate(correct,total)
    print()
    print("="*50)
    print("      📊 INTERVIEW REPORT   ")
    print("="*50)
    print()
    print("Question Asked    :",total)
    print("Correct Answers   :",correct)
    print("Wrong Answers     :",total-correct)
    print(f"Score            :{score}%")
    if score >= 80:
        print("Status            : 🟢 EXCELLENT")
    elif score >= 60:
        print("Status            : 🟡 GOOD")
    else:
        print("Status            : 🔴 NEEDS PRACTICE")

    print("========================================")

def python():

    print("\n🐍 PYTHON INTERVIEW")
    print("----------------------------------------")

    correct = 0
    correct += ask(
        "Question 1: Which keyword is used to define a function?",
        ["A. function", "B. def", "C. define", "D. fun"],
        "B"
    )

    correct += ask(
        "Question 2: Which data type stores multiple items?",
        ["A. int", "B. float", "C. list", "D. bool"],
        "C"
    )

    correct += ask(
        "Question 3: Which symbol is used for comments?",
        ["A. //", "B. #", "C. /*", "D. @@"],
        "B"
    )

    correct += ask(
        "Question 4: Which collection stores key-value pairs?",
        ["A. List", "B. Tuple", "C. Set", "D. Dictionary"],
        "D"
    )

    correct += ask(
        "Question 5: Which keyword returns a value from a function?",
        ["A. print", "B. output", "C. return", "D. value"],
        "C"
    )

    show(correct,5)
def sql():

    print("\n🗄️ SQL INTERVIEW")
    print("----------------------------------------")

    correct = 0

    correct += ask(
        "Question 1: Which command is used to retrieve data from a table?",
        ["A. GET", "B. SELECT", "C. FETCH", "D. READ"],
        "B"
    )

    correct += ask(
        "Question 2: Which command is used to add a new row?",
        ["A. INSERT", "B. ADD", "C. UPDATE", "D. CREATE"],
        "A"
    )

    correct += ask(
        "Question 3: Which clause is used to filter records?",
        ["A. SORT BY", "B. FILTER", "C. WHERE", "D. CHECK"],
        "C"
    )

    correct += ask(
        "Question 4: Which command is used to modify existing data?",
        ["A. CHANGE", "B. MODIFY", "C. UPDATE", "D. ALTER"],
        "C"
    )

    correct += ask(
        "Question 5: Which keyword removes duplicate results?",
        ["A. UNIQUE", "B. DISTINCT", "C. REMOVE", "D. DIFFERENT"],
        "B"
    )

    show(correct, 5)


def dsa():

    print("\n🧩 DSA INTERVIEW")
    print("----------------------------------------")

    correct = 0

    correct += ask(
        "Question 1: Which data structure follows LIFO?",
        ["A. Queue", "B. Stack", "C. Array", "D. Graph"],
        "B"
    )

    correct += ask(
        "Question 2: Which data structure follows FIFO?",
        ["A. Stack", "B. Tree", "C. Queue", "D. Graph"],
        "C"
    )

    correct += ask(
        "Question 3: Which data structure consists of nodes and edges?",
        ["A. Stack", "B. Queue", "C. Graph", "D. Array"],
        "C"
    )

    correct += ask(
        "Question 4: What is the worst-case time complexity of linear search?",
        ["A. O(1)", "B. O(log n)", "C. O(n)", "D. O(n²)"],
        "C"
    )

    correct += ask(
        "Question 5: Which data structure is commonly used for recursion?",
        ["A. Stack", "B. Queue", "C. Graph", "D. Heap"],
        "A"
    )

    show(correct, 5)


def aiml():

    print("\n🤖 AI / ML INTERVIEW")
    print("----------------------------------------")

    correct = 0

    correct += ask(
        "Question 1: What does ML stand for?",
        ["A. Machine Learning", "B. Model Language",
         "C. Machine Logic", "D. Memory Learning"],
        "A"
    )

    correct += ask(
        "Question 2: Which is an example of supervised learning?",
        ["A. Classification", "B. Random guessing",
         "C. Data storage", "D. Sorting"],
        "A"
    )

    correct += ask(
        "Question 3: Which library is commonly used for numerical computing in Python?",
        ["A. NumPy", "B. Flask", "C. Tkinter", "D. Django"],
        "A"
    )

    correct += ask(
        "Question 4: What is the purpose of training data?",
        ["A. To train a machine learning model",
         "B. To delete a model",
         "C. To create a website",
         "D. To install Python"],
        "A"
    )

    correct += ask(
        "Question 5: Which technique is used to predict a category?",
        ["A. Classification", "B. Compilation",
         "C. Encryption", "D. Compression"],
        "A"
    )

    show(correct, 5)
print("="*50)
print("      🧠 AI INTERVIEW SIMULATOR    ")
print("="*50)
print()
print("Choose Interview:")
print("1.Python 🐍")
print("2.Sql 🗄️")
print("3.Dsa 🧩")
print("4.AI/ML 🤖")
print("5.Exit 🚪")
print()
ch=int(input("Enter your choice:"))

if ch==1:
    python()
elif ch==2:
    sql()
elif ch==3:
    dsa()
elif ch==4:
    aiml()
elif ch==5:
    print("\n Thanks for using AI interviewer Simulator. 😊  \n")
else:
    print("Invalid Choice ❌")


