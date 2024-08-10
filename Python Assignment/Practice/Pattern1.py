#         *
#       *   *
#     *       *
#   *           *
#     *       *
#       *   *
#         *

def print_star_pattern(n):
    for i in range(n//2 + 1):
        for _ in range(n - (i * 2) - 1):
            print(" ", end="")
        if i == 0:
            print("*")
        else:
            print("*", end="")
            for _ in range(4 * i - 1):
                print(" ", end="")
            print("*")

    for i in range(n//2 - 1, -1, -1):
        for _ in range(n - (i * 2) - 1):
            print(" ", end="")
        if i == 0:
            print("*")
        else:
            print("*", end="")
            for _ in range(4 * i - 1):
                print(" ", end="")
            print("*")


    
n = int(input("Enter the height of the diamond(odd number): "))

print_star_pattern(n)