s_num = 1
present = 0  
absence = 0

Total_Student = int(input("Enter Total number student in class: ")) 

while s_num <= Total_Student:
    In_class = input(f"Is student {s_num} in class (yes=1/no=0): ")
    
    
    if In_class == "1":
        print(f"{s_num}: 1 (Present)")
        present += 1 
    else:
        print(f"{s_num}: 0 (Absent)")
        absence += 1 
    
    s_num += 1

print(f"present : {present}, absence: {absence}") 

''' Enter total number of students in class: 5
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
present: 3, absence: 2

Process finished with exit code 0'''
