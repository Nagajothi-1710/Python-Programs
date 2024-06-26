import random

print("welcom to cows & bulls by Nagajothi")
print("It is a 2 digit number guessing game")

sn=str(random.randint(10,99))
chances=7
while chances>0:
    pg=input("Enter your Guess : ")
    if sn==pg:
        print("Yes, You Guessed it correct")
        print("You Won the Game")
        break
    else:
        cows=0
        bulls=0
        if sn[0]==pg[0]:
            bulls+=1
        if sn[1]==pg[1]:
            bulls+=1
        if sn[0]==pg[1]:
            cows+=1
        if sn[1]==pg[0]:
            cows+=1
        print("bulls : ",bulls)
        print("cows : ",cows)
        chances-=1
        if chances<1:
            print("You loss the Game")
            print("The secret number is : ",sn)
            break
            















        
