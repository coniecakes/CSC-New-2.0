list1 = []
for i in range(1400, 2101):
    if i%7 == 0 and i%9 ==0:
        list1.append(i)
print(list1)
#
# def factorial(num1):
#     fact = 1
#     if num1%2 == 0:
#         for i in range(1, num1+1):
#             fact *= i
#         print(f'{num1}! = {fact}')
#     else:
#         fact = num1**3
#         print(f'{num1}^3 = {fact}')
#     return(fact)
#
# num = int(input("Enter your number here: "))
# user_fact = factorial(num)
#
# #create a list of prime numbers from 2 to 100, inclusive
# prime_num = []
# for i in range(2, 101):
#     num = 2
#     if i%num == 0:
#         i += 1
#     elif i%num != 0:
#         num += 1
#     else:
#         prime_num.append(i)
# print(prime_num)

prime_num = []
for i in range(2, 101):
    is_prime = True
    for num in range(2, int(i**0.5) + 1):
        if i % num == 0:
            is_prime = False
            break
    if is_prime:
        prime_num.append(i)
print(prime_num)
print()


a=1
b=1
count = 0
fib = []
while len(fib) < 10:
    next_term = a+b
    if next_term%2 == 0:
        fib.append(next_term)
    a, b=b, next_term
    count += 1
print(fib)

print(11//2)

print()
grade = 75
if grade < 50:
     print("F")
elif grade < 60:
     print("D")
elif grade < 75:
     print("C")
elif grade < 85:
     print("B")
elif grade <= 100:
     print("A")
else:
     print("Invalid grade")

# Prof's code for prime number problem
list1 = []
remove = 0
for x in range (2,100):
    remove = 0
    list1.append(x)
    for y in range (2,x):
        if x%y==0:
            remove = 1
    if remove:
        list1.remove(x)

print (list1)