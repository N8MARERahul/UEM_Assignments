# Print the pattern upto N Lines:
#
#  .        .         .
#  /_\      /\       /\
#
#           /__\     / \
#
#                   /___\
#  N=2      N=3      N=4

n = int(input("Enter the value of n: "))

for i in range(n):
    if i == 0:
        print("\b.")
    elif i == n - 1:
        print("/", end="")
        for x in range(n - 1):
            print("_", end="")
        print("\\")
    else:
        print("/", end="")
        for k in range(i - 1):
            print(" ", end="")
        print("\\")

