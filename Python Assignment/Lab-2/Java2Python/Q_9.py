# Write a Java program to convert a Binary Number to Decimal

binary = input("Enter a binary number: ")

length = len(binary) - 1

decimal = 0

for i in binary:
    if i == '1':
        decimal += 2 ** length
    length -= 1

print(f"Decimal = {decimal}")