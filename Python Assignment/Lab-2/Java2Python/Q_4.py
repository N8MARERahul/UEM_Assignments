# Write a Java program to calculate the sum of natural numbers up to a certain range.

n_range = int(input("Enter the range of the Natural number: "))

sum = 0
for i in range(1, n_range):
    print(i, end=" + ")
    sum += i

print(f"{n_range} = {sum + n_range}")