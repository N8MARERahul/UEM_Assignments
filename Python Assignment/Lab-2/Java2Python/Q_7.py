# Write a Java program to count the number of digits of an integer.

num = int(input("Enter a number: "))

digit = 0
while num != 0:
    digit += 1
    num //= 10

print(f"Total digits = {digit}")