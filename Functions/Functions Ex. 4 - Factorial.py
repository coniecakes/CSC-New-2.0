# write a factorial function
def factorial(num1):
    fact = 1
    if num1%2 == 0:
        for i in range(1, num1+1):
            fact *= i
        print(f'{num1}! = {fact}')
    else:
        fact = num1**4
        print(f'{num1}^4 = {fact}')
    return(fact)

num = int(input("Enter your factorial here: "))

user_fact = factorial(num)


