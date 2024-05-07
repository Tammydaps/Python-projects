# Simple Calculator Program
'''
This is a simple calculator that includes functions for each arithmetic operation
and a main function (calculator()) that takes user input and performs the selected operation.
'''
# Function to perform Addition
def add(x,y):
    return x + y

# Function to perform subtraction
def subtract(x,y):
    return x - y

# Function to perform multiplication
def multiply(x,y):
    return x * y

# Function to perform division
def divide(x,y):
    if y!=0:
        return x/y
    else:
        return "cannot divide by zero"
    
 # Main function to run the calculator
def calculator():
    print("This is a simple calculator program")

# Get user input for numbers
num_1 = float(input("kindly enter the first number: "))
num_2 = float(input("kindly input the second number: "))

# Get user input for operation
operation = input("choose your operation (+, -, *, /): ")

# Let us perform the selected operation
if operation == '+':
    result = add(num_1,num_2)
elif operation =='-':
    result = subtract(num_1,num_2)
elif operation == '*':
    result = multiply(num_1,num_2)
elif operation == '/':
    result = divide(num_1,num_2)
else:
    result = "Invalid operation"

# Display the result
print(f"Your Result is: {result}")

# Run our calculator
calculator()