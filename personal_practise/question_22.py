n = int(input("Enter the number: "))
o = n
t = 0 

while n > 0:
    digit = n % 10
    t += digit ** 3
    n //= 10

if t == o:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
