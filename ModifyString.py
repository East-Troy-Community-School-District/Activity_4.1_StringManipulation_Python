'''
Modify String
Pawelski
11/6/2023
Introduction to Computer Science

Instructions:
Try running the program. It does not work!
You might be wondering why. Strings a immutable,
which is a fancy way of saying that they cannot
be changed after the fact. Now, you might be wondering,
what about this line of code...

word = "rush"

Replace the bad line of code with this line. The program
works! Why? This line of code works because you are
replace the string instead of trying to modify it.
'''

word = "rash"
word[1] = "u"
print(word)