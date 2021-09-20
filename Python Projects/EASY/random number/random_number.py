import random as rd
print("*Guessing The Number Game*")
print("Guess the number between 1 to 100\nNote : You have only 10 chance")
flag = 'Y'
while(flag=='Y' or flag=='y'):
    n = rd.randint(1,101)
    turn = 1
    while(turn<=10):
        x = int(input())
        if(x==n):
            print("You Win!!!!! in ",turn," turns")
            break
        elif(x > n and (turn != 10)):
            print("Number which you entered is greater\nEnter smaller number")
        elif(x < n and (turn != 10)):
            print("Number which you entered is smaller\nEnter larger number")
        if(turn != 10):
            print("Number of turns left : ",10-turn)
        turn=turn+1
    if(turn > 10):
        print("Unfortunately..You..Lost..")
    print("Do you want to try for more time(Y/N) : ",end="")
    flag = input()


print("Thank You!!!")