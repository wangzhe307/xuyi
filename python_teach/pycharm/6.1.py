def trim(s):
    if s==" ":
        print(s)
    elif s=='':
        print(s)
    elif s[0]==" ":
        s=s[1:]
        print(s)
    elif s[-1]==" ":
        s=s[:-1]
        print(s)
trim('')