import sys
l=[i for i in range(90000)]
print(sum(l))
print(sys.getsizeof(l),"bytes")


g=(j for j in range(90000))
print(sum(g))
print(sys.getsizeof(g),"bytes")