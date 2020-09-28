# Guess-number-Game
import random
randNumber = random.randint(1,100)
userGuess = None
guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("Enter your guess: "))
    guesses += 1
    if(userGuess==randNumber):
        print("you guesses it right!")
    else:
        if(userGuess>randNumber):
            print("you guesses is wrong!")
        else:
            print("you guesses it wrong!")

print(f"you guessed the number in {guesses} guesses")
        
