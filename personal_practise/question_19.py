secert = 7
guess = 0

while guess != secert:
    guess = int(input("guess the number: "))
    
    if guess < secert:
        print("little low")
    elif guess > secert:
        print("too high")
    else:
        print("correct")