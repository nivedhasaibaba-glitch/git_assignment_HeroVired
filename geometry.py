import math

import calculator

class GeometryCalculator:

    def calculate_circle_area(self, radius):
        return math.pi * radius ** 2

    def calculate_rectangle_area(self, length, width):
        return length * width

    length = 10
    width = 6
    print(f"Rectangle Area = {calculator.calculate_rectangle_area(length, width)}")