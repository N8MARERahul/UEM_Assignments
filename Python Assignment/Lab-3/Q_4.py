# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).

def reverse_list(arr):
    reversed_arr = []
    for i in range(len(arr)-1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

# Test the function

print("Enter data for the Array(Type '-1' to exit): ")
arr = []
while True:
    data = int(input("-> "))
    if data == -1:
        break
    arr.append(data)
print(f"Array -> {arr}") 
print(f"Reversed Array -> {reverse_list(arr)}") 
