'''
First Last Letter
Pawelski
3/23/2023
Python II
'''

repeat = "y"
while repeat == "y" or repeat == "yes":
    word = input("Enter a four letter word >> ").strip()
    print("First letter:", word[0])
    print("Last letter:", word[3])
    repeat = input("Would you like to enter another word? (y/n) >> ").lower()
    print()