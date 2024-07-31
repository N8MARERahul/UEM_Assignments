# Write a program in Python to check if a number is Krishnamurthy number.

import math

num = int(input("Enter a positive integer number: "))

if num < 0:
    print("Please enter a positive integer number")
    exit()
n = num
result = 0
while n > 0:
    digit = n % 10
    result += math.factorial(digit)
    n //= 10

if result == num:
    print(f"{num} is a Krishnamurthy number")
else:
    print(f"{num} is not a Krishnamurthy number")