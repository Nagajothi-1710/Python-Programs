import random

print("Welcome to Number Guessing Game")

x = random.randint(1,100)
#print(x)
a=int(input("Guess a number between 1-100 : "))
if x == a:
    print("Yes, You Guess it")
else:
    print("No, you are wrong")

    
