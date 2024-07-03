import random
import time

print("Game is booting...")

time.sleep(1)

print("Game is Started!")

name = input ("Enter your name: ")

print (f"wlecome {name}, to our game, Rock, Paper & Sciecors")
game_choice = random.randrange(0, 2)

user_input = input("Pick a object, like [R] , [P] ,[S] ").lower()

if (user_input == "r" or user_input == "p" or user_input == "s"):
    # Rock 0 
    if (user_input == "r"):
        if (game_choice== 0):
            print('You win its rock!!')
        else: 
            print("You lose!")

    # Paper 1
    elif (user_input == "p"):
        if (game_choice == 1):
            print("You win its rock!!")
        else:
            print("You lose!")

    # Ssc .. 2
    elif (user_input == "s"): 
        if (game_choice == 2): 
            print('You win!')  
        else:
            print("You lose!")
    
else:
    print("Bad input, try using [R] Rock, [P] Paper & [S] Sciecors")