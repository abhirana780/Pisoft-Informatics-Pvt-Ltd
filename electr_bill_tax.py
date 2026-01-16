#per unit price under 100 is 5 for household, 3.5 for commercial and 2 ffor industrial
#per unit price between 100 and 200 is 7 for household, 5.5 for commercial and 4 for industrial
#per unit price above 200 is 10  for household, 8 for commercial and 6 for industrial
for i in range(10):
    unit_price = 0
    user_type = input("Enter the type of user (household/commercial/industrial): ")
    unit_used = int(input("Enter the number of units used: "))
    if user_type == "commercial":
        if unit_used <= 100:
            unit_price = 3.5
            total_bill = unit_used * unit_price
            print(f"Your total electricity bill is: Rs.{total_bill}")
        elif unit_used <= 200:
            unit_price = 5.5
            total_bill = unit_used * unit_price
            print(f"Your total electricity bill is: Rs.{total_bill}")
        elif unit_used > 200:
            unit_price = 8
            total_bill = unit_used * unit_price
            print(f"Your total electricity bill is: Rs.{total_bill}")
        else:
            print("Invalid input.")
    elif user_type == "industrial":
        if unit_used <= 100:
            unit_price = 2
            total_bill = unit_used * unit_price
            print(f"Your total electricity bill is: Rs.{total_bill}")
        elif unit_used <= 200:
            unit_price = 4
            total_bill = unit_used * unit_price
            print(f"Your total electricity bill is: Rs.{total_bill}")
        elif unit_used > 200:
            unit_price = 6
            total_bill = unit_used * unit_price
            print(f"Your total electricity bill is: Rs.{total_bill}")
        else:
            print("Invalid input.")
    elif user_type == "household":
        if unit_used <= 100:
            unit_price = 5
            total_bill = unit_used * unit_price
            print(f"Your total electricity bill is: Rs.{total_bill}")
        elif unit_used <= 200:
            unit_price = 7
            total_bill = unit_used * unit_price
            print(f"Your total electricity bill is: Rs.{total_bill}")
        elif unit_used > 200:
            unit_price = 10
            total_bill = unit_used * unit_price
            print(f"Your total electricity bill is: Rs.{total_bill}")
        else:
            print("Invalid input.")
    else:
        print("Invalid input.")
    proceed = input("Do you want to calculate again? (yes/no): ")
    if proceed == 'yes':
        continue
    else:
        print("Thank you for using the electricity bill calculator.")
        break