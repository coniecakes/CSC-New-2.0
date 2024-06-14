class Student:
    def __init__(self, name, dob, gender, rollnum, major, gpa=0.0):
        self.name = name
        self.dob = dob
        self.gender = gender
        self.rollnum = rollnum
        self.major = major
        #add a new attribute and assign it a default value
        self.gpa = gpa
    #create a default function that gets called for print
    def __str__(self):
        retstr = "This is " + self.name + " and the dob is " + self.dob
        return (retstr)

    #getter methods
    def get_name(self):
        return self.name
    def get_dob(self):
        return dob
    def get_rollnum(self):
        return self.rollnum
    def get_gpa(self):
        return self.gpa
    def get_gender(self):
        return(self.gender)
    #setter methods
    def set_gender(self, gender):
        self.gender = gender
    def set_rollnum(self, rollnum):
        self.rollnum = rollnum
    def set_gpa(self,gpa):
        self.gpa = gpa
    def set_dob(self, dob):
        self.dob = dob
    def set_major(self, major):
        self.major = major
    def set_gpa(self, gpa):
        self.gpa = gpa
    #class methods


# #main program begins here
# #even though we added a attribute to the class we dont have to change the previous instantiation
john = Student('John Day', '1/1/2000', 'm', 'AU123', 'compsci')
#
print (john.get_gpa())
# #we can set the attribute value using the setter methods
john.set_gpa(3.49)
#
print (john.get_gpa())
john.set_gender('NB')
print(john.get_gender())
john.set_major("Comp Sci")
print(john.major)
jane = Student ('Jane Doe', '1/1/2001', 'f', 'AU124', 'Pol Sci', 3.91)
print (jane.get_gpa())

print (john)
print (jane)

