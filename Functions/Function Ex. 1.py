# Create a function that finds the sum 5 numbers but squares all even numbers and cubes all odd numbers

def sum_of_squares(num1, num2, num3, num4, num5):
    ss = 0
    list1 = [num1, num2, num3, num4, num5]
    for i in list1:
        if i%2 == 0:
            ss += (i**2)
        else:
            ss += (i**3)
    print(f'Sum of Squares and Cubes: {ss}')
    return(ss)


list1 = [1, 2, 3, 4, 5]
print(list1)
sum = sum_of_squares(list1[0],list1[1],list1[2],list1[3],list1[4])
print(sum)
print(1+(2**2)+(3**3)+(4**2)+(5**3))
print()
list2 = [10, 12, 31, 24, 5]
print(list2)
sum = sum_of_squares(list2[0],list2[1],list2[2],list2[3],list2[4])
print(sum)
print((10**2)+(12**2)+(31**3)+(24**2)+(5**3))
print()
list3 = [10, 12, 31, 24, 5]
print(list3)
sum = sum_of_squares(*list3)
print(sum)
print((10**2)+(12**2)+(31**3)+(24**2)+(5**3))