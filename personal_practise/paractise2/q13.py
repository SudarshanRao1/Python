s = "abc123456def4565"

count = 0

for i in s:
    if i.isdigit():
        count += 1
print("count of digits = ", count)
 