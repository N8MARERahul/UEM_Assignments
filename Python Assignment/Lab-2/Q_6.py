# Define a sum function with two parameters and call the function

def sum(n1, n2):
    return n1 + n2

def main():
    n1 = int(input("Enter the 1st number: "))
    n2 = int(input("Enter the 2nd number: "))

    print(f"SUM = {sum(n1, n2)}")

if __name__ == "__main__":
    main()