print("Welcome to the Basic Calculator!")
operation = input("Enter operation: \n For Addition press: + \n Subtraction press: -\n Multiplication press: *\n Division press: / \n Percentage press: % \n Your choice:  ")
value1 = int(input("Enter a number: "))
value2 = int(input("Enter another number: "))
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
elif operation == '%':
    if value2 != 0:
        result = float(value1)*100/float(value2)
        print(f"Result in percentage: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation.")
proceed = input("do you want to proceed : yes/no :")
if proceed=="yes":
    operation = input("Enter operation: \n For Addition press: + \n Subtraction press: -\n Multiplication press: *\n Division press: / \n Percentage press: % \n Your choice:  ")
    value3 = int(input("Enter a number: "))
    value4 = int(input("Enter another number: "))
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
    elif operation == '%':
        if value4 != 0:
            result = float(value3)*100/float(value4)
            print(f"Result in percentage: {result}")
        else:
            print("Error: Division by zero is not allowed.")
elif proceed=="no":
    print("Thank you!")
else: 
    print("Invalid input")
proceed2 = input("do you want to proceed : yes/no :")
if proceed2=="yes":
    operation = input("Enter operation: \n For Addition press: + \n Subtraction press: -\n Multiplication press: *\n Division press: / \n Percentage press: % \n Your choice:  ")
    value5 = int(input("Enter a number: "))
    value6 = int(input("Enter another number: "))
    if operation == '+':
        result = value5 + value6
        print(f"Result after addition: {result}")
    elif operation == '-':
        result = value5 - value6
        print(f"Result after subtraction: {result}")
    elif operation == '*':
        result = value5 * value6
        print(f"Result after multiplication: {result}")
    elif operation == '/':
        if value6 != 0:
            result = value5 / value6
            print(f"Result after division: {result}")
    elif operation == '%':
        if value6 != 0:
            result = float(value5)*100/float(value6)
            print(f"Result in percentage: {result}")
        else:
            print("Error: Division by zero is not allowed.")
elif proceed2=="no":
    print("Thank you!")
else:
    print("Invalid input.") 
proceed3 = input("do you want to proceed : yes/no :")
if proceed3=="yes":
    operation = input("Enter operation: \n For Addition press: + \n Subtraction press: -\n Multiplication press: *\n Division press: / \n Percentage press: % \n Your choice:  ")
    value7 = int(input("Enter a number: "))
    value8 = int(input("Enter another number: "))
    if operation == '+':
        result = value7 + value8
        print(f"Result after addition: {result}")
    elif operation == '-':
        result = value7 - value8
        print(f"Result after subtraction: {result}")
    elif operation == '*':
        result = value7 * value8
        print(f"Result after multiplication: {result}")
    elif operation == '/':
        if value8 != 0:
            result = value7 / value8
            print(f"Result after division: {result}")
    elif operation == '%':
        if value8 != 0:
            result = float(value7)*100/float(value8)
            print(f"Result in percentage: {result}")
        else:
            print("Error: Division by zero is not allowed.")
elif proceed3=="no":
    print("Thank you!")
else:
    print("Invalid input.")
proceed4 = input("do you want to proceed : yes/no :")
if proceed4=="yes":
    operation = input("Enter operation: \n For Addition press: + \n Subtraction press: -\n Multiplication press: *\n Division press: / \n Percentage press: % \n Your choice:  ")
    value9 = int(input("Enter a number: "))
    value10 = int(input("Enter another number: "))
    if operation == '+':
        result = value9 + value10
        print(f"Result after addition: {result}")
    elif operation == '-':
        result = value9 - value10
        print(f"Result after subtraction: {result}")
    elif operation == '*':
        result = value9 * value10
        print(f"Result after multiplication: {result}")
    elif operation == '/':
        if value10 != 0:
            result = value9 / value10
            print(f"Result after division: {result}")
    elif operation == '%':
        if value10 != 0:
            result = float(value9)*100/float(value10)
            print(f"Result in percentage: {result}")
        else:
            print("Error: Division by zero is not allowed.")
elif proceed4=="no":
    print("Thank you!")
else:
    print("Invalid input")