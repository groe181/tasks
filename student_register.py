
number_of_students = int(input("How many students are taking the exam? "))

with open('reg_form.txt', 'w') as f:
    for student in range(number_of_students):
        f.write("#" + input("Student number: ") + " _______________" + "\n")


# student_numbers = []

# for student in range(number_of_students):
#     student_numbers.append(input("Student number: "))

# with open('reg_form.txt', 'w') as f:
#     for index, student in enumerate(student_numbers):
#         f.write("#" + student + " _______________" + "\n")
