class my_one:
    def firstName(self):
        print("My First Name Sachini")
        self.__lastName()  # access to the private variable

    def __lastName(self):  #private variable
        print("My Last Name Dhananjana")



myObj = my_one()     #create object
myObj.firstName()


"""
output:
My First Name Sachini
My Last Name Dhananjana
"""
