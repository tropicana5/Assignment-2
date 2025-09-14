class Shape:
    def __init__(self):
        print("✅ Shape constructor called - initializing shape properties")

    def calculate_area(self):
        # Base class version does nothing
        print("Shape's calculate_area() called (no area calculation here)")


class Rectangle(Shape):
    def __init__(self, width, height):
        # Not calling super().__init__() here (on purpose for this example)
        self.width = width
        self.height = height

    def calculate_area(self):
        # Call Shape's constructor inside this method
        super().__init__()  # triggers Shape __init__

        # Optionally call Shape's calculate_area()
        super().calculate_area()

        # Rectangle-specific area calculation
        area = self.width * self.height
        print(f"Rectangle area: {area}")
        return area


# Example usage
rect = Rectangle(5, 10)
rect.calculate_area()