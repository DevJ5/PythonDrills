'''
Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)
'''
try:
    str = input("Enter a string\n")
    strList = list(str)
    strList.reverse()

    print("A palindrome.") if str == "".join(strList) else print("Not a palindrome.")
except:
    pass
