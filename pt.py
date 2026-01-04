import pandas as pd

# Load CSV file
df = pd.read_csv("students.csv")

# Calculate total and average
df["Total"] = df[["Maths", "Science", "English"]].sum(axis=1)
df["Average"] = df["Total"] / 3

# Grade function
def grade(avg):
    if avg >= 75:
        return "A"
    elif avg >= 50:
        return "B"
    elif avg >= 35:
        return "C"
    else:
        return "F"

# Addgrade
df["Grade"] = df["Average"].apply(grade)

# Top student
top_student = df.loc[df["Total"].idxmax()]
print("Top Student:")
print(top_student)

# Failed students
failed_students = df[df["Grade"] == "F"]
print("\nFailed Students:")
print(failed_students)

# Save report
df.to_csv("student_report.csv", index=False)

print("\nReport saved as student_report.csv")
