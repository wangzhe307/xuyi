import math
def quadratic(a, b, c):
    t=pow(b, 2) - 4 * a * c
    if t>0:
        x1=(-b+pow(t,0.5))/(2*a)
        x2=(-b-pow(t,0.5))/(2*a)
        print(x1,x2)
    else:
        print("输入不符合条件")
quadratic(3,5,1)
