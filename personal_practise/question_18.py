n = int(input("enter the number of rows: "))

i = 1

while i<=n:
    print(" "*(n-1) + "*" * (2*i-1))
    i += 1
i = n-1

while i >= 1:
    print(" "*(n-1) + "*" * (2*i-1))
    i = i-1
