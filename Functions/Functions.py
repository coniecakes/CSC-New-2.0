# define a function - begins with 'def' followed by a name

def time_taken (dist, speed=30): # you can set a default value from right to left
    timeTaken = (dist/speed)
    print(f'{dist} miles')
    print(f'{speed} miles per hour')
    print(f'{timeTaken} hours')
    return (timeTaken) # returning the value that was calculated

location_1 = 'Bethesda'
distance_1 = 10
speed_1 = 20
time1 = time_taken(distance_1, speed_1) # call the function --> using the function
print()
location_2 = "Foggy Bottom"
distance_2 = 7.5
time2 = time_taken(distance_2)

# functions have 1 or more parameters (what go into the function for the calculation)
# arguments are values passed into the function
print()

def add_numbers(num1, num2, num3=10):
    total = num1 + num2 + num3
    print(num1, num2, num3, '\n\tTotal:', total)
    return(total)
x = 10
y = 15
z = 20
sum = add_numbers(x,y,z)
print()
a = 2
b = 3
sum1 = add_numbers(a,b)