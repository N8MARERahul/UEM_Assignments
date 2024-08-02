# Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(a, b):
    slope = -b / a
    return slope

print("Enter the Linear equation, Format: Ax + By + C = 0")
a = int(input("Enter the value of A: "))
b = int(input("Enter the value of B: "))

print(f"Slope of the Linear Equation is = {calculate_slope(a, b)}")