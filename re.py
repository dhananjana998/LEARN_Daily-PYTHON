s_num = 1
present = 0
absence = 0

try:
    Total_Student = int(input("Enter total number of students in class: "))

    while s_num <= Total_Student:
        In_class = input(f"Is student {s_num} in class (yes=1 / no=0): ")

        if In_class == "1":
            print(f"{s_num}: 1")
            present += 1
        else:
            print(f"{s_num}: 0")
            absence += 1

        s_num += 1

    print(f"present: {present}, absence: {absence}")

except EOFError:
    print("Error: No more input available. Please provide all required inputs.")
    # You might want to exit here or handle it differently
except ValueError:
    print("Invalid input. Please enter a valid number for total students or 1/0 for presence.")



    '''Enter total number of students in class: 5
Is student 1 in class (yes=1 / no=0): 0
1: 0
Is student 2 in class (yes=1 / no=0): 1
2: 1
Is student 3 in class (yes=1 / no=0): 0
3: 0
Is student 4 in class (yes=1 / no=0): 1
4: 1
Is student 5 in class (yes=1 / no=0): 1
5: 1
present: 3, absence: 2'''