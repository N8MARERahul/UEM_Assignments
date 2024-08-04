# Write a Java program to read two integer values m and n and to decide and print whether m is multiple of n.

m = int(input("Enter the value for m: "))
n = int(input("Enter the value for n: "))

if m % n == 0:
    print(f"m({m}) is multiple of n({n})")
else:
    print(f"m({m}) is not multiple of n({n})")
