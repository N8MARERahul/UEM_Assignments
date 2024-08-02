# Compute the sum up to n terms in the series 1 - 1/2 + 1/3 - 1/4 + 1/5 -... 1/n where n is a positive integer and input by user.

n = int(input("Enter a positive integer: "))

sum = 1
sign = -1
print("1", end=" ")
for i in range(2, n + 1):
    sum += 1 / i * sign
    print(f"{'-' if sign == -1 else '+'} 1/{i}", end=" ")
    sign = -1 if sign == 1 else 1

print(f"= {sum}")