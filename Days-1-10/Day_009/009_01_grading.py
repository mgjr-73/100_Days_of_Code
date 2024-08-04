# Instructions
# You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the
# names of the students and the values are their exam scores.
#
# Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary
# called student_grades that should contain student names for keys and their grades for values.
#
# This is the scoring criteria:
# Scores 91 - 100: Grade = "Outstanding"
# Scores 81 - 90: Grade = "Exceeds Expectations"
# Scores 71 - 80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"
#
# Expected Output
# '{'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}'

# Hint
# - Remember that looping through a Dictionary will only give you the keys and not the values.
# - If in doubt as to why your code is not doing what you expected, you can always print out the intermediate values.
# - At the end of your program, the print statement will show the final student_scores dictionary, do not change this.

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for key in student_scores:
    if student_scores[key] >= 91:
        student_grades[key] = "Outstanding"
    elif student_scores[key] >=81:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] >= 71:
        student_grades[key] = "Acceptable"
    elif student_scores[key] < 71:
        student_grades[key] = "Fail"

print(student_grades)

#################
# Instructor Code
#################
# for student in student_scores:
#   score = student_scores[student]
#   if score > 90:
#     student_grades[student] = "Outstanding"
#   elif score > 80:
#     student_grades[student] = "Exceeds Expectations"
#   elif score > 70:
#     student_grades[student] = "Acceptable"
#   else:
#     student_grades[student] = "Fail"