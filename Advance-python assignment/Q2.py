#Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle 

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        return 3.14159 * self.radius ** 2

    def compute_perimeter(self):
        return 2 * 3.14159 * self.radius

# Create an instance of Circle
radius = float(input("Enter the radius of the circle: "))
circle = Circle(radius)

area = circle.compute_area()
perimeter = circle.compute_perimeter()

print(f"The area of the circle is: {area}")
print(f"The perimeter of the circle is: {perimeter}")
