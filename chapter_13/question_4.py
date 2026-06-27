def divisible5(n):
    if(n%5 == 0):
        return True
    return False

a = [1 , 2 , 2334,  455, 3456, 567, 4567, 5678]

f = list(filter(divisible5 , a))
print(f)
