#Write a function day_name that converts an integer number 0 to 6 into the name of a day. Assume day 0 is “Sunday”.
# return None if the arguments to the function are not valid.
# print (day_name(3))  would print "Wednesday"
# print (day_name(6)) would print "Saturday"
# print (day_name(42)) would print “None”
def weekday(a):
    if a == 0:
        print(f'Sunday.')
    elif a == 1:
        print(f'Monday.')
    elif a == 2:
        print(f'Tuesday.')
    elif a == 3:
        print(f'Wednesday.')
    elif a == 4:
        print(f'Thursday.')
    elif a == 5:
        print(f'Friday.')
    elif a == 6:
        print(f'Saturday.')
    else:
        print(f'None.')
    return(a)
a = 5
weekday(a)

def day_name(x):
    dict1 = {0:"Sunday", 1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday"}
    if x in dict1:
        return(dict1[x])
    else:
        return("None")

x = int(input("Enter your day number here: "))
print(day_name(x))
