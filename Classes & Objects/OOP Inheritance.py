class Person():
    def __init__(self, fname, lname, dob, gender):
        self.fname = fname
        self.lname = lname
        self.dob = dob
        self.gender = gender
    #crete the getter and setter methods
    #also create the __str__ method

    def printName(self):
        print(self.fname, self.lname)

#define a child class for the Person class
class Student (Person):

    #construtor for the child class
    def __init__(self, fname, lname, dob, gender, year, major, gpa):
        #the below is the parent's constructor
        Person.__init__(self, fname, lname, dob, gender)
        #assign values to the child class attributes
        self.year = year
        self.major = major
        self.gpa = gpa

    #a child class method
    def printYear(self):
        print(self.year)

p1 = Person("n", "d", "June 1 1990", "Male")

s1 = Student("J", "T", "June 1 2000", "Female", 2020,"CompSci", 3.4)

s1.printName()
s1.printYear()

p1.printName()

#we cannot call the chid class method from a parent class object
#p1.printYear()

#child class object has access to parent class attributes
print (s1.fname)

#parent class objects do not have access to child class attributes
#print (p1.year)