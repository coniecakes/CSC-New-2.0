# import student module
# from student module import Student

class Roster:
    def __init__(self, roster_list=[]):
        self.roster_list = []

    def get_roster_list(self):
        return self.roster_list

    def add_student(self, student):
        self.roster_list.append(student)

    def get_deanslist(self):
        deanslist = []
        for i in self.roster_list:
            if i.isDeansList():
                deanslist.append(i)
        return deanslist

#create a new student
john = Student('John', '1/1/2000', 'm', 'AU123', 'compsci', 3.4)

#create an object of  the Roster class
compsci = Roster()

#add the student to the roster
compsci.add_student(john)

list1 = compsci.get_roster_list()

#
#create and add another student
jane = Student('Jane', '1/1/2000', 'm', 'AU124', 'compsci', 3.9)
compsci.add_student(jane)

narendra = Student ('ND', '1/1/2000', 'm', 'AU100', 'compsci', 3.9)
compsci.add_student(narendra)

# for i in compsci.get_roster_list():
#       print (i)

deanslist = compsci.get_deanslist()
for i in deanslist:
      print (i)