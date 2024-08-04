# 1
# 2 3 4
# 5 6 7 8 9

n = int(input("Enter the height: "))
count = 1
col = 1
for _ in range(n):
    for _ in range(col):
        print(count, end=" ")
        count += 1
    col += 2
    print()