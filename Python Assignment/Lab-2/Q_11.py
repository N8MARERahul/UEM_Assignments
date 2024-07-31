# Write a program in Python to find the sum of digits of a number.

num = int(input("Enter a positive integer number: "))

result = 0
while num != 0:
    digit = num % 10
    result += digit
    num //= 10

print(f"SUM = {result}")