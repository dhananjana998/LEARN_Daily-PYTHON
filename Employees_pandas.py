import pandas as pd

#  Read CSV
df = pd.read_csv("employees.csv")

print("=== All Employee Data ===")
print(df)

#  Calculate Total Salary (Basic + Allowances + Bonus)
df["TotalSalary"] = df["BasicSalary"] + df["Allowances"] + df["Bonus"]

#  Calculate Annual Salary
df["AnnualSalary"] = df["TotalSalary"] * 12

print("\n=== After Adding Salary Columns ===")
print(df)

# Show employees earning above 60,000 per month
high_salary = df[df["TotalSalary"] > 60000]
print("\n=== Employees earning > 60,000 ===")
print(high_salary)

#  Sort employees by total salary
sorted_df = df.sort_values("TotalSalary", ascending=False)
print("\n=== Employees Sorted by Salary (High → Low) ===")
print(sorted_df)

#  Group by department (average salary)
dept_salary = df.groupby("Department")["TotalSalary"].mean()
print("\n=== Average Salary by Department ===")
print(dept_salary)

#  Save final output
df.to_csv("salary_results.csv", index=False)
print("\nsalary_results.csv saved successfully!")
