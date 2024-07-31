# Find GCD of two numbers

n1 = int(input("Enter the 1st number: "))
n2 = int(input("Enter the 2nd number: "))

gcd = 1
for i in range(2, n1 + 1 if n1 < n2 else n2 + 1):
    if n1 % i == 0 and n2 % i == 0:
        gcd = i

print(f"GCD = {gcd}")