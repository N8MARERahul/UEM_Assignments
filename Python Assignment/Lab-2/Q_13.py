# Write a Python program to print the first 6 terms of a geometric sequence starting with 2 and having a common ratio of 3.

print("Sequence ->")

term = 2
for i in range(6):
    print(term, end=", ")
    term *= 3