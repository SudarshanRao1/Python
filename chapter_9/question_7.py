with open("log.txt") as f:
    c = f.readlines()

lineno = 1
for line in c:
    if ("python" in line):
        print(f"yes python is present at the line -> {lineno}")
        break
    lineno += 1
    
else:
    print("python is not present")
