# Print the series upto N terms: 1,2,6,24,120,720 …

n = int(input("Enter the value of N: "))

value = 1
for i in range(1, n + 1):
    value = value * i
    print(value, end=", ")
