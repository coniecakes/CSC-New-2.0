class Student:
    name = "Name"
    dob = "DOB"
    gender = "Gender"
    rollnum = "Roster Number"
    major = "Major"

#main program starts here

#create an instance of this Student class.
john = Student()
print (john.name, john.rollnum, john.major)

# objects are MUTABLE and so we can change their values as desired
john.name = "John"
john.dob = "1/1/2000"
john.gender = 'm'
john.rollnum = 'AU123'
john.major = 'compsci'

print (john.name, john.rollnum, john.major)
