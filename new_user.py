u_name = input("Enter your name: ")
u_age = int(input("Enter your age: ") )
age= u_age>18
u_designation = input("Enter your designation: ")
u_experience = int(input("Enter your years of experience: "))   
if u_experience > 2 and age:
    print(f"Hello {u_name}, you are eligible for the senior position as you have {u_experience} years of experience.")
elif u_experience<2 and age:
    print(f"Hello {u_name}, you are eligible for the junior position as you have {u_experience} years of experience.")
else: 
    print(f"One of the values entered are not in correct format or your age is less than 18")

print("hi")
u_name = input("Enter your name: ")
u_age = int(input("Enter your age: ") )
age= u_age>18
u_designation = input("Enter your designation: ")
u_experience = int(input("Enter your years of experience: "))   
if u_experience > 2 and age:
    print(f"Hello {u_name}, you are eligible for the senior position as you have {u_experience} years of experience.")
elif u_experience<2 and age:
    print(f"Hello {u_name}, you are eligible for the junior position as you have {u_experience} years of experience.")
else: 
    print(f"One of the values entered are not in correct format or your age is less than 18")

