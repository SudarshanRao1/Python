word = ["Twinkle" , "twinkle"]

with open("pomes.txt" , "r") as f:
    c = f.read()

for i in word:
    c = c.replace(i , "#" * len(word))

with open("pomes.txt" , "w") as f:
    f.write(c)

