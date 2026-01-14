bank_balance=10000
user_input=input("Are you want to credit or debit or check bank balance in your bank account (enter credit/debit/bank balance):")
if user_input=='credit':
  credit=int(input("Enter the amount of money you want to credit:"))
  if credit>50000:
      print("credited amount is more than 50000, so it does no credit to your bank balance.")
  elif credit<=50000:
      bank_balance+=credit
      print("Your updated bank balance after credit is :",bank_balance)
  else:
        print("Invalid input.")
elif user_input=='debit':
    debit=int(input("Enter the amount of money you want to debit:"))
    if debit>bank_balance:
      print("debit amount is more than your bank balance, so it does no debit to your bank balance.")
    elif debit<=bank_balance:
      bank_balance-=debit
      print("Your updated bank balance after debit is :",bank_balance)
    else:
        print("Invalid input.")
elif user_input=='bank balance':
    print("Your current bank balance is :",bank_balance)
else :
    print("Invalid input.")
user_input=input("You want to proceed enter yes to continue and no to exit:")
if user_input=='yes':
    user_input=input("Are you want to credit or debit or check bank balance in your bank account (enter credit/debit/bank balance):")
    if user_input=='credit':
      credit=int(input("Enter the amount of money you want to credit:"))
      if credit>50000:
          print("credited amount is more than 50000, so it does no credit to your bank balance.")
      elif credit<=50000:
          bank_balance+=credit
          print("Your updated bank balance after credit is :",bank_balance)
      else:
            print("Invalid input.")
    elif user_input=='debit':
        debit=int(input("Enter the amount of money you want to debit:"))
        if debit>bank_balance:
          print("debit amount is more than your bank balance, so it does no debit to your bank balance.")
        elif debit<=bank_balance:
          bank_balance-=debit
          print("Your updated bank balance after debit is :",bank_balance)
        else:
            print("Invalid input.")
    elif user_input=='bank balance':
        print("Your current bank balance is :",bank_balance)
    else :
        print("Invalid input.")


