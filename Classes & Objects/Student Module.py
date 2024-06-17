class Student:
    def __init__(self, name, dob, gender, rollnum, major, gpa=0.0):
        self.name = name
        self.dob = dob
        self.gender = gender
        self.rollnum = rollnum
        self.major = major
        #add a new attribute and assign it a default value
        self.gpa = gpa

    #the default method to allow us to print this object
    def __str__(self):
        str1 = 'This is '+ self.name+ '\'s record.\n'
        str2 = 'Their AU ID is ' + self.rollnum
        retstr = str1 + str2
        return retstr

    #getter methods
    def get_name(self):
        return self.name
    def get_dob(self):
        return self.dob
    def get_rollnum(self):
        return self.rollnum
    def get_gpa(self):
        return self.gpa
    def get_major(self):
        return self.major

    #setter methods
    def set_gender(self, gender):
        self.gender = gender
    def set_rollnum(self, rollnum):
        self.rollnum = rollnum
    def set_gpa(self,gpa):
        self.gpa = gpa
    def set_major(self, major):
        self.major = major
    def set_dob(self, dob):
        self.dob = dob

    #class methods
    def isDeansList(self):
        if self.gpa >= 3.9:
            return 1
        else:
            return 0