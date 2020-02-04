"""
Write a program (function!) that takes a list and returns a new list that contains 
all the elements of the first list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing a list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a different function.
"""

def main():
    list = []
    lookup = {}

    while True:
        input = getInput("Enter a number or type 'q' to return a list of non duplicates\n")
        if input == 'q':
            break
        if checkNoDuplicate(lookup, input):
            addToList(list, input)
            lookup[input] = 1

    print(list)

def getInput(message):
    return input(message)

def checkNoDuplicate(lookup, input):
    return lookup.get(input) == None

def addToList(list, item):
    list.append(int(item))

if __name__ == "__main__":
    main()
