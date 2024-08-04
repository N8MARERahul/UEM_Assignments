# Write a Java program to calculate Sum & Average of an integer array.

length = int(input("Enter the length of the array: "))
arr = []

for i in range(length):
    arr.append(int(input(f"Enter the {i + 1} value: ")))
total_sum = sum(arr)
print(f"Array = {arr}")
print(f"Sum = {total_sum}")
print(f"Average = {total_sum / length if length > 0 else 0}")
