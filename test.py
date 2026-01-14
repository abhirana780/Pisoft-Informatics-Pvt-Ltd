# user = int(input("Enter range:"))
# for i in range(user):
#     print("hii")
    
    
times = int(input("How many times do you want to calculate? "))
for i in range(times):
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("1. Add\n2. Multiply\n3. Subtract\n4. Divide")
    select_choice = int(input("Enter your choice: "))
    if select_choice == 1:
        print(f"{a} + {b} = {a + b}")
    elif select_choice == 2:
        print(f"{a} X {b} = {a * b}")
    elif select_choice == 3:
        if a >= b:
             print(f"{a} - {b} = {a - b}")
        else:
            print(f"{a} - {b} = {b - a}".lstrip(1))
    elif select_choice == 4:
        if b != 0:
            print(f"{a} / {b} = {a / b}")
        else:
            print("Division by zero not allowed")
    else:
        print("Wrong choice")
    print("--------------------")