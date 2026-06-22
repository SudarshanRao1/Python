with open("log.txt") as f:
    c = f.read()
with open("new.txt" , "w") as f:
    f.write(c)
