"""
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
and makes a new list of only the first and last elements of the given list. 
For practice, write this code inside a function.
"""

a = [5, 10, 15, 20, 25]

def getFirstAndLast(listOfNumbers):
    firstAndLast = []
    firstAndLast.append(listOfNumbers.pop(0))
    firstAndLast.append(listOfNumbers.pop(len(listOfNumbers) - 1))
    return firstAndLast

print(getFirstAndLast(a))
