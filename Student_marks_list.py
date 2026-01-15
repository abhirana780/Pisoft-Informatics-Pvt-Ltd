#taking input of marks
#total 5 subs
#calculating percentage
#displaying result
#ranking students based on percentage
num = int(input("Enter number of students: "))
s_list = []
for i in range(num):
    print("Student ", i+1)
    s_name = input("Enter your name: ")
    math = int(input("Enter marks obtained in Mathematics: "))
    science = int(input("Enter marks obtained in Science: "))
    english = int(input("Enter marks obtained in English: "))
    history = int(input("Enter marks obtained in History: "))
    geography = int(input("Enter marks obtained in Geography: "))
    total_marks = math + science + english + history + geography
    maximum_marks = 500
    percentage = (total_marks / maximum_marks) * 100
    if percentage >= 90:
        grade = 'A'
    elif percentage >= 80:
        grade = 'B'
    elif percentage >= 70:
        grade = 'C'
    elif percentage >= 60:
        grade = 'D'
    elif percentage >= 50:
        grade = 'E'
    elif percentage < 50:
        grade = 'F'
    else:
        grade = 'invalid entry'
    s_list.append((s_name, percentage))
    print("\nStudent Name:", s_name)
    print("Total Marks Obtained:", total_marks, "out of", maximum_marks)
    print(f"Percentage: {percentage}% ")
    print("Grade:", grade)
    print("-------------------------------")
    print("\n")
print("Ranking of Students based on Percentage:")
