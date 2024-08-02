# Write a program to compute sin x for given x. The user should supply x and a positive integer n. We compute the sine of x using the series and the computation should use all terms in the series up through the term involving xn sin x = x - x3/3! + x5/5! - x7/7! + x9/9! ........

import math

x = float(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))
if n <= 0:
    print("The number of terms must be a positive integer.")
    exit()
    
sin_val = x

print(f"sin({x}) = {x} ", end="")
for i in range(1, n):
    term_pow = 2 * i + 1
    term = ((-1) ** i) * (x ** term_pow) / math.factorial(term_pow)
    sin_val += term
    print(f"{'-' if i % 2 == 0 else '+'} {x}^{term_pow}/{term_pow}! ", end="")

print(f"= {sin_val}")