"""
Write a program (using functions!) that asks the user for a long string containing multiple words. 
Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

  My name is Michele
Then I would see the string:

  Michele is name My
shown back to me.
"""

def main():
    try:
        sentence = input("Enter a sentence.\n$ ")
        sentence_list = sentence.split()
        print(" ".join(sentence_list[::-1]))
    except:
        pass

if __name__ == "__main__":
    main()



