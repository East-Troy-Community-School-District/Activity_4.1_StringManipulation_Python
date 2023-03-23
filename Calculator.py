'''
Calculator
Pawelski
3/23/2023
Python II
'''

def calculation(operation, num1, num2):
    '''
    Performs the desired calculation, if possible.
    '''
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/" and num2 != 0:
        return num1 / num2
    return "error"

repeat = "y"
while repeat == "y" or repeat == "yes":
    number1 = float(input("Enter the first operand >> "))
    operation = input("Enter the operation >> ")
    number2 = float(input("Enter the second operand >> "))
    print(number1, operation, number2, "=", calculation(operation, number1, number2))
    repeat = input("Would you like to perform another calculation? (y/n) >> ").lower()
    print()
    