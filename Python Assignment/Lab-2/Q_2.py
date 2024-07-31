# To solve the quadratic equation.

import math

def solve_quadratic(a, b, c):
    # Calculate the discriminant
    dis = b**2 - 4*a*c
    sqrt_value = math.sqrt(abs(dis))
    
    # Calculate the two solutions
    if dis > 0:
        print("Real and Different Roots ->")
        print(f"Root - 1 -> {(- b + sqrt_value) / (2 * a)}")
        print(f"Root - 2 -> {(- b - sqrt_value) / (2 * a)}")

    elif dis == 0:
        print("Real and same Roots ->")
        print(f"Root -> {- b / (2 * a)}")

    else:
        print("Complex Roots ->")
        print(f"{- b / (2 * a)} + {sqrt_value / (2 * a)}i")
        print(f"{- b / (2 * a)} - {sqrt_value / (2 * a)}i")


def main():
    print("Equation format: ax^2 + bx + c = 0")
    
    # Get coefficients from the user
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    
    # Check if 'a' is not zero to ensure it's a quadratic equation
    if a == 0:
        print("The coefficient 'a' must not be zero for a quadratic equation.")
        return
    
    # Solve the quadratic equation and Display the results
    print(f"The roots of the equation {a}x^2 + {b}x + {c} = 0 are:")
    solve_quadratic(a, b, c)

if __name__ == "__main__":
    main()
