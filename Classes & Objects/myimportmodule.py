def sum_of_three(num1, num2, num3):
    sum = num1 + num2 + num3
    return (sum)

def cubes(num1):
    cube = num1**3
    return cube

def name_tag(name):
    return(f'Hello {name}!')

class Student:
    def __init__(self, fname, lname, major):
        self.fname = fname
        self.lname = lname
        self.major = major

    def get_fname(self):
        return self.fname
    def get_lname(self):
        return self.lname
    def get_major(self):
        return self.major
    def set_fname(self, fname):
        self.fname = fname
    def set_lname(self, lname):
        self.lname = lname
    def set_major(self, major):
        self.major = major


