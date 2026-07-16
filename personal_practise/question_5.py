# printing the even numbers

a = int(input("enter the number must be more than 2: "))

if a <= 2:
    raise ValueError("enter anything more than 2")
    
for i in range(0,a + 1):

    if i % 2 == 0:
        print(i)
    
    i+=1