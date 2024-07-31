# Write a function to calculate the power of a number using recursion

def power(base, exponent):
    if exponent < 0:
        return (1 / base) * power(base, exponent + 1)
    elif exponent == 0:
        return 1
    elif exponent == 1:
        return base
    else:
        return base * power(base, exponent - 1)

def main():
    base = int(input("Enter the base value: "))
    exp = int(input("Enter the exponent value: "))

    print(f"Ans = {power(base, exp)}")

if __name__ == "__main__":
    main()