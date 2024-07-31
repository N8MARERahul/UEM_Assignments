# Write a Java program to find LCM of two Numbers.

def hcf(n1, n2):
    hcf = 1
    for i in range(2, n1 + 1 if n1 < n2 else n2 + 1):
        if n1 % i == 0 and n2 % i == 0:
            hcf = i
    
    return hcf

def main():
    n1 = int(input("Enter the 1st number: "))
    n2 = int(input("Enter the 2nd number: "))

    print(f"LCM = {n1 * n2 // hcf(n1, n2)}")

if __name__ == "__main__":
    main()