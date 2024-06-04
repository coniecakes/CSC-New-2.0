dict1 = {"num1":"Donald","num2":"Mickey","num3":"Bugs","num4":"Daffy"}
print(dict1)
print(type(dict1))
print()
# print the keys from the dictionary
print(dict1.keys())
print()
# print the values from the dictionary
print(dict1.values())
print()
# use keys method to iterate through all keys in a dictionary
for k in dict1.keys():
    print(k)
print()
for k in dict1.keys():
    print(k, ":", dict1[k])
print()
# use keys method to iterate through each key to use its associated value
for k in dict1.keys():
    if (dict1[k] == 'Bugs'):
        print("Value 'Bugs' has key : ", k)
print()
print(dict1.values())
for val in dict1.values():
    print(val)
print()
print(list(dict1.items()))
print()