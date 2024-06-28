# def factorial(number):
#     if number == 0:
#         return 1
#     else:
#         return number * factorial(number - 1)
#
# print(factorial(3))
#
#
# for i in range(1000):
#     if i == 7:
#         break
#     elif i == 2 or i == 3 or i == 4:
#         continue
#     print(i)
#
#
# class Player:
#     def __init__(self, name, age, height, weight, total_score):
#         self.name = name
#         self.age = age
#         self.height = height
#         self.weight = weight
#         self.total_score = total_score
#
#     def isStarPlayer(self, total_score):
#         if total_score * 3 >= 100:
#             return "Star player"
#         else:
#             return "Not a star player"
#
# p1 = Player("conie",25, 70,170, 35)
# print(p1.name)
# print(p1.isStarPlayer(p1.total_score))
#
# def my_equation(a):
#     x = ((a**3)+(3*a))/(a+1)
#     return x
# print(my_equation(10))
# print(my_equation(13))

# print(3**3)
# print(3*3)
# print(3+1)
# print((27+9)/4)


# class Shape:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#     def get_length(self):
#         return self.length
#     def get_width(self):
#         return self.width
#     def set_length(self, length):
#         self.length = length
#     def set_width(self, width):
#         self.width = width
#     def __str__(self):
#         str1 = "This object is " + str(self.length) + " long and " + str(self.width) + " wide."
#         return (str1)
#     def area(self):
#         a = self.length * self.width
#         return a
#     def paintingCost(self, price_per_sqft = int()):
#         cost = self.area() * price_per_sqft
#         return cost
#
# rect = Shape(4,5)
# print(rect.get_width()) # test getter method
# print(rect.get_length()) # test getter method
# print(rect) # test __str__ method
# print(rect.area()) # test area method
# rect.set_width(10) # test setter method
# print(rect.get_width()) # confirm setter method test
# print(rect.area()) # confirm setter method test
# print(f'The cost of painting is: ${rect.paintingCost(25)}') # test paintingCost method

class Player:
    def __init__(self, name, age, height, weight, total_score):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.total_score = total_score

    def isStarPlayer(self):
        if self.total_score * 3 >= 100:
            return "Star player"
        else:
            return "Not a star player"

p1 = Player("conie", 25, 70,170,30)
print(p1.isStarPlayer())