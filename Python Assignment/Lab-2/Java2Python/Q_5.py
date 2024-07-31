# Write a Java program to print all multiple of 10 between a given interval.

lower = int(input("Enter the Lower limit: "))
upper = int(input("Enter the Upper limit: "))

for i in range(lower, upper):
    if i % 10 == 0:
        print(i, end=" ")