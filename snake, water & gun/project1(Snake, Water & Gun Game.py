'''
1 for snake
-1 for water
0 for gun

'''
import random
player = int(input("Enter your choice: "))
computer = random.choice([1, -1, 0])
print(computer)

if player == computer:
    print("It's a tie!")

else:
    if(player == 1 and computer == -1):
        print("You win! Snake beats water.")
    
    elif(player == 1 and computer == 0):
        print("You lose! Gun beats snake.")
    
    elif(player == -1 and computer == 1):
        print("You lose! Snake beats water.")
    
    elif(player == -1 and computer == 0):
        print("You win! Water beats gun.")

    elif(player == 0  and computer == 1):
        print("You win! Gun beats snake.")
    
    elif(player == 0 and computer == -1):
        print("You lose! Water beats gun.")

    else:
        print("Invalid input! Please enter 1 for snake, -1 for water, or 0 for gun.")




