f = open("pomes.txt")

c = f.read()

if("Twinkle".lower() in c):
    print("The word twinkle is present in the poem")
else:
    print("The word twinkle is not present in the poem")

f.close()
