"""
Create a program that will play the “cows and bulls” game with the user. The game works like this:

Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. 
For every digit that the user guessed correctly in the correct place, they have a “cow”. 
For every digit the user guessed correctly in the wrong place is a “bull.”
Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
Once the user guesses the correct number, the game is over. 
Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.
"""
import random

def main():
    try:
        while True:
            random_int = str(rand.randint(1000, 9999))
            print(random_int)
            guess = input("Enter a 4-digit number\n$ ")
            cows = 0
            bulls = 0
            for n, i in enumerate(random_int):
                if guess[i] == n:
                    cows += 1
                else:
                    bulls += 1
            print(f"{cows} cows, {bulls} bulls")
            if cows == 4:
                break

    except Exception:
        pass

    
if __name__ == "__main__":
    main()
