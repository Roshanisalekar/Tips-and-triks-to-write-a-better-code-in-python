l=[30.90,67,89,67,23,45,13,12,11,22]
sorted_list=sorted(l)  #sorted_list=sorted(l,reverse=True) 
print(sorted_list)

dl=[
    {"name":"roshani","mark":39},
    {"name":"sakshi","mark":3},
    {"name":"nikita","mark":91},
    {"name":"jay","mark":9}]
sorted_data=sorted(dl,key=lambda x :x["mark"])

for i in sorted_data:
    print(i)