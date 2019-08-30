L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
V=[]
for i in L:
    print(i[0])
    V.append(i[0])
print(V)
print(sorted(V))

