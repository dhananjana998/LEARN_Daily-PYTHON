"""This program checks student marks and tells whether they Pass or Fail using a lambda function."""
#student marks
students = {
    "sachi":87,
    "mano":67,
    "sala":76,
    "Amal":25}

#lambda function
check_result=lambda marks:"pass" if marks>=40 else "fail"

for name,marks in students.items():
    print(f"{name}:{marks} - {check_result(marks)}")

"""
Output:
sachi:87 - pass
mano:67 - pass
sala:76 - pass
Amal:25 - fail

"""
