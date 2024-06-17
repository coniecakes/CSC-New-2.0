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

class Roster:
    def __init__(self, roster_list=[]):
        self.roster_list = []

    def get_roster_list(self):
        return self.roster_list

    def add_student(self, student):
        self.roster_list.append(student)
    def add_accounting_list(self):
        accounting_maj = []
        for student in self.roster_list:
            if student.get_major() == "Accounting":
                accounting_maj.append(student)
        return accounting_maj

    def get_deanslist(self):
        deanslist = []
        for i in self.roster_list:
            if i.isDeansList():
                deanslist.append(i)
        return deanslist
    def __str__(self):
        str1 = "This is the Dean's List:\n "
        str2 = deanslist
        retstr = str1 + str2
        return retstr

john = Student("John Bon Jovi", 11/11/2002, "M", "AU13579", "Accounting", 3.71)
jane = Student("Jane Doe", 4/20/1999,"F", "AU2468", "Accounting", 3.92)
conie = Student("Conie O'Malley", 6/19/1992, "NB", "AU12345","Accounting", 3.80)
jackson = Student("Jackson T", 1/5/2004, "M", "AU23456", "Biochemistry",4.0)
mathew = Student("Mathew H", 9/11/2001, "M", "AU34567","Business", 2.75)

# Accounting = Roster()
roster = Roster()
roster.add_student(john)
roster.add_student(jane)
roster.add_student(conie)
roster.add_student(jackson)
roster.add_student(mathew)
# Accounting.add_student(john)
# Accounting.add_student(jane)
# Accounting.add_student(conie)
conie.set_gpa(3.95)
accounting_students = roster.add_accounting_list()
deans_list_students = roster.get_deanslist()
print("Accounting Students:\n")
for student in accounting_students:
    print(student)
print("\nDean's List Students:\n")
for student in deans_list_students:
    print(student)
# list1 = Accounting.get_roster_list()
# print(list1)
# print()
# deanslist = Accounting.get_deanslist()
# for i in deanslist:
#     print(i)