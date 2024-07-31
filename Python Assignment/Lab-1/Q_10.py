# WAP to generate the Fibonacci series upto n.

num = int(input("Enter the value of n: "))

if num < 0: 
    print("Please enter a number greater or equal to 0")
    exit()

n1 = 0 
n2 = 1

print(f"The Fibonacci series upto {num} is ->")
if num >= n1:
    print(n1, end="")
if num >= n2:
    print(f", {n2}", end="")
if num >= n1 + n2: 
    while num >= n1 + n2:
        n = n1 + n2
        print(f", {n}", end="")
        n1, n2 = n2, n
