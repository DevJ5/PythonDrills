"""
Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest)
and another number. 
The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.
"""

def main():
    try:
        numbers = input("Enter a list of number separated by a comma\n$ ")
        target_number = int(input("Enter a number you wish to find\n$ "))
        numbers_list = list(map(lambda n: int(n), numbers.split(",")))
        numbers_list.sort()
        
        found = False
        len(numbers_list)
        while True:


    except:
        pass
if __name__ == "__main__":
    main()
