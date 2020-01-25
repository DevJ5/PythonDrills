"""
Ask the user for a number and determine whether the number is prime or not. 
(For those who have forgotten, a prime number is a number that has no divisors.). 
You can (and should!) use your answer to Exercise 4 to help you. 
Take this opportunity to practice using functions, described below.
"""

def getNumber(helptext = "Enter a number\n$ "):
    return int(input(helptext))

def checkIsPrime(number):
    if number == 1:
        isPrime = False

    isPrime = True
    divisor = 2
    
    while divisor != number:
       if number % divisor == 0:
           isPrime = False
           break
       divisor += 1

    return isPrime

def main():
    number = getNumber()
    print(checkIsPrime(number))

if __name__ == "__main__":
    main()

