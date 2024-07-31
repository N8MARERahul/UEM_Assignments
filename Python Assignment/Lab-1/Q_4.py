# reverse a number

num = int(input("Enter the number: "))

rev = 0

n = num
while n > 0:
    digit = n % 10
    rev = 10 * rev + digit
    n = n//10

print(f"Reverse of {num} = {rev}")
