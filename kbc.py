print("Welcome to Sasta KBC")
print("You will be asked total 5 questions")
print("Each question carries 10 k Money reward")
print("So, Are you ready?")
i = input("yes/no: ")
if i.lower() == "no" or i.lower() == "n":
    print("ok bye")
elif i.lower() == "yes" or i.lower() == "y":
    print("lets start the game")
ques = ["q1. Who is the president of Russia?\n a. Vladimir Putin\n b. Joe Biden\n c. Xi Jinping\n d. Bill Gates\n",
        "q2. Who is the prime minister of India?\n a. Arvind Kejriwal \n b. Narendra Modi\n c. Rahul Gandhi\n d. Rajpal Yadav\n",
        "q3. What is the capital of India?\n a. Mumbai\n b. Delhi\n c. Kolkata\n d. Chennai\n",
        "q4. What is the currency of Japan?\n a. Yen\n b. Dollar\n c. Euro\n d. Rupee\n",
        "q5. Which is the largest planet in our solar system?\n a. Earth\n b. Jupiter\n c. Saturn\n d. Sun\n"]  
ans = ["a", "b", "b", "a", "b"]
prize = 0
for p in range(len(ques)):
    print(ques[p])
    a = input("Enter your answer: ")
    if a.lower() == ans[p]:
        prize += 10
        print(f"Correct Answer! You have won {prize}k")
    else:
        print("Wrong Answer! You lost the game")
        break
print(f"You have won a total of {prize}k")
print("Thank you for playing Sasta KBC")