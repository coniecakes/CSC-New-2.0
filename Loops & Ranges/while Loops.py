#use while loops when you don't know how many times you want to do something
# while xxxx condition = TRUE:
    #statement 1
    #statement 2
    #statement x
# countdown = 10
# while countdown > 0:
#     print(countdown)
#     countdown -= 1
# print("Blastoff!")
# sum = 0
# num = 1
# while num < 101:
#     sum += num
#     num += 1
# print(sum)
# print(num)
# print()
# even_num = 0
# while even_num < 101:
#     even_num += 1
#     if even_num%2==0:
#         print(even_num)
# print()
# list1 = []
# list2 = []
# x = 0
# while x < 101:
#     x += 1
#     if x%2==0:
#         list2.append(x)
#     else:
#         list1.append(x)
# print("These are the odd numbers ", list1)
# print("These are the even numbers ", list2)

# print()
# prod = 1
# num1 = 1
# factorial = int(input("Enter your number here: "))
# while num1 <= factorial:
#     prod *= num1
#     num1 += 1
# print(prod)

#Use the while loop to find the smallest number that is divisible by all integers from 1 to 9
#2520
num = 9
while num < 9999999:
    if num%1 == 0 and num%2 == 0 and num%3 == 0 and num%4 == 0 and num%5 == 0 and num%6 == 0 and num%7 == 0 and num%8 == 0 and num%9 == 0:
        print(num)
        break
    num += 1
