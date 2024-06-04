a,b = 1,1
fib = [a,b]
count = 3
next = a+b
while True:
    next = a + b
    if next > 10000:
        print(next)
        print(count)
        break
    a,b = b,next
    fib.append(next)
    count += 1
