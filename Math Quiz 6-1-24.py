import random

points=0
print("Welcome to Math Quiz")
print("----------------------")
print("Level 1: Addition (5 Questions)")
print("Level 2: Subration (5 Questions)")
print("Level 3: Multiblcation (5 Questions)")
print("Level 4: Division (5 Questions)")
print("Each correct Answer : 10 Points")
print("Each Wrong Answer : -5Points")
print("------------------------------------")
print("Level 1: Addition (5 Questions)")
print("")
for i in range(5):
    num1=random.randint(1,100)
    num2=random.randint(1,100)
    print("What is {} + {}?".format(num1,num2))
    sa=eval(input("Ans : "))
    if sa == num1+num2:
        print("you are correct answer")
        points+=10
    else:
        print("you are wrong answer")
        points-=5
        
print("--------------------------------------")
print("level 2: Subration (5 Question)")
print("")
for i in range(5):
    nums1=random.randint(1,100)
    nums2=random.randint(1,100)
    print("What is {} - {}?".format(nums1,nums2))
    st=eval(input("Ans : "))
    if st == nums1-nums2:
        print("You are correct answer")
        points+=10
    else:
        print("you are wrong answer")
        points-=5
    
print("--------------------------------------")
print("level 3: Multiblication (5 Question)")
print("")
for i in range(5):
    numm1=random.randint(1,15)
    numm2=random.randint(1,15)
    print("What is {} * {}?".format(numm1,numm2))
    so=eval(input("Ans : "))
    if so == numm1*numm2:
        print("You are correct answer")
        points+=10
    else:
        print("You are wrong answer")
        points-=5

print("--------------------------------------")
print("level 4: Division (5 Question)")
print("")
for i in range(5):
    numd1=random.randint(1,15)
    numd2=random.randint(1,15)
    print("What is {} / {}?".format(numd1,numd2))
    sd=eval(input("Ans : "))
    if sd == numd1/numd2:
        print("Yor are correct answer")
        points+=10
    else:
        print("You are wrong answer")
        points-=5
print("--------------------------------------")
print("Your points is ", points)
