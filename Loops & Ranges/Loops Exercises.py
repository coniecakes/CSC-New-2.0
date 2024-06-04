# find the sum of the first 100 terms of the Fibonacci series
# a = 1, b = 1
# find the first term in the series greater than 1000
a,b = 1,1
fib = [a,b]
count = 2
sum = a+b
while True:
    next = a+b
    a,b = b,next
    fib.append(next)
    count += 1
    sum += next
    if count == 100:
        break
print(fib)
print(len(fib))
print(sum)