print("Welcome to the SBI Bank")
a = 2000000000000
choice = input("Enter your choice to proceed (1 for credit/2 for debit/3 for check balance): ")
if choice == '1':
    print("welcome to the credit section")
    credit_amount = int(input("Enter the amount to be credited: "))
    if credit_amount<50000:
        a += credit_amount
        print(f"Your new balance is: {a}")
        print("your transaction is completed successfully")
    else:
        print("Invalid input")

elif choice == '2':
    print("welcome to the debit section")
    if a>=500:
        debit_amount = int(input("Enter the amount to be debited: "))
        a -= debit_amount
        print(f"Your new balance is: {a}")
        print("your transaction is completed successfully")
    elif a<10000:
        print("your have insufficient balance")

elif choice == '3':
    print(f"Your balance: {a}")
    
else:
    print("Invalid input")

print("Thank you for using the SBI Bank")