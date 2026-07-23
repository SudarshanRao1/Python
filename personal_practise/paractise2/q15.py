s = "beautiful"
res = ""
a = "aeiou"
for i in s:
    if i not in a:
        res += i
print(res)