# weekday = int(input("Type the number of your weekday: "))
#
# if(weekday==0):
#     print("Sunday")
# elif(weekday==1):
#     print("Monday")
# elif(weekday==2):
#     print("Tuesday")
# elif(weekday==3):
#     print("Wednesday")
# elif(weekday==4):
#     print("Thursday")
# elif(weekday==5):
#     print("Friday")
# elif(weekday==6):
#     print("Saturday")
# else:
#     pass

# number1 = 5
# number2 = 6
# number3 = 4
#
# if(number1>number2):
#     if(number1>number3):
#         print(number1, " is greater than ", number2, " and ", number3)
#     if(number2>number3):
#         print(number2, " is greater than ", number1, " and ", number3)
#     else:
#         print(number3, " is greater than ", number1, " and ", number2)
# print("this is the end")

# num1 = int(input("enter your first number here: "))
# num2 = int(input("enter your second number here: "))
# num3 = int(input("enter your third number here: "))
# num4 = int(input("enter your fourth number here: "))
#
# if(num1>num2):
#     if(num2>num3) and (num3>num4):
#         print(num1, " is the greatest")
# if(num2>num3) and (num3>num4) and (num1<num2):
#     print(num2, " is the greatest")
# if(num3>num4) and (num1<num2) and (num2<num3):
#     print(num3, " is the greatest")
# if(num4>num3) and (num2<num3) and (num1<num2):
#     print(num4, " is the greatest")

userNum = int(input("Enter your number here: "))
if (userNum%5==0) or (userNum%7==0):
    print("You're a winner baby!")
    if(userNum%8==0):
        print("You're a super winner baby!")
else:
    print("You're not a winner.")