#welcome to sbi 
#enter choice credit/debit/bank balance
#credit limit 50000
#debit limit bank balance:10000

print("Welcome to SBI Bank")
bank_balance=10000
user_input=input("Do you want to credit, debit, check bank balance in your bank account or close your account (enter credit/debit/bank balance/close account): ")
if user_input=='credit':
  credit=int(input("Enter the amount of money you want to credit: "))
  if credit>50000:
      print("Credited amount is more than 50000, so it does not credit to your bank balance.")
  elif credit<=50000:
      bank_balance = bank_balance + credit
      print(f"{credit} credited successfully.")
  else:
        print("Invalid input.")
elif user_input=='debit':
    debit=int(input("Enter the amount of money you want to debit: "))
    if debit>bank_balance:
      print("Debit amount is more than your bank balance, so it does not debit from your bank balance.")
    elif debit<=bank_balance:
      bank_balance = bank_balance - debit
      print(f"{debit} debited from your account successfully.")
    else:
        print("Invalid input.")
elif user_input=='bank balance':
    print("Your current bank balance is: ", bank_balance)
elif user_input=='close account':
    print("To close your account, you need withdraw all your money first.")
    withdraw=(input("Do you want to withdraw all your money & close your account (enter yes/no): "))
    if withdraw=='yes':
        print(f"You have withdrawn all your money: {bank_balance}. Your account is now closed.")
        bank_balance=0
    elif withdraw=='no':
        print("Your account is not closed.")
else :
    print("Invalid input.")
proceed=input("Do you want to proceed? Enter yes to continue and no to exit: ")
if proceed=='yes':
    user_input=input("Do you want to credit, debit, check bank balance in your bank account or close your account (enter credit/debit/bank balance/close account): ")
    if user_input=='credit':
      credit=int(input("Enter the amount of money you want to credit: "))
      if credit>50000:
          print("Credited amount is more than 50000, so it does not credit to your bank balance.")
      elif credit<=50000:
          bank_balance = bank_balance + credit
          print(f"{credit} credited successfully.")
      else:
            print("Invalid input.")
    elif user_input=='debit':
        debit=int(input("Enter the amount of money you want to debit: "))
        if debit>bank_balance:
          print("Debit amount is more than your bank balance, so it does not debit from your bank balance.")
        elif debit<=bank_balance:
          bank_balance = bank_balance - debit
          print(f"{debit} debited from your account successfully.")
        else:
            print("Invalid input.")
    elif user_input=='bank balance':
        print("Your current bank balance is: ", bank_balance)
    elif user_input=='close account':
        print("To close your account, you need withdraw all your money first.")
        withdraw=(input("Do you want to withdraw all your money & close your account (enter yes/no): "))
        if withdraw=='yes':
            print(f"You have withdrawn all your money: {bank_balance}. Your account is now closed.")
            bank_balance=0
        elif withdraw=='no':
            print("Your account is not closed.")
    else :
        print("Invalid input.")