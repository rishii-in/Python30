dict={
    "name":"Rishi",
    "age":19,
    "branch":"CSM"
}

print(dict)
print(dict["age"])

dict["Cgpa"]=9.1

dict["age"]=20

print(dict)

for i in dict:
    print(i)

for i in dict.values():
    print(i)

dict={
    "name":"Rishi",
    "age":20,
    "branch":"csm"
}

for k,v in dict.items():
    print(k,':',v)

print(dict.get("branch","Not Found"))


dict={
    "name":"Rishi",
    "age":20,
    "branch":"csm"
}

dic=input("enter a key :  ")
if dic in dict:
    print(dict[dic])
else:
    print("Not Found")

print(dict.get("phn","No Phn Number"))

dict.pop("branch")
print(dict)

print(dict)
dict.popitem()
print(dict)

dict.clear()
print(dict)

dict={
    "name":"Rishi",
    "age":20,
    "branch":"csm"
}

dic1=dict.copy()
dic1["age"]=21
print(dic1)
print(dict)

stud={
    "stud1":{
        "name":"rishi",
        "age":19,
        "branch":"csm"
    },
    "stud2":{
        "name":"vannu",
        "age":19,
        "branch":"csm"
    }
}

print(stud["stud2"])

stud["stud1"]["age"]=22
print(stud["stud1"])

for i in stud:
    print(i)
    for n in stud[i]:
        print(n,':',stud[i][n])

dict2={
    "marks":[90,80,60,92]
}
print(sum((dict2["marks"])))
summ=sum((dict2["marks"]))

print(summ/len(dict2["marks"]))
