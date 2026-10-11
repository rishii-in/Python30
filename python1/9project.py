"""
python=set()
aiml=set()

print("======================== Student Course Manager  ==================================")
while True:
    print()
    print("1.Add student to python")
    print("2.Add student to aiml")
    print("3.Show students in both courses")
    print("4.Show python only students")
    print("5.Show aiml only students")
    print("6.Show all students")
    print("7.Show students in exactly one course")
    print("8.Search student")
    print("9.Show python students")
    print("10.Show aiml students")
    print("11.Exit")
    print()

    ch=int(input("Enter your choice:"))
    print()
    if ch==1:
        n=input("Enter name of student:")
        python.add(n)
        print()
        print("Added student succesfully")

    elif ch==2:
        n1=input("Enter name of the student:")
        aiml.add(n1)
        print()
        print("Added student succesfully")

    elif ch==3:
        print("------ Students in Both courses-----------")
        print()
        s1=python&aiml
        for i in s1:
            print(i)

    elif ch==4:
        print("------ Students only in python course-----------")
        print()
        s2=python-aiml
        for i in s2:
            print(i)

    elif ch==5:
        print("------ Students only in aiml course-----------")
        print()
        s3=aiml-python
        for i in s3:
            print(i)

    elif ch==6:
        print("-------- ALL Students----------------")
        print()
        total=python|aiml
        for i in total:
            print(i)

    elif ch==7:
        print("----------Exact one course------------")
        print()
        t1=python^aiml
        for i in t1:
            print(i)

    elif ch==8:
        name=input("Enter name of student:")
        print()
        if name in (python&aiml):
            print(f"{name} in both courses")
        elif name in python:
            print(f"{name} in python only")
        elif name in aiml:
            print(f"{name} in aiml only")
        else:
            print("No record of the student") 

    elif ch==9:
        print("-------- Python Students------------")
        print()
        n=python.copy()
        for i in n:
            print(i)

    elif ch==10:
        print("-------- Aiml Students------------")
        print()
        n1=aiml.copy()
        for i in n1:
            print(i)

    elif ch==11:
        print("Thanks fot Visiting ")
        print()
        print("See you again")       
        break
"""

print("="*50)
print("          💼 CAREER SKILL MATCHER  ")
print("="*50)
print()
skill=input("enter your skills:").lower().strip()
skills=set(skill.split(","))
print()
software_developer={"python","java","c++","html","css","javascript"}
full_stack_developer={"python","html","css","javascript","react","nodejs"}
data_scientist={"python","r","sql","statistics","machine learning"} 
product_company={"python", "java", "c++", "sql", "dsa", "git", "system design"}
service_company={"python", "java", "sql", "dsa", "aptitude", "communication"}
ai_engineer={"python","machine learning","deep learning","nlp","computer vision"}
while True:
    print("-"*50)
    print("Choose your Desired Career:")
    print("-"*50)
    print("1. Software Developer")
    print("2. Full Stack Developer")
    print("3. Data Scientist")
    print("4.AI Engineer")
    print("5.Product Company")
    print("6.Service Company")
    print("7.Exit")
    print("-"*50)
    print()
    ch=int(input("Enter your choice:"))
    print()
    if ch==1:
        career="software developer"
        career_skills=software_developer
    elif ch==2:
        career="Full Stack developer"
        career_skills=full_stack_developer
    elif ch==3:
        career="Data Scientist"
        career_skills=data_scientist
    elif ch==4:
        career="AI Engineer"
        career_skills=ai_engineer
    elif ch==5:
        career="Product Based Company"
        career_skills=product_company     
    elif ch==6:
        career="Service Based Company"
        career_skills=service_company     
    elif ch==7:
        print("Thanks for using Career Skill Matcher ")
        break
    else:
        print("Invalid Choice ❌")

    print("="*50)
    print("         📊 CAREER ANALYSIS  ")
    print("="*50)
    print()
    print(f"Career Selected : {career}")
    print()
    print("👤 Your skills :")
    for i in skills:
        print(i)
    print()
    print("-"*50)
    print()
    print("✅ MATCHING SKILLS")
    print("-"*50)
    skills_required=skills&career_skills
    count=len(skills_required)
    for i in skills_required:
        print(i)
    print()
    print("-"*50)
    print()
    print("❌ MISSING SKILLS")
    print()
    skills_learn=career_skills-skills
    for i in skills_learn:
        print(i)
    print()
    print("-"*50)
    print()
    percentage=(len(skills_required)/len(career_skills))*100
    if percentage>=70:
        status="🟢 Strong Skill Match"
    elif percentage>=40:
        status="🟡 Moderate chances to get a job"
    else:
        status="🔴 Needs to Improve"
    print("📊 Match Status :",status)
    print(f"🎯 Match Score :{len(skills_required)}/{len(career_skills)}")
    print(f"📈 Match  : {percentage}")
    print()
    print("💡 Recommendation:")
    print("Try to improve:")
    for i in skills_learn:
        print(i)
    print()
    print("-"*50)
print()
