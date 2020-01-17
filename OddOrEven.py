"""
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 
Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""
def main():
    while True:
        try:
            num = int(input("Enter a number\n"))
            check = int(input("Enter a number to divide by\n"))

            # Is the number dividable by 4
            if checkIsMultipyOfFour(num):
                print(f"{num} is dividable by four.")
                break

            # Does it divide evenly
            if checkDividesEvenly(num, check):
                print(f"{num} / {check} is an integer.")
            else:
                # Is the number even or odd
                print(f"{num} is even." if checkIsEven(num) else "{num} is odd.")

        except Exception as e:
            print(f"{e}")

def checkIsEven(number):
    return number % 2 == 0

def checkIsMultipyOfFour(number):
    return number % 4 == 0

def checkDividesEvenly(num, check):
    return number % check == 0

if __name__ == '__main__':
    main()
