import itertools
def pi(N):
    list1=[]
    list2=[]
    for i in range(N):
        list1.append((i+1)*2-1)
    for x,y in enumerate(list1):
        list1[x]=4/(y*pow(-1,x))
    return sum(list1)
    #print(sum(list1))

print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')