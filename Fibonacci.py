"""
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
Take this opportunity to think about how you can use functions. 
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence 
is the sum of the previous two numbers in the sequence. 
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""

try:
    amount = int(input("How many Fibonacci numbers do you want?\n$ "))

    if amount <= 0:
        print("Enter a positive integer.")

    numbers = []
    if amount == 1:
        numbers.append(1)
    elif amount == 2:
        numbers.extend([1,1])
    else:
        numbers = [1,1]
        i = 2

        while len(numbers) != amount:
            next_number = numbers[i - 2] + numbers[i - 1]
            numbers.append(next_number)
            i += 1

    print(numbers)

except:
    print("Thats not a valid amount.")

