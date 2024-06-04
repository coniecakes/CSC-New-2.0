# dictionary of 1 to 100 that are divisible by 5
dict1 = {}
for i in range (1,101):
    if i%5 == 0:
        dict1[i] = i**3
print(dict1)
print()
dict2 = {}
num = 1
while num <= 100:
    if num%5 == 0:
        dict2[num] = num**3
    num += 1
print(dict2)

