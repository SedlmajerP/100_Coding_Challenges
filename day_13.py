# Question 47
# Define a class named Circle which can be constructed by a radius.
# The Circle class has a method which can compute the area.

class Circle():
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        _constPI = 3.14159
        area = _constPI*(self.radius**2)
        print(area)


circle1 = Circle(20)

print("\nQuestion 47:")
circle1.area()

# Question 48
# Define a class named Rectangle which can be constructed by a length and width.
# The Rectangle class has a method which can compute the area.


class Rectangle():
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

    def rect_area(self):
        area = self.lenght*self.width
        print(area)


rect = Rectangle(10, 5)
print("\nQuestion 48:")
rect.rect_area()


# Question 49
# Define a class named Shape and its subclass Square.
# The Square class has an init function which takes a length as argument.
# Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

class Shape():
    def area(self):
        area = 0
        print(area)


class Square(Shape):
    def __init__(self, lenght=0):
        self.lenght = lenght

    def square_area(self):
        area = self.lenght**2
        print(area)


square = Square(5)
print("\nQuestion 49:")
Shape().area()
square.square_area()

# Question 50
# Please raise a RuntimeError exception.


def count(x, y):
    if x < 0 or y < 0:
        raise RuntimeError("Number muset not be lower than zero")
    else:
        print(x + y)


print("\nQuestion 50:")
count(-1, 2)
