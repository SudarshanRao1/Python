
def generatetable(n):
    table = ""
    for i in range(1,11):
        table += f"{n} X {i} = {n*i}\n"
    
    with open(rf"C:\Users\SUDARSHAN\OneDrive\Documents\Python\chapter_9\tables/table_{n}.txt" , "w") as f:
        f.write(table)


for i in range(2,21):
    generatetable(i)