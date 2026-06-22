# sum the first n natural numbers using recurssion

def sum(n):
    if (n == 1):
        return 1
    return sum(n - 1) + n

print(sum(int(input("enter the number: "))))

