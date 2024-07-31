# Write a Java program to find median of a set of numbers.

set = input("Enter the comma separated set of numbers: ")

list = [float(s.strip()) for s in set.split(",")]

length = len(list)

if length % 2 != 0:
    print(f"Median = {list[length // 2]}")
else:
    print(f"Median = {(list[length // 2] + list[length // 2 - 1]) / 2}")
