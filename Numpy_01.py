import numpy as np

marks = np.array([
    [78, 90, 90],
    [63, 71, 66],
    [89, 67, 95],
    [54, 69, 60],
    [91, 84, 87]
])

# Total and average marks of each student
total_marks = np.sum(marks, axis=1)
average_marks = np.mean(marks, axis=1)

# Print student-wise marks
for i in range(len(marks)):
    print(f"Student {i+1}: Total = {total_marks[i]}, Average = {round(average_marks[i], 2)}")

# Average marks of each subject
average_subject = np.mean(marks, axis=0)
print("\nAverage marks of each subject:")
print(f"Math    : {round(average_subject[0], 2)}")
print(f"Science : {round(average_subject[1], 2)}")
print(f"English : {round(average_subject[2], 2)}")

"""
Output:

Student 1: Total = 258, Average = 86.0
Student 2: Total = 200, Average = 66.67
Student 3: Total = 251, Average = 83.67
Student 4: Total = 183, Average = 61.0
Student 5: Total = 262, Average = 87.33

Average marks of each subject:
Math    : 75.0
Science : 76.2
English : 79.6

"""
