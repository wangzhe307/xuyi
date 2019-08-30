def NUM(list):
    num = list[0]

    for i in list:

        if i>num:
            num=i
    print("max：",num)

    num1=list[0]
    for j in list:
        if j<num1:
            num1=j
    print("min：",num1)

NUM([1,2,3,4])
