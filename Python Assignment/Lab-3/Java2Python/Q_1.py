# Write a program to compute the value of Euler’s number that is used as the base of natural logarithms. Use the following formula.
# e= 1+ 1/1! +1 /2! + 1/3+................ 1/n!

import math

def compute_e(terms):
    e_value = 1.0
    print("1", end=" ")
    for i in range(1, terms + 1):
        print(f"+ 1/{i}!", end=" ")
        e_value += 1 / math.factorial(i)
    print(f" = {e_value}")
    return e_value

terms = int(input("Enter the no of Terms: "))
print(f"Approximation of Euler's number e with {terms} terms: {compute_e(terms)}")