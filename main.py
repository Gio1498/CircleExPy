from circle import Circle

circle1 = Circle(radius = 7)
circle2 = Circle(diameter = 5)
circle3 = Circle(radius = 10)

# insert all circles in a list
circles = [circle1, circle2, circle3]

# print the value of all circles in list
for circle in circles:
    circle.print_circle()

# sort the list of circles in size order decreasing
circles.sort(key = lambda circle: circle.radius, reverse = True)

# check if in the list there are any circles with same radius
for i in range(len(circles) - 1):
    if circles[i].radius == circles[i + 1].radius:
        print("There are circles with same radius")
        break
    else:
        print("There are no circles with same radius")
        break

# print first element of list
print("Circle with radius ",circles[0].radius ," is the biggest")	