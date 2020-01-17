"""
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
"""
import datetime
try:
    # Ask for user input
    name = input("What is your name?\n")
    age = int(input("What is your age?\n"))
    numberOfCopies = int(input("How many times would you like this message to be showed?\n"))
    # Calculate the year of turning 100 
    currentYear = datetime.datetime.now().year
    yearsTillHundred = 100 - age
    yearOfTurningHundred = currentYear + yearsTillHundred
    # Print out the result an n amount of times.
    for i in range(numberOfCopies):
        print(f"Dear {name}, you will turn 100 in the year {yearOfTurningHundred}.")
except:
    pass

