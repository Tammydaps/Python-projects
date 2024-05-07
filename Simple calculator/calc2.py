# Simple Calculator
'''
After running the first version of the calculator, let us enhance our 
program by incorporating conditional statements to handle different operations based on user input.
'''
# main function to run the enhanced version of our calculator
def enhanced_calc():
    print("Enhanced Calculator Program") 
    # Get user input for numbers
    num_1 = float(input("Kindly Enter the first number: "))
    num_2 = float(input("Kindly Enter the second number: "))

    # Get user input for operation
    operation = input("Choose desired operation (+, -, *, /): ")

    # Perform the selected operation using conditional statements
    if operation in ['+', '-', '*', '/']:
        result = calculate(num_1,num_2, operation)
    else:
        result = "Invalid operation"
    # Display the result
    print(f"Result: {result}")

# Function to add two numbers
def add(x,y):
    return x + y

# Function to subtract two numbers
def subtract(x,y):
    return x - y

# Function to multiply two numbers
def multiply(x,y):
    return x * y

# Funtion to divide two numbers 
def divide(x,y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero"
# Function to handle different operations using conditional statements
def calculate(x,y, op):
    if op == '+':
        return add(x,y)
    elif op == '-':
        return subtract(x,y)
    elif op == '*':
        return multiply(x,y)
    elif op == '/':
        return divide(x,y)   
# Call the enhanced_calculator function
enhanced_calc()