'''
Upper Lower
Pawelski
3/23/2023
Python II
'''

repeat = "y"
while repeat == "y" or repeat == "yes":
    word = input("Enter a word >> ")
    word_upper = word.upper()
    word_lower = word.lower()
    print("Original:", word)
    print("Upper case:", word_upper)
    print("Lower case:", word_lower)
    repeat = input("Would you like to enter another word? (y/n) >> ")
    print()
