import random


print("Welcome to Guessing Colours Game")
print("*********************************")
colours=["Red","Yellow","Brown","Pink","Blue","Orange","Black"]
c=random.choice(colours)
print("Red,Yellow,Brown,Pink,Blue,Orange,Black")
print("---------------------------------------")
us=input("Gussing the colour among them : ")
if c==us:
    print(" ")
    print("Your Guess is correct")
else:
    print(" ")
    print("Your Guess is wrong")
