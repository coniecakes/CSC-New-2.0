# name = input("Enter your name here:")
# salary = input("Enter your salary here: ")
# print(name)
# print("$" + salary)
# print()
# var1 = input("Enter first number here: ")
# var2 = input("Enter second number here: ")
# total = int(var1)+int(var2)
# print(total)
# var1 = input("Enter string 1: ")
# var2 = input("Enter string 2: ")
# print(var1+" " +var2)


P = float(input("Enter Principal Amount: "))
N = int(input("Enter Number of Periods (in years): ")) * 12
R = float(input("Enter Interest Rate (as percentage): ")) / 100
i = (R)/12
numerator = i*(1+i)**N
denominator = (1+i)**N-1
# print(float(i))
# print(numerator)
# print(denominator)
A = P*(numerator/denominator)
print(f"Your monthly mortgage payment is: ${A:.2f}")