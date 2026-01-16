#less than 25000 salary no tax
#25000 to 50000 5% tax
#50000 to 100000 10% tax
#above 100000 15% tax
#cal tatal tax payed and in-hand salary

for i in range(100):
    user_id = input("Enter your user ID: ")
    salary = int(input("Enter your monthly salary: "))
    a_salary = salary*12
    if salary < 25000:
        tax_rate = 0
    elif 25000 <= salary <= 50000:
        tax_rate = 0.05
    elif 50000 < salary <= 100000:
        tax_rate = 0.10
    else:
        tax_rate = 0.15 
    tax_amount = salary * tax_rate
    in_hand_salary = salary - tax_amount
    print("User ID:", user_id)
    print("Monthly Salary:", salary)
    print("Tax Rate:", tax_rate * 100, "%")
    print("Tax Amount:", tax_amount)
    print("In-hand Salary:", in_hand_salary)
    print(f"Your annual salary is {a_salary} and tax paid is {tax_amount*12} annually.")
    proceed = input("Do you want to calculate again? (yes/no): ")
    if proceed == 'yes':
        continue
    else:
        print("Thank you for using the salary tax calculator.")
        break
