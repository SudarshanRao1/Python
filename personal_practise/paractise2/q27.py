arr = [1, 2, 3, 2, 4, 5, 1]

u = []

for i in arr:
    if i not in u:
        u.append(i)

print(u, end=" ")