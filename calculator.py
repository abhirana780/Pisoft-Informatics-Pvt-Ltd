print("Welcome to calculator!")
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print("Select operation -")
print("1. Add  2. Subtract 3. Multiply 4. Divide")
choice=int(input("Enter choice(1/2/3/4):"))
if choice==1:
    print(a,"+",b,"=",a+b) 
elif choice==2:
    print(a,"-",b,"=",a-b)
elif choice==3:
    print(a,"*",b,"=",a*b)
elif choice==4:
    print(a,"/",b,"=",a/b)
else:
    print("Invalid choice.")
user_input=input("You want to proceed enter yes to continue and no to exit:")
if user_input=='yes':
    c=int(input("Enter first number:"))
    d=int(input("Enter second number:"))
    print("Select operation -")
    print("1. Add  2. Subtract 3. Multiply 4. Divide")
    choice=int(input("Enter choice(1/2/3/4):")) 
    if choice==1:
        print(c,"+",d,"=",c+d) 
    elif choice==2:
        print(c,"-",d,"=",c-d)
    elif choice==3:
        print(c,"*",d,"=",c*d)
    elif choice==4:
        print(c,"/",d,"=",c/d)
    else:
        print("Invalid choice.")
elif user_input=='no':
    print("Exit from the calculator.")
else:
    print("Invalid input.")
user_input=input("You want to proceed enter yes to continue and no to exit:")
if user_input=='yes':   
    e=int(input("Enter first number:"))
    f=int(input("Enter second number:"))
    print("Select operation -")
    print("1. Add  2. Subtract 3. Multiply 4. Divide")
    choice=int(input("Enter choice(1/2/3/4):")) 
    if choice==1:
        print(e,"+",f,"=",e+f) 
    elif choice==2:
        print(e,"-",f,"=",e-f)
    elif choice==3:
        print(e,"*",f,"=",e*f)
    elif choice==4:
        print(e,"/",f,"=",e/f)
    else:
        print("Invalid choice.")
elif user_input=="no":
    print("Exit from the calculator.")
else:
    print("Invalid input.")
user_input=input("You want to proceed enter yes to continue and no to exit:")
if user_input=='yes':
    g=int(input("enter first number:"))
    h=int(input("enter second number:"))
    print("Select operation:")
    print("1.Add 2.Subtract 3. Multiply 4. divide")
    choice=int(input("Enter choice(1/2/3/4):"))
    if choice==1:
        print(g,"+",h,"=",g+h) 
    elif choice==2:
        print(g,"-",h,"=",g-h)
    elif choice==3:
        print(g,"*",h,"=",g*h)
    elif choice==4:
        print(g,"/",h,"=",g/h)
    else:
        print("Invalid choice.")
elif user_input=='no':
    print("Exit from the calculator.")
else:
    print("Invalid input.") 