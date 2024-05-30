list1 = [1,2,3,4,5,6,7,8,9, 10, 11, 12, 13]
# sum = 0
# for i in list1:
#     sum += i
#
# print(sum)
# print()
# sum1 = 0
# for i in list1:
#     if i%2 == 0:
#         sum1 = sum1 + i
# print(sum1)

list2 = [2, 4, 6, 8, 10, 12, 16, 18, 20]
sqr = 0
for i in list2:
    print(i**2)
print()
print("exercise 2")
for j in list1:
    if j%2==0:
        print(j)
print()
print('exercise 3')
count1 = 0
list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for k in list3:
    if k%2==0:
        count1 += 1
print(count1)
print()
print("ex. 4")
count2 = 0
for l in list3:
    count2 += l ** 2
print(count2)
print()
count3 = 0
str1 = "Understanding that hard problems can be solved by step-by-step algorithmic processes (and having technology to execute these algorithms for us) is one of the major breakthroughs that has had enormous benefits. So while the execution of the algorithm may be boring and may require no intelligence, algorithmic or computational thinking — i.e. using algorithms and automation as the basis for approaching problems — is rapidly transforming our society. Some claim that this shift towards algorithmic thinking and processes is going to have even more impact on our society than the invention of the printing press. And the process of designing algorithms is interesting, intellectually challenging, and a central part of what we call programming."
for i in str1.split():
    if len(i)%5==0:
        count3 += 1
print(count3)




