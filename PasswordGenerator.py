"""
Write a password generator in Python. Be creative with how you generate passwords - 
strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
The passwords should be random, generating a new password every time the user asks for a new password. 
Include your run-time code in a main method.

Extra:

Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
"""

import random
import string

def main():
    password_length = int(input("How long do you want your password to be?\n$ "))
    characters = string.ascii_letters + string.digits + string.punctuation
    password = []

    for i in range(password_length):
        char = characters[random.randint(0, len(characters))]
        password.append(str(char))
    
    print(f"You're new password is: {''.join(password)}")

if __name__ == "__main__":
    main()
