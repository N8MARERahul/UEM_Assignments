# Write a python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

num = int(input("Enter the hight of the pattern: "))

for i in range(1, num + 1):
    for j in range(1, num + 1):
        if j == 1 or j == 3:
            print(i, end=" ")
        elif j == 2:
            print("1", end=" ")
        else:
            print(i ** (j - 2), end=" ")
    print("")