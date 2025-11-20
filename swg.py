import random
print("Welcome to the Game !")
computer_choice = random.randint(-1,1)
draw = 0
win = 0
loose = 0
while True :
    player_choice = input("Enter your Choice [snake/gun/water/quit]: ").lower()
    if player_choice == "snake" and computer_choice == -1:
        print("computer chose snake, Game drawed")
        draw += 1
    elif player_choice == "snake" and computer_choice == 1:
        print("computer chose gun, You loose!")
        loose += 1
    elif player_choice == "snake" and computer_choice == 0:
        print("computer chose water, You won!")
        win += 1
    elif player_choice == "water" and computer_choice == -1:
        print("computer chose snake, You loose!")
        loose +=1
    elif player_choice == "water" and computer_choice == 0:
        print("computer chose water, Game drawed")
        draw += 1
    elif player_choice == "water" and computer_choice == 1:
        print("computer chose gun, You won!")
        win +=1
    elif player_choice == "gun" and computer_choice == -1:
        print("computer chose snake, You won!")
        win +=1 
    elif player_choice == "gun" and computer_choice == 0:
        print("computer chose water, You loose !")
        loose +=1
    elif player_choice == "gun" and computer_choice == 1:
        print("computer chose gun, Game drawed")
        draw +=1
    else:
        print("Ok, Bye!")
        print("You won", win, "times")
        print("You loose", loose,"times")
        print("Game drawed", draw, "times")
        break
print("Thankyou For Playing !")
    

    