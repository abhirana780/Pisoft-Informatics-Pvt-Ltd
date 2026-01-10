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
proceed = input("do you want to proceed : yes/no :")
if proceed=="yes":
    value3 = int(input("Enter a number: "))
    value4 = int(input("Enter another number: "))
    operation = input("Enter operation (+, -, *, /): ")
    if operation == '+':
        print(f"Result after addition: {result}")
    elif operation == '-':
        result = value3 - value4
        print(f"Result after subtraction: {result}")
    elif operation == '*':
        result = value3 * value4
        print(f"Result after multiplication: {result}")
    elif operation == '/':
        if value4 != 0:
            result = value3 / value4
            print(f"Result after division: {result}")
        else:
            print("Error: Division by zero is not allowed.")
elif proceed=="no":
    print("Thank you!")
    