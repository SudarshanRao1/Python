def table(n):
    for i in range(1 , 11):
        print(f"{n} X {i} = {n * i}")
    print("\n")
    print("upside down\n")
    for i in range(10 , 0 , -1):
        print(f"{n} X {i} = {n * i}")
table(5)
