arr = [1,2,3,4,5]

rev = []

for i in range(len(arr)-1,-1,-1):
    rev.append(arr[i])
print(rev , end = " ")