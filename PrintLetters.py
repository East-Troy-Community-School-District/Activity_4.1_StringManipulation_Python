'''
Print Letters
Pawelski
11/6/2023
Introduction to Computer Science

Instructions:
Before running the program, trace it to determine
what it will do. Then run the program to check
your work. Why does the loop start at 0? Why does
the loop stop at 9 (while it says 10, the loop
does not get to 10)? What is the connection
between 10 and the length of the string?
Change word to "short". When you run the program, it
throws an error. Why? How could we fix this problem?
Change word to "supercalifragilisticexpialidocious". The
program no longer prints the whole word! Why?
How could we fix this problem permentantly?
'''

word = "traversing"
for i in range(0, 10):
    print(word[i])