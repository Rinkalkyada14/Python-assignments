#Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def compute_area(self):
        return self.length * self.width

# Create an instance of Rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
rectangle = Rectangle(length, width)

area = rectangle.compute_area()
print(f"The area of the rectangle is: {area}")
