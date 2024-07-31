# Convert Decimal number to Binary

num = int(input("Enter the number: "))

binary = ""

while num > 0:
    rem = num % 2
    binary = str(rem) + binary
    num //= 2

print(f"Binary = {binary}")