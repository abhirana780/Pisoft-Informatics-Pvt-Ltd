#This programs loops the valus entered by the user
start_val = int(input("Enter the starting value: "))
end_val = int(input("Enter the ending value: "))
for i in range(start_val, end_val):
    if start_val and end_val >= 0 and start_val < end_val:
      print(i)
    else:
        print("Invalid input.")
    
