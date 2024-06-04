# collection of key:value pairs
# within curly {} brackets - key & value can be any data pair
# all key:value pairs are independent of each other
# no indexing in a dictionary - access elements by using the key
dict1 = {"num1":"Donald","num2":"Mickey","num3":"Bugs","num4":"Daffy"}
dict2 = {1:123, 2:234, 3:345, 4:456}
print(dict1)
print()
print(dict1["num1"])
print()
print()
dict_of_squares = {}
for i in range(10):
    dict_of_squares[i] = i**2
print(dict_of_squares)
del(dict_of_squares[5])
print(dict_of_squares)
