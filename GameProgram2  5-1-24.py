import random

print("Welcome to Number Guessing Game")

x= random.randint(1,100)
#print(x)
a=int(input("Guess a number between 1-100 : "))

if a>=30 and a<=50:
    print("Your Guess is to Low")
elif a>50 and a<=80:
    print("Your Guess is to High")
elif x==a:
    print("Yes, Your Guess it")
