# Write a Java program to find area and perimeter of a circle.

import math

radius = float(input("Enter the radius of the circle: "))

print(f"Area = {round(math.pi * radius * radius, 3)}")

print(f"perimeter = {round(2 * math.pi * radius, 3)}")