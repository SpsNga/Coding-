import random 
number = random.randint(1,100)
print("Welcome to the Number Guessing Game ")



while True :
    n = int(input("Guess the number between 1 and 100 "))
    if n == number :
        print("Correct answer , Congrats , You Won !")
        break
    elif n < number :
        print("Too low !")    
    else :
        print("Too high")    

    
print("Thank you for playing the game !")