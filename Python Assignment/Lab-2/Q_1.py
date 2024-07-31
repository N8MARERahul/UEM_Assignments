# To find the sum of square root of any three numbers.

print("Enter any positive numbers ->")
n1 = int(input("Enter the 1st number: "))
n2 = int(input("Enter the 2nd number: "))
n3 = int(input("Enter the 3rd number: "))

sum = n1 ** 0.5 + n2 ** 0.5 + n3 ** 0.5

print(f"Sum = {round(sum, 3)}")