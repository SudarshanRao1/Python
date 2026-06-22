'''c/5 = f-32/9'''
# celcious to forienheit conversion using the function

def heatconversion(f):
    return 5 * (f - 32)/9

f = int(input("enter the temp.: "))
c = heatconversion(f)
print(round(c , 3))

# round function will round of the things
