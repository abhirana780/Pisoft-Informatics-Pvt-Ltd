value1 = int(input("Enter a number: "))
value2 = int(input("Enter another number: "))
operation = input("Enter operation (+, -, *, /): ")
if operation == '+':
    result = value1 + value2
    print(f"Result after addition: {result}")
elif operation == '-':
    result = value1 - value2
    print(f"Result after subtraction: {result}")
elif operation == '*':
    result = value1 * value2
    print(f"Result after multiplication: {result}")
elif operation == '/':
    if value2 != 0:
        result = value1 / value2
        print(f"Result after division: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter a valid operation (+, -, *, /).")