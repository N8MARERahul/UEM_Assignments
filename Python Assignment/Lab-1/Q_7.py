# Write a program which makes use of function to display all such numbers which are divisible by 7 but are not a multiple of 5, between 1000 and 2000.

def divisibleBy5(num):
    end = num % 10
    if end == 5 or end == 0:
        return True
    return False

def divisibleBy7(num):
    return num % 7 == 0

for i in range(1000, 2000):
    if divisibleBy7(i) and not divisibleBy5(i):
        print(i, end=", ")