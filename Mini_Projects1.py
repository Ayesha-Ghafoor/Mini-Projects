# Student Marks Manager

# Dictionary to store student names and their marks
students = {}

# Function to calculate grade based on average marks
def calculate_grade(avg):
    if avg >= 90:
        return 'A+'
    elif avg >= 80:
        return 'A'
    elif avg >= 70:
        return 'B'
    elif avg >= 60:
        return 'C'
    elif avg >= 50:
        return 'D'
    else:
        return 'F'

# Input number of students
num = int(input("Enter the number of students: "))

# Input names and marks using loop
for i in range(num):
    name = input(f"\nEnter name of student {i+1}: ")
    marks = []
    for j in range(3):  # Assuming 3 subjects
        mark = float(input(f"Enter marks for subject {j+1}: "))
        marks.append(mark)
    students[name] = marks

# Display student data with average and grade
print("\n---- Student Report ----")
for name, marks in students.items():
    avg = sum(marks) / len(marks)
    grade = calculate_grade(avg)
    print(f"\nName: {name}")
    print(f"Marks: {marks}")
    print(f"Average: {avg:.2f}")
    print(f"Grade: {grade}")
