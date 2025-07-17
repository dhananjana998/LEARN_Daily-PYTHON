class Student_01:

     def followed(self):
       return "Music"
       
class Student_02:

    def follwed(self):
      return "Dancing"

class Student_03:

  def follwed(self)
    return "Art"

#polymorphism in action 
def second_section_Sub(subject):
  return subject.follwed()

#create object 
student_01=Student_01()
student_02=Student_02()
student_03=Student_03()


print(second_section_Sub(student_01))#output Music
print(second_section_Sub(student_02))#output Dancing 
print(second_section_Sub(student_03))#output Art
