import math


# Base class
class Shape:
    def area(self):
        """Calculate the area of the shape (to be implemented by subclasses)."""
        raise NotImplementedError("Subclasses must implement this method.")


# Circle subclass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


# Rectangle subclass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Function that uses polymorphism
def total_area(shapes):
    """
    Calculate the total area of a list of shapes.

    Parameters:
        shapes (list): A list of objects that implement area().

    Returns:
        float: The sum of all areas.
    """
    return sum(shape.area() for shape in shapes)


# Example usage
shapes = [Circle(5), Rectangle(4, 6), Circle(3)]
print("Total area:", total_area(shapes))