n = int(input("enter the table you want: "))

count = 0

while n > 0:
    n//=10
    count+=1
print("number of digits = ", count)