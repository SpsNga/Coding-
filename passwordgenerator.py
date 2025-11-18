import random 
import string
l = int(input("Enter the length of the password: "))
password = ""
for i in range(l):
    password += random.choice(string.ascii_letters + string.digits + string.punctuation)
print("Generated password:", password)