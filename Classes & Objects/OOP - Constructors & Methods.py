class Student:
    def __init__(self, name, dob, gender, rollnum, major):
        self.name = name
        self.dob = dob
        self.gender = gender
        self.rollnum = rollnum
        self.major = major

    #getter methods
    def get_name(self):
        return self.name
    def get_dob(self):
        return self.dob
    def get_rollnum(self):
        return self.rollnum
    def get_major(self):
        return self.major
    def get_dob(self):
        return(self.dob)
    def get_gender(self):
        return(self.gender)

    #setter methods
    def set_gender(self, gender):
        self.gender = gender

    def set_rollnum(self, rollnum):
        self.rollnum = rollnum

    def set_name(self, name):
        self.name = name

    def set_dob(self, dob):
        self.dob = dob

    def set_major(self, major):
        self.major = major

# #main program begins here
john = Student('John Last', '1/1/2000', 'M', 'AU123', 'compsci')

# #use the getter methods
print (john.get_name())
#
# #use setter methods
john.set_rollnum('AU321')
# #and the getter methods
print (john.get_rollnum())
john.set_gender('NB')
print(john.get_gender())


