# write a function that finds the factorial of a number
def factorial(num1):
    count = num1
    while count > 1:
        count -= 1
        num1 *= count
    print(num1)
    return(num1)

test = factorial(4)
print(4*3*2*1)

def factorial_new(num):
    fact = 1
    for i in range(1, num+1):
        fact = fact*i
    return(fact)

print(factorial_new(4))