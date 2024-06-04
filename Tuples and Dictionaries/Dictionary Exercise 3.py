# my attempt
str1 = "Journyx technology, from the source code of our software to the code that maintains our Web site and ASP sites, is entirely based on Python. It increases our speed of development and keeps us several steps ahead of competitors while remaining easy to read and use. It's as high level of a language as you can have without running into functionality problems. I estimate that Python makes our coders 10 times more productive than Java programmers, and 100 times more than C programmers."
list1 = str1.split()
dict1 = {}
for i in list1:
    dict1[i] = list1.count(i)
print(dict1)

# prof's code
dict2 = {}
for i in list1:
    if i not in dict2.keys():
        dict2[i] = list1.count(i)
print(dict2)
