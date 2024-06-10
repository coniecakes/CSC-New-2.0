# classes have attributes & methods
# automobile class
# Attributes: (different)
    # Tires: 2, 4, 6, 3, 12, 16
    # Headlights: 1, 2, 4
    # Windshield: Yes or No
# Methods: --> denoted by m in dropdown (.append, .sort, etc.)
    # Forward
    # Backward
    # Brake

class Student:
    name = ""
    dob = ""
    id_num = ""
    major = ""

student1 = Student()
print(type(student1))
student1.dob = "6/10/1992"
student1.name = "Johnnie"
student1.id_num = "1234"
student1.major = "Finance"
print(student1.name, student1.id_num, student1.dob, student1.major)

class Automobile:
    tires = int()
    headlights = int()
    windshield = True or False

vehicle1 = Automobile()
print(type(vehicle1))
vehicle1.windshield = True
vehicle1.headlights = 2
vehicle1.tires = 4
print(vehicle1.tires, vehicle1.headlights, vehicle1.windshield)

# using a constructor --> takes objects as its attributes

class Students:
    def __init__(self, name, dob, id_num, major):
        self.name = name
        self.dob = dob
        self.id_num = id_num
        self.major = major

student2 = Students('John', '1/1/2000', 'AU1234','Finance')
print(student2.id_num, student2.name)

student3 = Students('Tara','1/5/1998','AU5678','Comp Sci')
student4 = Students('Lindsi','4/5/1999','AU2468','Poly Sci')
student5 = Students('Brittany','11/15/1994','AU0001','Literature')
print(student5.name)
student5.name = "Britney"
print(student5.name)

student_list = [student2, student3, student4, student5]

for i in student_list:
    print(f'{i.name}', end="\n")

