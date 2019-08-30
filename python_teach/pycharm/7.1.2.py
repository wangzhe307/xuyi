from functools import reduce
def prod(x,y):
    return x*y

print(reduce(prod,[1,3,5,10]))
