import random
randNumber=random.randint(1,100) #we are creating numbers from 1 to 100
# print(randNumber)it will show the random number
userGuess=None
guesses=0

while(userGuess!=randNumber):
    userGuess=int(input("enter your guess:"))
    guesses+=1
    if(userGuess==randNumber):
        print("you guessed it right!")
    else:
        if(userGuess>randNumber):
            print("you guessed it wrong!enter a smaller number")
        else:
            print("you guessed it wrong!enter a larger number")
print(f"you guessed the number in {guesses} guesses")
with open("highscore.txt","r")as f:
    highscore= int(f.read())
if (guesses<highscore):
    print("you have just broken the high score")
with open("highscore.txt","w") as f:
    f.write(str(guesses))

