#text based adventure game
name = input("What is your name ? ")
print("Welcome to the Adventure Game !", name)
print("Let's Start !")
answer = input("You are on a bridge , do u wanna cross it or jump into the river flowing under it ? (cross/jump) ")
if answer == "cross" :
     answer = input("You crossed the bridge and reached a town , do u wanna enter it? (yes/no) ")
     if answer == "yes" :
          print("u entered the town and got killed, u lose !")
     elif answer == "no":
          print("u ignored the town and got killed by archers , u lose !")
     else :
          print("Not a valid answer, u lose !")
    
elif answer == "jump":
     answer = input("U jumped into the river , now do u want to dive more or swim and reach the plain land ? (dive/land) ")
     if answer == "dive" :
         answer = input("u dived in more and ran out of oxygen , You lose !")
     elif answer == "land" :
          answer = input("U reached the land and found a Chinese Dragon , do u wanna ride it? (yes/no) ")
          if answer == "yes":
               answer = input("You are now riding the Dragon !!! , You just reached the City of Clouds , Do u wanna enter? (yes/no) ")
               if answer == "yes":
                    print("u enter the city , found gold and a new home ! You Won !!!")
               elif answer == "no":
                    print("u ignored the city and fell , You lose !")
               else:
                    print("Not a valid answer, You lose!")
          
          elif answer == "no":
               print("U ignored the Dragon and it burnt u , You lose !")
          else :
               print("Not a valid answer, You lose !")
     else :
          print("Not a valid answer, You lose !")


else :
     print("Not a valid answer, You lose !")