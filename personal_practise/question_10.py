# reverseing the number 

n = int(input("enter the number: "))
r = 0
while n > 0:
    r = r*10+n%10
    n //= 10
print("reversed number is: ",r)