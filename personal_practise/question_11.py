# palendrome number 

n = int(input("enter the number: "))
a = n
r = 0
while n > 0:
    r = r*10+n%10
    n //= 10

if a == r:
    print("palindrome")
else:
    print("not a palindrome")