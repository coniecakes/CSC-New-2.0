# a=1
# b=1
# count = 2
# fib = [a,b]
# print("The first term = ", a)
# print("The second term = ", b)
# print()
# sum = 0
# while count <= 100:
#     next_term = a+b
#     fib.append(next_term)
#     a=b
#     b=next_term
#     count += 1
# print(fib)
# print()
# print()
# a=1
# b=1
# c=0
# count = 2
# fib = [a,b]
# # print("The first term = ", a)
# # print("The second term = ", b)
# # print()
# # sum0 = 0
# # while True:
# #     next_term = a+b
# #     print(count, "th term = ", next_term)
# #     a,b = b,next_term
# #     fib.append(next_term)
# #     count += 1
# #     if(count == 100):
# #         break
# # print(fib)
# # print()
# sum = 0
# # while True:
# #     next_term = a+b
# #     sum += next_term
# #     a,b = b,next_term
# #     fib.append(next_term)
# #     count += 1
# #     if(count == 100):
# #         break
# # print(fib)
# # print(sum)
# # print(len(fib))
# while count < 100:
#     next_term = a+b
#     sum += next_term
#     a,b = b,next_term
#     fib.append(next_term)
#     count += 1
# print(fib)
# print(sum)
# print(len(fib))
# print()
# n = 1
# a1 = 1
# d = 3
# list1 = []
# while n < 10:
#     next_term = a1 + (n-1)*d
#     list1.append(next_term)
#     n += 1
# print(list1)
# t1 = 1
# list1 = []
# while t1 < 10:
#     term = (t1*(t1+1))/2
#     list1.append(int(term))
#     t1 += 1
# print(list1)
# print(type(list1[1]))
# a = 1
# b = 1
# count = 2
# fib = [a,b]
# while count < 100:
#      next_term = a+b
#      fib.append(next_term)
#      a=b
#      b=next_term
#      count += 1
# print(fib)
# print(len(fib))
# print()
# c,d = 1,1
# fib1 = []
# for i in range(100):
#     fib1.append(c)
#     c,d = d,d+1
# print(fib1)
# print(len(fib1))
a1 = 2
r = 2
list2 = []
while True:
    term = a1*(r**(a1-1))
    list2.append(term)
    a1 += 1
    if len(list2) == 10:
        break
print(list2)