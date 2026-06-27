from functools import reduce

a = [1 , 2 , 24,  55, 34, 67, 45, 58]

def greater(a,b):
    if (a>b):
        return a
    return b

print(reduce(greater ,a))