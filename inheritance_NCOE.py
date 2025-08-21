# Define the base class for All National College members
class CollegeMember:
    # Constructor - called automatically when creating a new member
    def __init__(self, name, age, phone, gender):  # initialize the member's basic information
        self.name = name  # store the member's name
        self.age = age  # store the member's age
        self.phone = phone  # store the member's phone
        self.gender = gender  # store the member's gender

    # Method to display the member information
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Phone-Number: {self.phone}, Gender: {self.gender}")


# TeacherTrainers class inherits from CollegeMember
class TeacherTrainers(CollegeMember):
    # Constructor for TeacherTrainers with additional trainers_id parameter
    def __init__(self, name, age, phone, gender, trainers_id):
        # Call the parent class constructor
        super().__init__(name, age, phone, gender)
        # Set the specific information of TeacherTrainers
        self.trainers_id = trainers_id

    # Override display to show specific information of TeacherTrainers
    def display(self):
        print(
            f"Teacher Trainer - Name: {self.name}, Age: {self.age}, Phone-Number: {self.phone}, Gender: {self.gender}, ID: {self.trainers_id}")


# Lecturer class inherits from CollegeMember
class Lecturer(CollegeMember):
    # Constructor for Lecturer with additional lecturer_id parameter
    def __init__(self, name, age, phone, gender, lecturer_id, subject):
        # Call the parent class constructor
        super().__init__(name, age, phone, gender)
        # Set the specific information of Lecturer
        self.lecturer_id = lecturer_id
        self.subject = subject

    # Override display to show specific information of Lecturer
    def display(self):
        print(
            f"Lecturer - Name: {self.name}, Age: {self.age}, Phone-Number: {self.phone}, Gender: {self.gender}, ID: {self.lecturer_id}, Subject: {self.subject}")


# AcademicStaff class inherits from CollegeMember
class AcademicStaff(CollegeMember):
    # Constructor for AcademicStaff with additional academicStaff_id parameter
    def __init__(self, name, age, phone, gender, academicStaff_id, workHours):
        # Call the parent class constructor
        super().__init__(name, age, phone, gender)
        # Set the specific information of AcademicStaff
        self.academicStaff_id = academicStaff_id
        self.workHours = workHours

    # Override display to show specific information of AcademicStaff
    def display(self):
        print(
            f"Academic Staff - Name: {self.name}, Age: {self.age}, Phone-Number: {self.phone}, Gender: {self.gender}, ID: {self.academicStaff_id}, Work-Hours: {self.workHours}")


# Main program execution starts here
# Create an empty list to store all college members
members = []

print("-----------------------------------Enter details of NCOE members------------------------------")

# Loop to collect the information for all members
for i in range(1, 6):  # Reduced from 500 to 5 for testing
    print(f"\nMember No: {i}")

    # Ask the member type
    member_type = input("Type (teachertrainers/lecturer/academicstaff): ").lower()

    # Get common information for all members
    name = input("Enter Your Name: ")
    age = int(input("Enter Your Age: "))  # Convert to integer
    phone = input("Enter Your Phone Number: ")
    gender = input("Enter Your Gender: ")

    # Create the appropriate type based on input
    if member_type == "teachertrainers":
        trainers_id = input("Teacher Trainers ID: ")
        member = TeacherTrainers(name, age, phone, gender, trainers_id)
    elif member_type == "lecturer":
        lecturer_id = input("Lecturer ID: ")
        subject = input("Subject: ")
        member = Lecturer(name, age, phone, gender, lecturer_id, subject)
    elif member_type == "academicstaff":
        academicStaff_id = input("AcademicStaff ID: ")
        workHours = input("Work Hours: ")
        member = AcademicStaff(name, age, phone, gender, academicStaff_id, workHours)
    else:
        # If type is invalid, create a generic CollegeMember
        print("Invalid type! ")


    # Add the new member to our list
    members.append(member)

print("\n\n-------------------------------------NCOE Members----------------------------------------")

for member in members:
    # Call the display method appropriate for each member type
    member.display()


""" output:
Member No: 1
Type (teachertrainers/lecturer/academicstaff): teachertrainers
Enter Your Name: dhananjana
Enter Your Age: 23
Enter Your Phone Number: 0775822669
Enter Your Gender: Female
Teacher Trainers ID: s2514

Member No: 2
Type (teachertrainers/lecturer/academicstaff): lecturer
Enter Your Name: Dissanayake
Enter Your Age: 45
Enter Your Phone Number: 0785678934
Enter Your Gender: Male
Lecturer ID: L001
Subject: Sociology

Member No: 3
Type (teachertrainers/lecturer/academicstaff): academicstaff
Enter Your Name: kamal
Enter Your Age: 34
Enter Your Phone Number: 0765678903
Enter Your Gender: Male
AcademicStaff ID: A004
Work Hours: 6
"""


   
