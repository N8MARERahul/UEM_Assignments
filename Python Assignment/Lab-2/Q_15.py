# Write a Python program that prompts the user to enter a base number and an exponent, and then calculates the power of the base to the exponent. The program should not use the exponentiation operator (**) or the math.pow() function.

base = int(input("Enter the base value: "))
exp = int(input("Enter the exponent value: "))

result = 1

if exp > 1:
    for i in range(exp):
        result *= base
else:
    for i in range(exp - 1, -1):
        result *= 1 / base

print(f"Result = {result}")