# Write a Java Program to check if a number is Positive or Negative.

num = int(input("Enter the number: "))

if num > 0:
    print(f"{num} is a positive number")
elif num < 0:
    print(f"{num} is a negative number")
else:
    print(f"{num} is equal to Zero(0)")