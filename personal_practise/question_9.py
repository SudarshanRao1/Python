n = int(input("enter the number: "))

i = 2
is_prime = True

while i < n:
    if n% i ==0 :
        is_prime = False
        break
    i += 1
if is_prime and n > 1:
    print("prime")
else:
    print("not prime")
