# Write a program to compute cosine of x. The user should supply x and a positive integer n. We compute the cosine of x using the series and the computation should use all terms in the series up through the term involving xn cos x = 1 - x2/2! + x4/4! - x6/6! ....

import math

x = float(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))

if n <= 0:
    print("The number of terms must be a positive integer.")
    exit()
    
cos_val = 1

print(f"sin({x}) = 1 ", end="")
for i in range(1, n):
    term_pow = 2 * i
    term = ((-1) ** i) * (x ** term_pow) / math.factorial(term_pow)
    cos_val += term
    print(f"{'-' if i % 2 == 0 else '+'} {x}^{term_pow}/{term_pow}! ", end="")

print(f"= {cos_val}")