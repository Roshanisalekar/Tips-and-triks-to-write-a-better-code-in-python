l=[50,30,58,45,70,90]
a=[]
for i in l:
    a.append(i*2)
print("using for loop",a)


x=[i*2 for i in l]
print("using  list comprehensions ",x)