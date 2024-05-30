# num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# sum = 0
# for i in num:
#     sum += i
# print(sum)
# print()
# sum1 = 0
# for i in range(16):
#     sum1 += i
# print(sum1)
# print()
# sum2 = 0
# for i in range(301):
#     sum2 += i
# print(sum2)
# print()
# prod = 1
# for i in range(1,16):
#     prod *= i
# print(prod)
# print()
# numsqr = 0
# for i in range(0,100,5):
#     numsqr = i**2
#     numsqrplus = numsqr + 4
#     print(numsqrplus)
# print()
# num4 = 0
# for i in range(10,1001,10):
#     if i%50==0:
#         num4+=1
#     print(i)
# print(num4)
print()
prod1 = 1
for i in range(1,528,4):
    prod1 = prod1 * i
    print(i)
print(prod1)
print()
list1 = 0
for i in range(3,303):
    if i%3==0 and i%7==0:
        print("Buzz",i)