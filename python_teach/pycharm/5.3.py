def product(x, *y):
    s=x
    for i in y:
        s=s*i
    print(s)
product(2,3,4)