'''
Lower Repeat
Pawelski
11/6/2023
Introduction to Computer Science

Instructions:
Run the program and consider the following questions...
1. What does this program do?
2. What values can you enter to have the
   program say "Hello!" again?
3. How would you modify the program so that it would
   accept "yes", "YES", "Yes", "YEs". YeS", "yES", or
   "yeS" to have the loop repeat?
4. Previously, we use the or operator to check for each
   string that would cause the loop to repeat. Why is
   using the lower() method easier?
'''

repeat = "y"
while repeat == "y":
    print("Hello!")
    repeat = input("Say hello again? (y/n) >> ").lower()