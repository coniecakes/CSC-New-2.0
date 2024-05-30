# fruits = ['apple', 'orange', 'banana', 'kiwi', 'mango']
# print(fruits)
# print()
# print(fruits[1])
# print()
# odd_numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
# # even_numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 24, 26]
# print(odd_numbers[5]+even_numbers[5])
# print(odd_numbers[5])
# print(even_numbers[5])
# print()
# print(odd_numbers[:5])
# print(even_numbers[5:10])
# print(even_numbers[::-5])
# print(even_numbers[:-3])
# print(odd_numbers[:99])
# lengthoflists = len(odd_numbers)
# del(odd_numbers[3])
# print(odd_numbers)
# print()
# var2 = 5
# if var2 in even_numbers:
#     print("5 is in the list")
# if var2 not in even_numbers:
#     print("5 is not in the list")
# even_numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# print(len(even_numbers))
# print()
# del(even_numbers[4])
# print(len(even_numbers))
# var1 = 6
# if var1 in (even_numbers):
#     print("6 is in the list")
# if var1 not in (even_numbers):
#     print("6 is not in the list")
# print()
# var2 = 7
# if var2 in (even_numbers):
#     print("7 is in the list")
# if var2 not in (even_numbers):
#     print("7 is not in the list")
# print()
# var3 = 21
# if var3 not in (even_numbers):
#     print("21 is not in the list")
# else:
#     print("21 is in the list")
# print()
list1 = [1, 3, 5, 7, 9, 11]
print(type(list1))
print()
list1.append('Conie')
print(list1)
list1.insert(1,1234)
print(list1)
print()
list1.remove('Conie')
print(list1)
print()
list1.reverse()
print(list1)
print()
sortedlist = sorted(list1)
print(sortedlist)
