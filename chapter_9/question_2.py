import random

def game():
    print("you are playing the game..")
    score = random.randint(1,62)

    # Fetch the high Score

    with open("Hi-Score.txt") as f:
        h = f.read()
        if(h != ""):
            h = int(h)
        else:
            h = 0

        print(f"Your Score: {score}")

        if(score > h):

            # write this high socre to file
            with open("Hi-Score.txt"  , "w") as f:
                f.write(str(score))
        
        return score    
    
game()