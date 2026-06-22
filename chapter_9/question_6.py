with open("log.txt") as f:
    c = f.read()

if "python" in c:
    print("yes python is present")
else:
    print("python is not present")