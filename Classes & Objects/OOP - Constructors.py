class Student:

   #create a constructor for the class. The constructor has a special name
   #the name is always __init__(self)
    def __init__(self, name, dob, gender, rollnum, major):
        self.name = name
        self.dob = dob
        self.gender = gender
        self.rollnum = rollnum
        self.major = major


john = Student('John', '1/1/2000', 'm', 'AU123', 'compsci')
#
print (john.name)
#
# #an object is MUTABLE
# #you can change the value of an object anytime
john.dob = '2/1/2000'

print(f'Name: {john.name}\nDOB: {john.dob}\nGender: {john.gender}\nID Number: {john.rollnum}\n'
      f'Major: {john.major}')
john.major = "Comp Sci"
john.gender = "NB"
print()
print(f'Name: {john.name}\nDOB: {john.dob}\nGender: {john.gender}\nID Number: {john.rollnum}\n'
      f'Major: {john.major}')