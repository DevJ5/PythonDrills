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

    isDiscreteMathLover = True if input("Do you like discrete math? [n, Y]\n").lower().strip() == 'y' else False
    
    while True:
        number = getInput("Enter a number or type 'q' to return a list of non duplicates\n")
        if number == 'q':
            break
        elif isDiscreteMathLover:
            list.append(int(number))
        else:
            if checkNoDuplicate(lookup, number):
                addToList(list, number)
                lookup[number] = 1

    if isDiscreteMathLover: print(set(list))
    else: print(list)

def getInput(message):
    return input(message)

def checkNoDuplicate(lookup, number):
    return lookup.get(number) == None

def addToList(list, number):
    list.append(int(number))

if __name__ == "__main__":
    main()
