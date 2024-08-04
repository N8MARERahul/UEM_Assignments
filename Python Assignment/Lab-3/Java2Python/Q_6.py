# 1     1
#  2   2
#   3 3
#    4

n = int(input("Enter the height: "))

for i in range(n):
    for _ in range(i):
        print(" ", end="")
    
    print(i + 1, end=" ")
    for _ in range(n - i * 2):
        print(" ", end="")

    if i != n - 1:
        print(i + 1)