from functools import reduce
def str2float(s):
    nl = s.split(".")
    return reduce(lambda x, y: x * 10 + y, map(int, nl[0] + nl[1])) / (10 ** len(nl[1]))

print(str2float('123.456'))
