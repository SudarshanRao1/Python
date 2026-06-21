
''' creating the snake , water , gun , game
  -1 for snake
   0 for water
   1 for gun
'''

import random
import sys

print('''\n!!!!!!!!RULES!!!!!!! 
              Enter 1 for Gun
              Enter 0 for Water
              Enter -1 for Snake
      ''')


mydictonary = { -1 : "Snake" , 0 : "Water" , 1 : "Gun"}


def logic(player , computer):

    # now we will print the both people choise

    print(f"You chose {mydictonary[player]}\nComputer chose {mydictonary[computer]}")
    
    if (computer == player):
        print("Its a draw")
    
    else:    
        if(computer == -1 and player == 0):
            print("you lost")
            print("Game over!!!!")
        
        elif computer == -1 and player == 1:
            print("you Won!!")
            print("Misson passed. let's go to next level!")
        
        elif computer == 0 and player == -1:
            print("you Won!!")
            print("Misson passed. let's go to next level!")

        elif computer == 0 and player == 1:
            print("you lost")
            print("Game over!!!!")
        
        elif computer == 1 and player == 0:
            print("you Won!!")
            print("Misson passed. let's go to next level!")
        
        elif computer == 1 and player == -1:
            print("you lost")
            print("Game over!!!!")
        
        else:
            print("something went wrong!!!")
            print("Try restarting game.")
            sys.exit(1)
    
    print("Wanna try again , press c for continue and e for exit")
    a = input("please Enter: ")

    if a == "c":
        computer = random.choice([-1 , 0 , 1])
        player = int(input("Enter your choice[-1 , 0 , 1]: "))

        if player not in mydictonary:
            print("Game Over!!!")
            print("you Entered wrong values\n")
            print("REMEMBER!")
            print("Enter the right values only any one of these three next time[-1 , 0 , 1]")
            sys.exit(1)

        logic(player , computer)
    
    elif a == "e":
        sys.exit(1)
    
    else:
        print("invalid please enter eiter c or e next time")
        print("session timout because of invalid input")
        sys.exit(1)
    
computer = random.choice([-1 , 0 , 1])
player = int(input("Enter your choice[-1 , 0 , 1]: "))

if player not in mydictonary:
    print("Game Over!!!")
    print("you Entered wrong values\n")
    print("REMEMBER!")
    print("Enter the right values only any one of these three next time[-1 , 0 , 1]")
    sys.exit(1)

logic(player , computer)
