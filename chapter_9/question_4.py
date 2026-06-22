word = "Twinkle"

with open("pomes.txt" , "r") as f:
    c = f.read()
cn = c.replace(word , "########")

with open("pomes.txt" , "w") as f:
    f.write(cn)

