import myimportmodule

x = 5
y = 10
z = 15

a = myimportmodule.sum_of_three(x,y,z)
print(a)
print()
str1 = "Conie"
b = myimportmodule.name_tag(str1)
print(b)
print()
c = 9
d = myimportmodule.cubes(c)
print(d)

stud1 = myimportmodule.Student("John","Doe","Accounting")
stud2 = myimportmodule.Student("Jane","Doe","CompSci")
stud3 = myimportmodule.Student("Thomas","Jones","Communications")
stud4 = myimportmodule.Student("Levi","Strauss","History")

print(stud4.get_fname())
