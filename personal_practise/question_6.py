#  sum of the digits 
# we will enter a number then this will add all the digits inside that number


n = int(input("enter the number make sure it is atleast 2 digits: "))

t = 0
while n > 0:
    t += n % 10
    n = n//10
print("sum of the digits: " , t)    