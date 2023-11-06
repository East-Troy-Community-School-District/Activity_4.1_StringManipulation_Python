'''
Name Length
Pawelski
11/6/2023
Introduction to Computer Science

Instructions:
Before running the program, trace it to determine
what it will do. Then run the program to check
your work. Why must the program subtract 1 from
the length of the string? Why MUST this program
use the len() function in order to work?
'''

name = input("Enter your full name (add a space between first and last name) >> ")
name_length = len(name) - 1
print("Your name is " + str(name_length) + " characters long.")