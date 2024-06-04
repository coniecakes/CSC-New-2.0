a = 1
b = 1
count = 2
fib = [a,b]
next_term = 0
print("first term = ",a)
print("second term = ",b)

sum = 0
while count <= 100:
    next_term = a+b
    fib.append(next_term)
    a,b = b,next_term
    count += 1
print(fib)
print(len(fib))