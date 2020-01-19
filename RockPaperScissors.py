"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message 
of congratulations to the winner, and ask if the players want to start a new game)
"""

def main():
    newGame = True
    score = [0,0]

    while True:
        prompt = """
            [1]:Rock
            [2]:Paper
            [3]:Scissors
            $ """

        if newGame: 
            print("Welcome to this game of rock, paper, scissors. Good luck!")
            score = [0, 0]

        try:
            playerOne = int(input(f"Player one: {prompt}"))
            playerTwo = int(input(f"Player two: {prompt}"))
        except ValueError:
            print("Enter a valid option between 1 and 3")

        newGame = False

        if playerOne == playerTwo:
            printRoundWinner(None)
        elif playerOne == 1 and playerTwo == 2:
            score[1] += 1
            printRoundWinner(2)
        elif playerOne == 1 and playerTwo == 3:
            score[0] += 1
            printRoundWinner(1)
        elif playerOne == 2 and playerTwo == 1:
            score[0] += 1
            printRoundWinner(1)
        elif playerOne == 2 and playerTwo == 3:
            score[1] += 1
            printRoundWinner(2)
        elif playerOne == 3 and playerTwo == 1:
            score[1] += 1
            printRoundWinner(2)
        elif playerOne == 3 and playerTwo == 2:
            score[0] += 1
            printRoundWinner(1)

        isWinner = checkIsWinner(score)
        if isWinner:
            print(f"Player {isWinner} wins the game.\n")
            keepPlaying = False
            while True:
                endOfGameOption = input("[1]: Play again\n[x]: Quit\n$ ")
                if endOfGameOption == '1':
                    keepPlaying = True
                    break
                elif endOfGameOption == 'x':
                    keepPlaying = False
                    break
                else:
                    continue

            if not keepPlaying: break
            newGame = True
        else:
            print("Next round.")

def printRoundWinner(player):
    if player == 1: print("Player 1 has won the round.")
    elif player == 2: print("Player 2 has won the round.")
    else: print("Its a tie.")

def checkIsWinner(score):
    print(f"Score: {score}")
    if score[0] == 2: return 1
    elif score[1] == 2: return 2
    else: return None

if __name__ == '__main__':
    main()





