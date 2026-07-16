def fac(a):
    if a == 0:
        return 1
    
    return a*fac(a-1)

a = int(input("enter the number: "))
print(fac(a))