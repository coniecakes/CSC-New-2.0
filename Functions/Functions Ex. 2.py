# write a function that takes length, height, and cost per square unit and calculate cost to paint a rectangles
# default value is $20 / square unit
def paint_cost(width, height, cost = 20):
    area = width * height
    print(f"Area: {area} ft'")
    total = cost * area
    print(f'Total Paint Cost: ${total:,.2f}')
    return total

print("Project 1")
width1 = 12
height1 = 6
cost = paint_cost(width1,height1)
print("\nProject 2")
width2 = 15
height2 = 12
cost2 = 18
cost = paint_cost(width2,height2,cost2)