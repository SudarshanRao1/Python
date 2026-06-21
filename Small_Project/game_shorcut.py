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
        
        if((computer - player) == -1 or (computer - player) == 2):
            print("you Won!!")
        
        elif(not((computer - player) == -1 or (computer - player) == 2)):
            print("you Lost")

        else:
            print("something went wrong!!!")
            print("Try restarting game.")
            sys.exit(1)
    
    print("Wanna try again , press c for continue and e for exit")
    a = input("please Enter: ")

    if a == "c":
        computer = random.choice([-1 , 0 , 1])
        player = int(input("Enter your choice[-1 , 0 , 1 ]: "))
        
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
