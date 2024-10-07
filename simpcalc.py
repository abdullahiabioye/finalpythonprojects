try:
    # Ask the user to input two numbers
    Number1 = float(input("Enter the first number: "))
    Number2 = float(input("Enter the second number: "))
except ValueError:
    print("Invalid input. Please enter numeric values.")
    exit()

operator = input("Enter the operator (+, -, *, /): ")

if operator == '+':
    result = Number1 + Number2
    print("The Result is ", result)

elif operator == '-':
    result = Number1 - Number2
    print("The Result is ", result)

elif operator == '*':
    result = Number1 * Number2
    print("The Result is ", result)

elif operator == '/':
    try:
        # Check for division by zero
        result = Number1 / Number2
        print("The Result is ", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

else:
    print("Invalid operator. Please use one of the following: +, -, *, /")
