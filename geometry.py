import math

import calculator

class GeometryCalculator:

    def calculate_circle_area(self, radius):
        return math.pi * radius ** 2

    def calculate_rectangle_area(self, length, width):
        return length * width
    
    radius = 5
    print(f"Circle Area = {calculator.calculate_circle_area(radius)}")