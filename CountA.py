'''
Count A
Pawelski
11/6/2023
Introduction to Computer Science

Instructions:
Before running the program, make a prediction
to what it will do. Then run the program to
check your prediction. How does the loop execute?
How would you modify the program so that it counts
the number of t's in the string?
'''

count = 0
string = "data structures are fun to work with"

for character in string:
    if character == "a":
        count += 1

print("There are " + str(count) + " a's in the string.")