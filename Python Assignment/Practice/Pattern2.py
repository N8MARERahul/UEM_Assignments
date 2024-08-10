#   * * * * * * *
#   * * *   * * *
#   * *       * *
#   *           *
#   * *       * *
#   * * *   * * *
#   * * * * * * *

def print_star_pattern(n):
    N = n // 2
    for i in range(N + 1):
        if i == 0:
            print("* " * (N - i) + "* " + "* " * (N - i))
        else:
            print("* " * (N - i + 1) + ("* " if i == 0 else "  " * (i * 2 - 1)) + "* " * (N - i + 1))
    for i in range(N - 1, -1, -1):
        if i == 0:
            print("* " * (N - i) + "* " + "* " * (N - i))
        else:
            print("* " * (N - i + 1) + ("* " if i == 0 else "  " * (i * 2 - 1)) + "* " * (N - i + 1))

    
n = int(input("Enter the height of the diamond(odd number): "))

print_star_pattern(n)