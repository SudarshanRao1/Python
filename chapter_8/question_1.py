
def vaishnavi(a , b , c):
    if(a > b and a > c):
        return a
    elif(b > a and b > c):
        return "b is the greatest one"
    elif(c > a and c > b):
        return c
    
a = int(input("enter number: "))
b = int(input("enter number: "))
c = int(input("enter number: "))

x = vaishnavi(a , b ,c)

print("the greatest number is: ",x)
