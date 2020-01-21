'''
Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
(Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
'''

import random
randomNumber = random.randint(1,9)
totalGuesses = 0
while True:
    try:
        guess = int(input("Take a guess between 1 and 9\n$ "))
        totalGuesses += 1
        if guess < randomNumber:
            print("Too low...")    
        elif guess > randomNumber:
            print("Too high...")
        else:
            break
    except:
        pass
print(f"Congrats, it took you {totalGuesses} guesses to get the correct number, which was {randomNumber}.")

