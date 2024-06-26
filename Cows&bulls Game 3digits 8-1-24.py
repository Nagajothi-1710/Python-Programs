import random

print("WELCOME TO COWS & BULLS GAME")
print("IT IS A 3 DIGIT NUMBER GAME")

sn=str(random.randint(100,999))
#print(sn)
chances=7
while chances>0:
    un=input("Enter the Number: ")
    
    if sn==un:
        print("YES, You are gussed it")                      
        print("You Won the game")                          
        break
    else:                                                   
        cows=0                                                 
        bulls=0
        if sn[0]==un[0]:
            bulls+=1
        if sn[1]==un[1]:
            bulls+=1
        if sn[2]==un[2]:
            bulls+=1
        if sn[0]==un[1]:
            cows+=1
        if sn[1]==un[0]:
            cows+=1
        if sn[0]==un[2]:
            cows+=1     
        if sn[2]==un[0]:
            cows+=1
        if sn[1]==un[2]:
            cows+=1
        if sn[2]==un[1]:
            cows+=1
        print("bulls: ",bulls)
        print("cows: ",cows)
        
        chances-=1
        if chances<1:
            print("You loss the Game")
            print("Better luck next time")
            print("Your secrect number is: ",sn)
            break
            
        
            
        


        
        
    
