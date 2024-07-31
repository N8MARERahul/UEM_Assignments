# WAP to generate prime number series up to n

n = int(input("Enter the value of n: "))

for i in range(2, n + 1):
    flag = True
    for j in range(2, i//2 + 1):
        if i % j == 0:
            flag = False
            break
    if flag:
        print(i, end= ", ")