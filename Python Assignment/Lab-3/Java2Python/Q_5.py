#       1
#     2 1 2
#   3 2 1 2 3
# 4 3 2 1 2 3 4

n = int(input("Enter the height: "))
col = 1
for i in range(n):
    for _ in range(n - i - 1):
        print(" ", end=" ")
    
    val = i + 1
    for _ in range(col):
        if val == 0:
            val -= 2
        print(f"{abs(val)}", end=" ")
        val -= 1
    
    col += 2
    print()