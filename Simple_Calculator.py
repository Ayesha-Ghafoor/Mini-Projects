# Simple Calculator

# Function to add multiple numbers using *args
def add(*args):
    return sum(args)

# Function to subtract two numbers
def subtract(a, b):
    return a - b

# Function to multiply multiple numbers using *args
def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

# Function to divide two numbers (with zero division check)
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

# Main program
print("Simple Calculator")
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter your choice (1-4): ")

if choice == '1':
    numbers = input("Enter numbers to add separated by space: ").split()
    numbers = [float(num) for num in numbers]
    print("Result:", add(*numbers))

elif choice == '2':
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result:", subtract(a, b))

elif choice == '3':
    numbers = input("Enter numbers to multiply separated by space: ").split()
    numbers = [float(num) for num in numbers]
    print("Result:", multiply(*numbers))

elif choice == '4':
    a = float(input("Enter numerator: "))
    b = float(input("Enter denominator: "))
    print("Result:", divide(a, b))

else:
    print("Invalid input. Please select a number between 1 and 4.")
