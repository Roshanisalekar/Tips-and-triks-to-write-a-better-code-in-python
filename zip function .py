print("roshani has scored 90 marks in c++")
print("roshan has scored 60 marks in c#")
print("nikita has scored 80 marks in os")
print("nida has scored 50 marks in math")
print()

names=["roshani","roshan","nikita","nida"]
marks=[90,60,80,50]
subjects=["c++","c#","os","math"]

for name,mark,subject in zip (names,marks,subjects):
    print(name,"has scored",mark,"marks in",subject)