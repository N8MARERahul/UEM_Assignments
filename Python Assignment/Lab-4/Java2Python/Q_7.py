# Write a Java program to enter n elements in an array and find smallest number among them.

arr = list(map(int, input("Enter the elements of the array seperated by space: ").split()))

print(f"Smallest element = {min(arr)}")