print("===== Student Management System =====")

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

maths = float(input("Enter Maths marks: "))
science = float(input("Enter Science marks: "))
english = float(input("Enter English marks: "))

total = maths + science + english
percentage = total / 3

print("\n===== Student Result =====")
print("Name:", name)
print("Roll No:", roll_no)
print("Total Marks:", total)
print("Percentage:", percentage)

if percentage >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")